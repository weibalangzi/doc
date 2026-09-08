#!/usr/bin/env python3
"""Convert fq-book Docsify sources into a mobile-friendly EPUB for WeChat Reading."""

from __future__ import annotations

import argparse
import hashlib
import html
import io
import re
import sys
import uuid
from collections import OrderedDict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import markdown
from ebooklib import epub
from PIL import Image

BOOK_TITLE = "这本书能让你连接互联网"
BOOK_AUTHOR = "hoochanlon"
BOOK_LANG = "zh"

SIDEBAR_LINK_RE = re.compile(r"^\s*\*\s+\[([^\]]+)\]\(([^)]+)\)\s*$")
SIDEBAR_SECTION_RE = re.compile(r"^\s*\*\s+([^\[\*\n][^\n]*?)\s*$")
ALERT_LINE_RE = re.compile(
    r"^>\s*\[!(?P<label>important|tip|note|warning|caution|info)\]\s*(?P<body>.*)$",
    re.IGNORECASE,
)
DOCSIFY_TIP_RE = re.compile(r"^[>?!]{1,2}>\s*(.*)$")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
DETAILS_RE = re.compile(
    r"\*?<details>\s*<summary>(.*?)</summary>(.*?)</details>\*?",
    re.IGNORECASE | re.DOTALL,
)
HTML_TAG_RE = re.compile(
    r"</?(?:font|br\s*/?|b|i|u|span|div|p|summary|details|center|a)[^>]*>",
    re.IGNORECASE,
)
IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
INTERNAL_MD_LINK_RE = re.compile(
    r"\[([^\]]+)\]\((?!https?://|mailto:|#)([^)#?\s]+)(?:[?#][^)]*)?\)"
)
DOCSIFY_ABS_LINK_RE = re.compile(
    r"\[([^\]]+)\]\(/([^)?#\s]+)(?:[?#][^)]*)?\)"
)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$", re.MULTILINE)

LABEL_MAP = {
    "important": "重要",
    "tip": "提示",
    "note": "说明",
    "warning": "警告",
    "caution": "注意",
    "info": "信息",
}

MOBILE_CSS = """
@namespace epub "http://www.idpf.org/2007/ops";

html {
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
  padding: 0.9em 1em 1.4em;
  font-family: "PingFang SC", "Hiragino Sans GB", "Noto Sans CJK SC",
               "Source Han Sans SC", "Microsoft YaHei", sans-serif;
  font-size: 1em;
  line-height: 1.85;
  color: #222;
  word-wrap: break-word;
  overflow-wrap: break-word;
}
h1, h2, h3, h4, h5, h6 {
  font-weight: 600;
  line-height: 1.35;
  text-indent: 0;
  margin: 1.25em 0 0.55em;
  page-break-after: avoid;
}
h1 {
  font-size: 1.35em;
  text-align: center;
  margin-top: 0.4em;
  margin-bottom: 0.9em;
  padding-bottom: 0.45em;
  border-bottom: 1px solid #ddd;
}
h2 {
  font-size: 1.15em;
  margin-top: 1.4em;
}
h3 {
  font-size: 1.05em;
}
h4, h5, h6 {
  font-size: 1em;
}
p {
  margin: 0.55em 0;
  text-align: justify;
  text-indent: 2em;
  widows: 2;
  orphans: 2;
}
p.no-indent,
p.chapter-meta,
p.fig,
p.img-wrap,
li p {
  text-indent: 0;
}
.img-wrap {
  margin: 0.85em 0;
  text-align: center;
}
.img-wrap img {
  max-width: 100%;
  height: auto;
  display: inline-block;
}
.fig-missing {
  margin: 0.7em 0;
  padding: 0.45em 0.7em;
  background: #f8f8f8;
  border: 1px dashed #ccc;
  color: #777;
  font-size: 0.88em;
  text-indent: 0;
}
.chapter-meta {
  color: #777;
  font-size: 0.88em;
  text-align: center;
  margin: 0 0 1.1em;
}
ul, ol {
  margin: 0.5em 0 0.7em;
  padding-left: 1.4em;
}
li {
  margin: 0.28em 0;
  text-indent: 0;
  line-height: 1.7;
}
blockquote {
  margin: 0.85em 0;
  padding: 0.55em 0.85em;
  border-left: 0.22em solid #8a8a8a;
  background: #f6f6f6;
  color: #333;
}
blockquote p {
  text-indent: 0;
  margin: 0.35em 0;
}
code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.88em;
  word-break: break-all;
}
pre {
  margin: 0.8em 0;
  padding: 0.7em 0.8em;
  background: #f4f4f4;
  border-radius: 0.25em;
  overflow-x: auto;
  white-space: pre-wrap;
  word-break: break-word;
  line-height: 1.5;
  font-size: 0.86em;
}
pre code {
  font-size: inherit;
  word-break: break-word;
}
a {
  color: #2f5faf;
  text-decoration: none;
  word-break: break-all;
}
hr {
  border: 0;
  border-top: 1px solid #ddd;
  margin: 1.2em 0;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.8em 0;
  font-size: 0.92em;
  display: block;
  overflow-x: auto;
}
th, td {
  border: 1px solid #ccc;
  padding: 0.35em 0.5em;
  text-align: left;
  word-break: break-word;
}
.cover {
  text-align: center;
  padding-top: 28vh;
}
.cover h1 {
  border: 0;
  font-size: 1.55em;
  margin-bottom: 0.6em;
}
.cover .sub {
  color: #666;
  font-size: 0.95em;
  text-indent: 0;
  margin: 0.4em 0;
}
.toc-page h1 {
  border: 0;
}
.toc-page .sec {
  margin: 1.1em 0 0.35em;
  font-weight: 600;
  font-size: 1.05em;
  text-indent: 0;
}
.toc-page ul {
  list-style: none;
  padding-left: 0;
  margin: 0.2em 0 0.8em;
}
.toc-page li {
  margin: 0.35em 0;
  padding-left: 0.2em;
  line-height: 1.6;
}
.toc-page a {
  color: #222;
}
"""


def slugify(text: str) -> str:
    s = re.sub(r"[^\w\-]+", "-", text, flags=re.UNICODE).strip("-").lower()
    return s[:60] or "chapter"


def parse_sidebar(sidebar_text: str) -> list[tuple[str | None, str, str]]:
    chapters: list[tuple[str | None, str, str]] = []
    current_section: str | None = None
    for raw in sidebar_text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip() == "*":
            continue
        link = SIDEBAR_LINK_RE.match(line)
        if link:
            chapters.append((current_section, link.group(1).strip(), link.group(2).strip()))
            continue
        section = SIDEBAR_SECTION_RE.match(line)
        if section:
            current_section = section.group(1).strip()
    return chapters


def details_repl(m: re.Match[str]) -> str:
    summary = HTML_TAG_RE.sub("", m.group(1)).strip()
    summary = summary.strip("*").strip()
    body = m.group(2).strip().strip("*").strip()
    return f"**{summary}**\n\n{body}\n"


def normalize_docsify(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = HTML_COMMENT_RE.sub("", text)
    text = DETAILS_RE.sub(details_repl, text)
    text = re.sub(r"\*\*\s*\*\*", "", text)
    text = re.sub(r"^\*{2,}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"<br\s*/?>\s*", "\n", text, flags=re.IGNORECASE)
    # avoid blank lines introduced by "<br>\n" so tip continuations stay together
    text = re.sub(r"\n{3,}", "\n\n", text)

    lines = text.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        am = ALERT_LINE_RE.match(line)
        tip = DOCSIFY_TIP_RE.match(line) if not line.lstrip().startswith("> [") else None

        if am or tip:
            if am:
                label = LABEL_MAP.get(am.group("label").lower(), am.group("label"))
                chunks = [am.group("body").strip()]
            else:
                assert tip is not None
                if line.startswith("!>"):
                    label = "重要"
                elif line.startswith("?>"):
                    label = "提示"
                else:
                    label = "说明"
                chunks = [tip.group(1).strip()]
            i += 1
            # docsify callouts continue until blank line / heading / fence
            while i < len(lines):
                nxt = lines[i]
                if not nxt.strip():
                    break
                if nxt.lstrip().startswith(("#", "```")):
                    break
                if ALERT_LINE_RE.match(nxt) or DOCSIFY_TIP_RE.match(nxt):
                    break
                chunks.append(nxt.strip())
                i += 1
            body = " ".join(c for c in chunks if c)
            out.append(f"> **【{label}】** {body}" if body else f"> **【{label}】**")
            continue

        out.append(line)
        i += 1

    text = "\n".join(out)
    text = HTML_TAG_RE.sub("", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text


def collect_image_urls(texts: list[str]) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for text in texts:
        for m in IMG_RE.finditer(text):
            url = m.group(2).strip()
            if url.startswith(("http://", "https://")) and url not in seen:
                seen.add(url)
                found.append(url)
    return found


def _url_digest(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]


def compress_image(raw: bytes, max_side: int = 1280, quality: int = 72) -> tuple[bytes, str, str]:
    """Return (bytes, ext, mime). Prefer JPEG for screenshots."""
    img = Image.open(io.BytesIO(raw))
    img.load()
    if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
        img = img.convert("RGBA")
        background = Image.new("RGB", img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[-1])
        img = background
    elif img.mode != "RGB":
        img = img.convert("RGB")

    w, h = img.size
    scale = min(1.0, max_side / float(max(w, h)))
    if scale < 1.0:
        img = img.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.Resampling.LANCZOS)

    out = io.BytesIO()
    img.save(out, format="JPEG", quality=quality, optimize=True, progressive=True)
    return out.getvalue(), "jpg", "image/jpeg"


def fetch_one_image(url: str, cache_dir: Path) -> tuple[str, Path | None, str]:
    """Returns (url, local_path_or_None, note)."""
    digest = _url_digest(url)
    # cached?
    for ext in ("jpg", "jpeg", "png", "gif", "webp"):
        hit = cache_dir / f"{digest}.{ext}"
        if hit.is_file() and hit.stat().st_size > 0:
            return url, hit, "cache"

    req = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; fq-book-epub/1.0)",
            "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8",
        },
        method="GET",
    )
    try:
        with urlopen(req, timeout=25) as resp:
            raw = resp.read()
            ctype = (resp.headers.get("Content-Type") or "").split(";")[0].strip().lower()
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        return url, None, f"fail:{exc}"

    if not raw or len(raw) < 40:
        return url, None, "fail:empty"

    try:
        data, ext, _mime = compress_image(raw)
    except Exception:
        # fall back to original bytes with guessed extension
        if "png" in ctype:
            ext = "png"
        elif "gif" in ctype:
            ext = "gif"
        elif "webp" in ctype:
            ext = "webp"
        else:
            ext = "jpg"
        data = raw

    path = cache_dir / f"{digest}.{ext}"
    path.write_bytes(data)
    return url, path, "ok"


def download_images(urls: list[str], cache_dir: Path, workers: int = 12) -> dict[str, Path]:
    cache_dir.mkdir(parents=True, exist_ok=True)
    mapping: dict[str, Path] = {}
    ok = fail = 0
    print(f"Downloading {len(urls)} images...", flush=True)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(fetch_one_image, u, cache_dir) for u in urls]
        for i, fut in enumerate(as_completed(futures), start=1):
            url, path, note = fut.result()
            if path is not None:
                mapping[url] = path
                ok += 1
            else:
                fail += 1
            if i % 40 == 0 or i == len(futures):
                print(f"  images {i}/{len(futures)} ok={ok} fail={fail}", flush=True)
    return mapping


def rewrite_images(text: str, url_to_local: dict[str, Path], url_to_epub: dict[str, str]) -> str:
    def repl(m: re.Match[str]) -> str:
        alt = (m.group(1) or "").strip() or "配图"
        url = m.group(2).strip()
        epub_href = url_to_epub.get(url)
        if epub_href:
            return (
                f'\n\n<p class="img-wrap">'
                f'<img src="{html.escape(epub_href)}" alt="{html.escape(alt)}" />'
                f"</p>\n\n"
            )
        return (
            f'\n\n<p class="fig-missing">〔图片暂不可用：{html.escape(alt)}〕</p>\n\n'
        )

    return IMG_RE.sub(repl, text)


def rewrite_links(text: str, path_to_href: dict[str, str], title_by_path: dict[str, str]) -> str:
    def resolve(path: str) -> tuple[str, str]:
        path = path.lstrip("./")
        if path.endswith(".md"):
            key = path
        else:
            key = path if path.endswith(".md") else f"{path}.md"
        href = path_to_href.get(key)
        title = title_by_path.get(key)
        if not href:
            for k, v in path_to_href.items():
                if k.endswith("/" + key) or k == key or Path(k).stem == Path(path).stem:
                    href = v
                    title = title_by_path.get(k, title)
                    break
        return href or "", title or ""

    def md_link(m: re.Match[str]) -> str:
        label, path = m.group(1), m.group(2)
        href, title = resolve(path)
        if href:
            return f"[{label}]({href})"
        if title:
            return f"{label}（见「{title}」）"
        return label

    def abs_link(m: re.Match[str]) -> str:
        label, path = m.group(1), m.group(2)
        href, title = resolve(path if path.endswith(".md") else f"{path}.md")
        if not href:
            href, title = resolve(path)
        if href:
            return f"[{label}]({href})"
        if title:
            return f"{label}（见「{title}」）"
        return label

    text = INTERNAL_MD_LINK_RE.sub(md_link, text)
    text = DOCSIFY_ABS_LINK_RE.sub(abs_link, text)
    return text


def prepare_chapter_markdown(
    normalized: str,
    title: str,
    path_to_href: dict[str, str],
    title_by_path: dict[str, str],
    url_to_local: dict[str, Path],
    url_to_epub: dict[str, str],
) -> str:
    text = rewrite_images(normalized, url_to_local, url_to_epub)
    text = rewrite_links(text, path_to_href, title_by_path)

    text = re.sub(r"^#\s+.+\n+", "", text.lstrip(), count=1)
    text = re.sub(r"^#\s+", "## ", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return f"# {title}\n\n{text}\n"


def md_to_body_html(md_text: str) -> str:
    return markdown.markdown(
        md_text,
        extensions=[
            "markdown.extensions.fenced_code",
            "markdown.extensions.tables",
            "markdown.extensions.nl2br",
            "markdown.extensions.sane_lists",
        ],
        output_format="xhtml",
    )


def attach_style(item: epub.EpubHtml, style: epub.EpubItem) -> None:
    item.add_item(style)


def build_epub(docs_dir: Path, out_path: Path) -> int:
    sidebar = (docs_dir / "_sidebar.md").read_text(encoding="utf-8")
    entries = parse_sidebar(sidebar)
    if not entries:
        print("No chapters in _sidebar.md", file=sys.stderr)
        return 1

    used_names: set[str] = set()
    chapter_metas: list[dict] = []
    path_to_href: dict[str, str] = {}
    title_by_path: dict[str, str] = {}

    for idx, (section, title, rel) in enumerate(entries, start=1):
        src = docs_dir / rel
        if not src.is_file():
            print(f"skip missing: {rel}", file=sys.stderr)
            continue
        base = f"c{idx:03d}-{slugify(title)}"
        while base in used_names:
            base += "-x"
        used_names.add(base)
        # Keep chapters at EPUB root so stylesheet href `style/main.css` resolves.
        href = f"{base}.xhtml"
        path_to_href[rel] = href
        title_by_path[rel] = title
        chapter_metas.append(
            {
                "section": section,
                "title": title,
                "rel": rel,
                "src": src,
                "file_id": base,
                "href": href,
            }
        )

    book = epub.EpubBook()
    book.set_identifier(f"urn:uuid:{uuid.uuid4()}")
    book.set_title(BOOK_TITLE)
    book.set_language(BOOK_LANG)
    book.add_author(BOOK_AUTHOR)
    book.add_metadata("DC", "rights", "CC BY-NC 4.0")
    book.add_metadata("DC", "source", "https://hoochanlon.github.io/fq-book/#/")

    style = epub.EpubItem(
        uid="style_main",
        file_name="style/main.css",
        media_type="text/css",
        content=MOBILE_CSS.encode("utf-8"),
    )
    book.add_item(style)

    # Preload + normalize chapter markdown, then fetch images for embedding.
    normalized_bodies: dict[str, str] = {}
    for meta in chapter_metas:
        raw = meta["src"].read_text(encoding="utf-8", errors="replace")
        normalized_bodies[meta["rel"]] = normalize_docsify(raw)

    image_urls = collect_image_urls(list(normalized_bodies.values()))
    cache_dir = Path("/tmp/fq-book-image-cache")
    url_to_local = download_images(image_urls, cache_dir)

    url_to_epub: dict[str, str] = {}
    mime_by_ext = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "gif": "image/gif",
        "webp": "image/webp",
    }
    for i, (url, local) in enumerate(sorted(url_to_local.items(), key=lambda x: x[0])):
        ext = local.suffix.lstrip(".").lower() or "jpg"
        mime = mime_by_ext.get(ext, "image/jpeg")
        epub_name = f"images/img-{i:04d}-{local.stem}.{ext}"
        item = epub.EpubItem(
            uid=f"img_{i:04d}",
            file_name=epub_name,
            media_type=mime,
            content=local.read_bytes(),
        )
        book.add_item(item)
        url_to_epub[url] = epub_name

    print(
        f"Embedded images: {len(url_to_epub)}/{len(image_urls)}",
        flush=True,
    )

    cover = epub.EpubHtml(title="封面", file_name="cover.xhtml", lang=BOOK_LANG)
    cover.set_content(
        f"""
<div class="cover">
  <h1>{html.escape(BOOK_TITLE)}</h1>
  <p class="sub">作者：{html.escape(BOOK_AUTHOR)}</p>
  <p class="sub">微信读书 / 手机阅读适配版（含插图）</p>
</div>
<p class="no-indent" style="margin-top:2.5em;color:#666;font-size:0.9em;">
许可：CC BY-NC 4.0（非商用）<br/>
在线原书：https://hoochanlon.github.io/fq-book/#/
</p>
"""
    )
    attach_style(cover, style)
    book.add_item(cover)

    toc_sections: "OrderedDict[str | None, list[dict]]" = OrderedDict()
    for meta in chapter_metas:
        toc_sections.setdefault(meta["section"], []).append(meta)

    toc_parts = [
        '<div class="toc-page">',
        "<h1>目录</h1>",
        f'<p class="chapter-meta">{html.escape(BOOK_TITLE)}</p>',
    ]
    for section, items in toc_sections.items():
        if section:
            toc_parts.append(f'<p class="sec">{html.escape(section)}</p>')
        toc_parts.append("<ul>")
        for meta in items:
            toc_parts.append(
                f'<li><a href="{html.escape(meta["href"])}">{html.escape(meta["title"])}</a></li>'
            )
        toc_parts.append("</ul>")
    toc_parts.append("</div>")

    toc_page = epub.EpubHtml(title="目录", file_name="toc-page.xhtml", lang=BOOK_LANG)
    toc_page.set_content("\n".join(toc_parts))
    attach_style(toc_page, style)
    book.add_item(toc_page)

    spine_chapters: list[epub.EpubHtml] = []

    for meta in chapter_metas:
        md_body = prepare_chapter_markdown(
            normalized_bodies[meta["rel"]],
            meta["title"],
            path_to_href,
            title_by_path,
            url_to_local,
            url_to_epub,
        )
        # prepare_chapter_markdown calls normalize again — pass already normalized
        # by skipping double normalize: feed through rewrite only path.
        body_html = md_to_body_html(md_body)
        if meta["section"]:
            crumb = f'<p class="chapter-meta">{html.escape(meta["section"])}</p>\n'
            body_html = re.sub(
                r"(<h1[^>]*>.*?</h1>)",
                r"\1\n" + crumb,
                body_html,
                count=1,
                flags=re.DOTALL,
            )

        chapter = epub.EpubHtml(
            title=meta["title"],
            file_name=meta["href"],
            lang=BOOK_LANG,
            uid=meta["file_id"],
        )
        chapter.set_content(body_html)
        attach_style(chapter, style)
        book.add_item(chapter)
        spine_chapters.append(chapter)

    book.toc = tuple(spine_chapters)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    book.spine = ["nav", cover, toc_page, *spine_chapters]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    epub.write_epub(str(out_path), book, {})
    print(f"Articles: {len(spine_chapters)}")
    print(f"Wrote: {out_path} ({out_path.stat().st_size} bytes)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--docs-dir", type=Path, default=Path("/tmp/fq-book/docs"))
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "output",
    )
    args = parser.parse_args()
    epub_path = args.output_dir / f"{BOOK_TITLE}.epub"
    return build_epub(args.docs_dir, epub_path)


if __name__ == "__main__":
    raise SystemExit(main())
