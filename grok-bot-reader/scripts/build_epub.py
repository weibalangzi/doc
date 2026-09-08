#!/usr/bin/env python3
"""Build a mobile-friendly EPUB of Grok Bot usage guides for WeChat Reading."""

from __future__ import annotations

import argparse
import html
import re
import uuid
from pathlib import Path

import markdown
from ebooklib import epub

BOOK_TITLE = "Grok Bot 使用介绍（手机阅读版）"
BOOK_AUTHOR = "X社区整理 · 橙皮书 · 官方文档摘要"
BOOK_LANG = "zh"
BOOK_SOURCE = "https://docs.x.ai/grok-bot/ · https://github.com/KinGao294/grok-bot-orange-book"

IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
HEADING_H2_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)

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
li p {
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
.fig {
  margin: 0.7em 0;
  padding: 0.45em 0.7em;
  background: #f8f8f8;
  border: 1px dashed #ccc;
  color: #555;
  font-size: 0.9em;
  text-indent: 0;
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
    return s[:48] or "chapter"


def rewrite_images(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        alt = (m.group(1) or "").strip() or "配图"
        url = m.group(2).strip()
        return (
            f'\n\n<p class="fig">〔{html.escape(alt)}〕 '
            f"{html.escape(url)}</p>\n\n"
        )

    return IMG_RE.sub(repl, text)


def prepare_md(raw: str, title: str) -> str:
    text = raw.replace("\r\n", "\n").replace("\r", "\n").strip()
    text = rewrite_images(text)
    # Drop leading H1; we inject chapter title.
    text = re.sub(r"^#\s+.+\n+", "", text.lstrip(), count=1)
    # Demote leftover H1 so only the injected title is H1.
    text = re.sub(r"^#\s+", "## ", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return f"# {title}\n\n{text}\n"


def md_to_xhtml_body(md_text: str) -> str:
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


def split_orange_book(path: Path) -> list[tuple[str, str, str]]:
    """Return list of (section, title, markdown_body)."""
    text = path.read_text(encoding="utf-8")
    text = re.sub(
        r"^#\s+(Part\s+\d+[^\n]*|附录)\s*$",
        r"<!--SECTION:\1-->",
        text,
        flags=re.MULTILINE,
    )
    parts = re.split(r"\n(?=## )", text)
    chapters: list[tuple[str, str, str]] = []
    section = "橙皮书"

    for part in parts:
        part = part.strip()
        # Section markers may sit before a chapter or at the end of the previous body.
        leading = re.match(r"<!--SECTION:([^>]+)-->\s*", part)
        if leading:
            section = f"橙皮书 · {leading.group(1).strip()}"
            part = part[leading.end() :].strip()

        trailing_secs = list(re.finditer(r"<!--SECTION:([^>]+)-->", part))
        pending_section = None
        if trailing_secs:
            pending_section = f"橙皮书 · {trailing_secs[-1].group(1).strip()}"
            part = re.sub(r"\n?<!--SECTION:[^>]+-->\s*", "\n", part).strip()

        if not part.startswith("## "):
            if pending_section:
                section = pending_section
            continue

        title_line, _, body = part.partition("\n")
        title = title_line[3:].strip()
        if title == "目录":
            if pending_section:
                section = pending_section
            continue
        body = body.strip()
        body = re.sub(r"\n---\s*$", "", body).strip()
        if body:
            chapters.append((section, title, f"# {title}\n\n{body}\n"))
        if pending_section:
            section = pending_section
    return chapters


def load_front_chapters(chapters_dir: Path) -> list[tuple[str, str, str]]:
    files = sorted(chapters_dir.glob("*.md"))
    out: list[tuple[str, str, str]] = []
    for path in files:
        raw = path.read_text(encoding="utf-8")
        m = re.match(r"^#\s+(.+)$", raw.lstrip(), re.MULTILINE)
        title = m.group(1).strip() if m else path.stem
        out.append(("导读与精选", title, raw))
    return out


def build_epub(
    chapters_dir: Path,
    orange_path: Path,
    out_path: Path,
) -> int:
    items: list[tuple[str, str, str]] = []
    items.extend(load_front_chapters(chapters_dir))
    items.extend(split_orange_book(orange_path))
    if not items:
        print("No chapters found", flush=True)
        return 1

    book = epub.EpubBook()
    book.set_identifier(f"urn:uuid:{uuid.uuid4()}")
    book.set_title(BOOK_TITLE)
    book.set_language(BOOK_LANG)
    book.add_author(BOOK_AUTHOR)
    book.add_metadata("DC", "source", BOOK_SOURCE)
    book.add_metadata(
        "DC",
        "description",
        "X 推文/文章中的 Grok Bot 使用介绍精华 + 橙皮书 + 官方入门摘要，手机排版。",
    )

    style = epub.EpubItem(
        uid="style_main",
        file_name="style/main.css",
        media_type="text/css",
        content=MOBILE_CSS.encode("utf-8"),
    )
    book.add_item(style)

    cover = epub.EpubHtml(title="封面", file_name="cover.xhtml", lang=BOOK_LANG)
    cover.set_content(
        f"""
<div class="cover">
  <h1>{html.escape(BOOK_TITLE)}</h1>
  <p class="sub">{html.escape(BOOK_AUTHOR)}</p>
  <p class="sub">微信读书 / 手机阅读适配版</p>
</div>
<p class="no-indent" style="margin-top:2.5em;color:#666;font-size:0.9em;">
整理自公开 X 文章、橙皮书与官方文档摘要。<br/>
产品迭代快，价格与规则以官方最新为准。
</p>
"""
    )
    cover.add_item(style)
    book.add_item(cover)

    used: set[str] = set()
    chapter_hrefs: list[tuple[str, str, str]] = []
    spine_chapters: list[epub.EpubHtml] = []

    for idx, (section, title, raw) in enumerate(items, start=1):
        base = f"c{idx:03d}-{slugify(title)}"
        while base in used:
            base += "x"
        used.add(base)
        href = f"{base}.xhtml"
        md_text = prepare_md(raw, title)
        body = md_to_xhtml_body(md_text)
        crumb = f'<p class="chapter-meta">{html.escape(section)}</p>\n'
        body = re.sub(
            r"(<h1[^>]*>.*?</h1>)",
            r"\1\n" + crumb,
            body,
            count=1,
            flags=re.DOTALL,
        )
        chapter = epub.EpubHtml(
            title=title,
            file_name=href,
            lang=BOOK_LANG,
            uid=base,
        )
        chapter.set_content(body)
        chapter.add_item(style)
        book.add_item(chapter)
        spine_chapters.append(chapter)
        chapter_hrefs.append((section, title, href))

    toc_parts = [
        '<div class="toc-page">',
        "<h1>目录</h1>",
        f'<p class="chapter-meta">{html.escape(BOOK_TITLE)}</p>',
    ]
    current = None
    for section, title, href in chapter_hrefs:
        if section != current:
            if current is not None:
                toc_parts.append("</ul>")
            toc_parts.append(f'<p class="sec">{html.escape(section)}</p>')
            toc_parts.append("<ul>")
            current = section
        toc_parts.append(
            f'<li><a href="{html.escape(href)}">{html.escape(title)}</a></li>'
        )
    if current is not None:
        toc_parts.append("</ul>")
    toc_parts.append("</div>")

    toc_page = epub.EpubHtml(title="目录", file_name="toc-page.xhtml", lang=BOOK_LANG)
    toc_page.set_content("\n".join(toc_parts))
    toc_page.add_item(style)
    book.add_item(toc_page)

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
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--chapters",
        type=Path,
        default=root / "chapters",
    )
    parser.add_argument(
        "--orange",
        type=Path,
        default=root / "source" / "Grok-Bot-橙皮书.md",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=root / "output" / "Grok-Bot-使用介绍-手机阅读版.epub",
    )
    args = parser.parse_args()
    return build_epub(args.chapters, args.orange, args.out)


if __name__ == "__main__":
    raise SystemExit(main())
