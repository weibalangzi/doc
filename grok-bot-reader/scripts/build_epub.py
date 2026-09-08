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
TABLE_RE = re.compile(r"<table>.*?</table>", re.DOTALL | re.IGNORECASE)
MD_TABLE_RE = re.compile(
    r"(?:^\|.+\|\s*\n)+^\|[-:| ]+\|\s*\n(?:^\|.+\|\s*\n?)+",
    re.MULTILINE,
)

MOBILE_CSS = """
@namespace epub "http://www.idpf.org/2007/ops";

html {
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
  padding: 0.75em 0.85em 1.6em;
  font-family: "PingFang SC", "Hiragino Sans GB", "Noto Sans CJK SC",
               "Source Han Sans SC", "Microsoft YaHei", sans-serif;
  font-size: 1em;
  line-height: 1.9;
  color: #1f1f1f;
  word-wrap: break-word;
  overflow-wrap: break-word;
  -webkit-font-smoothing: antialiased;
}
h1, h2, h3, h4, h5, h6 {
  font-weight: 600;
  line-height: 1.4;
  text-indent: 0;
  text-align: left;
  margin: 1.35em 0 0.55em;
  page-break-after: avoid;
  page-break-inside: avoid;
}
h1 {
  font-size: 1.28em;
  margin-top: 0.25em;
  margin-bottom: 0.35em;
  padding-bottom: 0.4em;
  border-bottom: 1px solid #e5e5e5;
  letter-spacing: 0.01em;
}
h2 {
  font-size: 1.12em;
  margin-top: 1.55em;
  padding-top: 0.15em;
}
h3 {
  font-size: 1.02em;
  margin-top: 1.25em;
  color: #333;
}
h4, h5, h6 {
  font-size: 1em;
  color: #444;
}
p {
  margin: 0.65em 0;
  text-align: justify;
  text-justify: inter-ideograph;
  text-indent: 2em;
  widows: 2;
  orphans: 2;
}
p.no-indent,
p.chapter-meta,
p.fig,
p.source,
p.lead,
li p,
.kv p,
.card p {
  text-indent: 0;
}
p.lead {
  color: #444;
  margin: 0.4em 0 0.9em;
}
.chapter-meta {
  color: #888;
  font-size: 0.82em;
  text-align: left;
  margin: 0 0 1em;
  letter-spacing: 0.02em;
}
ul, ol {
  margin: 0.55em 0 0.85em;
  padding-left: 1.35em;
}
li {
  margin: 0.35em 0;
  text-indent: 0;
  line-height: 1.75;
  padding-left: 0.1em;
}
blockquote {
  margin: 0.9em 0;
  padding: 0.65em 0.8em;
  border-left: 0.2em solid #b0b0b0;
  background: #f7f7f7;
  color: #333;
  border-radius: 0 0.2em 0.2em 0;
}
blockquote p {
  text-indent: 0;
  margin: 0.3em 0;
  text-align: left;
  line-height: 1.75;
}
code {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.86em;
  word-break: break-all;
  background: #f3f3f3;
  padding: 0.05em 0.25em;
  border-radius: 0.15em;
}
pre {
  margin: 0.85em 0;
  padding: 0.75em 0.8em;
  background: #f5f5f5;
  border: 1px solid #ebebeb;
  border-radius: 0.3em;
  overflow-x: auto;
  white-space: pre-wrap;
  word-break: break-word;
  line-height: 1.55;
  font-size: 0.84em;
  page-break-inside: avoid;
}
pre code {
  font-size: inherit;
  word-break: break-word;
  background: transparent;
  padding: 0;
}
a {
  color: #2f5faf;
  text-decoration: none;
  word-break: break-all;
}
hr {
  border: 0;
  border-top: 1px solid #ececec;
  margin: 1.35em 0;
}
strong {
  font-weight: 600;
}
em {
  font-style: normal;
  color: #555;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin: 0.85em 0;
  font-size: 0.9em;
  display: block;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}
th, td {
  border: 1px solid #ddd;
  padding: 0.4em 0.55em;
  text-align: left;
  word-break: break-word;
  vertical-align: top;
}
th {
  background: #f3f3f3;
  font-weight: 600;
}
.fig, .source {
  margin: 0.7em 0;
  padding: 0.45em 0.7em;
  background: #f8f8f8;
  border: 1px dashed #d5d5d5;
  color: #666;
  font-size: 0.88em;
  text-indent: 0;
  text-align: left;
}
.card {
  margin: 0.7em 0;
  padding: 0.65em 0.75em;
  background: #fafafa;
  border: 1px solid #ececec;
  border-radius: 0.3em;
  page-break-inside: avoid;
}
.card .k {
  font-weight: 600;
  color: #222;
  margin: 0 0 0.25em;
  text-indent: 0;
  text-align: left;
}
.card .v {
  margin: 0;
  color: #333;
  text-indent: 0;
  text-align: left;
  line-height: 1.7;
}
.kv {
  margin: 0.75em 0 1em;
}
.kv-row {
  margin: 0 0 0.65em;
  padding-bottom: 0.55em;
  border-bottom: 1px solid #f0f0f0;
}
.kv-row:last-child {
  border-bottom: 0;
  padding-bottom: 0;
}
.cover {
  text-align: center;
  padding: 18vh 0.4em 2em;
}
.cover h1 {
  border: 0;
  font-size: 1.45em;
  margin-bottom: 0.7em;
  text-align: center;
  line-height: 1.35;
}
.cover .sub {
  color: #666;
  font-size: 0.92em;
  text-indent: 0;
  text-align: center;
  margin: 0.35em 0;
  line-height: 1.6;
}
.toc-page h1 {
  border: 0;
  text-align: center;
}
.toc-page .sec {
  margin: 1.2em 0 0.4em;
  font-weight: 600;
  font-size: 1.02em;
  text-indent: 0;
  color: #333;
}
.toc-page ul {
  list-style: none;
  padding-left: 0;
  margin: 0.15em 0 0.85em;
}
.toc-page li {
  margin: 0.42em 0;
  padding: 0.15em 0.1em;
  line-height: 1.55;
  border-bottom: 1px solid #f3f3f3;
}
.toc-page a {
  color: #222;
  display: block;
}
"""


def slugify(text: str) -> str:
    s = re.sub(r"[^\w\-]+", "-", text, flags=re.UNICODE).strip("-").lower()
    return s[:48] or "chapter"


def short_toc_title(title: str, limit: int = 22) -> str:
    """Shorter titles for WeChat Reading long-press chapter list."""
    t = re.sub(r"\s+", " ", title).strip()
    # Drop redundant book prefixes already shown via grouping
    t = re.sub(r"^附表[一二三四]：", "", t)
    if len(t) <= limit:
        return t
    # Prefer cut at Chinese punctuation / colon
    for sep in ("：", ":", "·", "—", "-", "（"):
        if sep in t[: limit + 2]:
            head = t.split(sep, 1)[0].strip()
            if 6 <= len(head) <= limit:
                return head
    return t[: limit - 1] + "…"


def rewrite_images(text: str) -> str:
    def repl(m: re.Match[str]) -> str:
        alt = (m.group(1) or "").strip() or "配图"
        url = m.group(2).strip()
        return (
            f'\n\n<p class="fig">〔{html.escape(alt)}〕 '
            f"{html.escape(url)}</p>\n\n"
        )

    return IMG_RE.sub(repl, text)


def md_table_to_cards(table_md: str) -> str:
    lines = [ln.strip() for ln in table_md.strip().splitlines() if ln.strip()]
    if len(lines) < 2:
        return table_md
    rows = []
    for ln in lines:
        if re.match(r"^\|?\s*[-:| ]+\s*\|?$", ln):
            continue
        cells = [c.strip() for c in ln.strip("|").split("|")]
        rows.append(cells)
    if len(rows) < 2:
        return table_md
    headers = rows[0]
    body = rows[1:]
    # 2-column comparison / role tables → stacked cards
    if len(headers) == 2:
        out = ['<div class="kv">']
        for row in body:
            while len(row) < 2:
                row.append("")
            k, v = row[0], row[1]
            out.append('<div class="kv-row card">')
            out.append(f'<p class="k">{k}</p>')
            out.append(f'<p class="v">{v}</p>')
            out.append("</div>")
        out.append("</div>")
        return "\n\n" + "\n".join(out) + "\n\n"
    # Wider tables: one card per row, label: value lines
    out = ['<div class="kv">']
    for row in body:
        out.append('<div class="kv-row card">')
        for i, cell in enumerate(row):
            label = headers[i] if i < len(headers) else f"列{i+1}"
            if i == 0:
                out.append(f'<p class="k">{cell}</p>')
            else:
                out.append(f'<p class="v"><strong>{label}</strong>：{cell}</p>')
        out.append("</div>")
    out.append("</div>")
    return "\n\n" + "\n".join(out) + "\n\n"


def convert_md_tables(text: str) -> str:
    return MD_TABLE_RE.sub(lambda m: md_table_to_cards(m.group(0)), text)


def normalize_horizontal_rules(text: str) -> str:
    # Keep section breathing room, but avoid dense --- noise
    text = re.sub(r"\n---+\n", "\n\n", text)
    return text


def promote_headings_after_title(text: str) -> str:
    """Ensure subsections under chapter H1 start at H2 (not H3)."""
    lines = text.splitlines()
    if not lines:
        return text
    # Detect minimum heading level among body headings (exclude first H1)
    levels: list[int] = []
    for i, line in enumerate(lines):
        if i == 0:
            continue
        m = re.match(r"^(#{2,6})\s+", line)
        if m:
            levels.append(len(m.group(1)))
    if not levels:
        return text
    min_level = min(levels)
    shift = min_level - 2  # want body headings to start at ##
    if shift <= 0:
        return text
    out: list[str] = []
    for i, line in enumerate(lines):
        if i == 0:
            out.append(line)
            continue
        m = re.match(r"^(#{2,6})(\s+.*)$", line)
        if m:
            new_level = max(2, len(m.group(1)) - shift)
            out.append("#" * new_level + m.group(2))
        else:
            out.append(line)
    return "\n".join(out)


def prepare_md(raw: str, title: str) -> str:
    text = raw.replace("\r\n", "\n").replace("\r", "\n").strip()
    text = rewrite_images(text)
    text = normalize_horizontal_rules(text)
    text = convert_md_tables(text)
    # Drop leading H1 (we inject our own title).
    text = re.sub(r"^#\s+.+\n+", "", text.lstrip(), count=1)
    # Demote leftover H1 so only the injected title is H1.
    text = re.sub(r"^#\s+", "## ", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    text = f"# {title}\n\n{text}\n"
    text = promote_headings_after_title(text)
    return text


def md_to_xhtml_body(md_text: str) -> str:
    # No nl2br: Chinese markdown already uses blank lines; nl2br densifies mobile text.
    body = markdown.markdown(
        md_text,
        extensions=[
            "markdown.extensions.fenced_code",
            "markdown.extensions.tables",
            "markdown.extensions.sane_lists",
        ],
        output_format="xhtml",
    )
    # First content paragraph after H1+meta feels better without indent.
    body = re.sub(
        r"(</h1>\s*(?:<p class=\"chapter-meta\">.*?</p>\s*)?)<p>",
        r'\1<p class="lead">',
        body,
        count=1,
        flags=re.DOTALL,
    )
    # Mark trailing source lines
    body = re.sub(
        r"<p>((?:公开出处|出处|来源|原帖)[^<]*)</p>",
        r'<p class="source">\1</p>',
        body,
    )
    return body


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


def split_front_file(path: Path) -> list[tuple[str, str, str]]:
    """Split a front markdown file by ## into multiple spine chapters when useful."""
    raw = path.read_text(encoding="utf-8")
    m = re.match(r"^#\s+(.+)$", raw.lstrip(), re.MULTILINE)
    top_title = m.group(1).strip() if m else path.stem
    # Only split the long X tips chapter; keep short notes intact.
    if "X 推文" not in top_title and "使用介绍精华" not in top_title:
        return [("导读与精选", top_title, raw)]

    body = re.sub(r"^#\s+.+\n+", "", raw.lstrip(), count=1)
    chunks = re.split(r"\n(?=## )", body.strip())
    out: list[tuple[str, str, str]] = []
    # Lead-in before first ##
    lead = chunks[0].strip() if chunks and not chunks[0].startswith("## ") else ""
    start_idx = 0
    if lead and not lead.startswith("## "):
        out.append(
            (
                "X 使用介绍",
                "X 精华导读",
                f"# X 精华导读\n\n{lead}\n",
            )
        )
        start_idx = 1
    for chunk in chunks[start_idx:]:
        chunk = chunk.strip()
        if not chunk.startswith("## "):
            continue
        title_line, _, rest = chunk.partition("\n")
        title = title_line[3:].strip()
        # Strip leading ordinal decoration for TOC clarity but keep in body H1
        rest = rest.strip()
        rest = re.sub(r"^---+\s*", "", rest)
        rest = re.sub(r"\n---+\s*$", "", rest)
        out.append(("X 使用介绍", title, f"# {title}\n\n{rest}\n"))
    return out or [("导读与精选", top_title, raw)]


def load_front_chapters(chapters_dir: Path) -> list[tuple[str, str, str]]:
    files = sorted(chapters_dir.glob("*.md"))
    out: list[tuple[str, str, str]] = []
    for path in files:
        out.extend(split_front_file(path))
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
        "X 推文/文章中的 Grok Bot 使用介绍精华 + 橙皮书 + 官方入门摘要，手机排版优化。",
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
  <p class="sub">微信读书 · 手机排版优化版</p>
</div>
<p class="no-indent" style="margin-top:2em;color:#666;font-size:0.9em;text-align:center;">
整理自公开 X 文章、橙皮书与官方文档摘要<br/>
产品迭代快，价格与规则以官方最新为准
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
        # Trailing rules look like accidental page breaks on phone.
        body = re.sub(r"(?:<hr\s*/?>\s*)+$", "", body.strip())
        body = re.sub(r"^(?:<hr\s*/?>\s*)+", "", body)
        ncx_title = short_toc_title(title)
        chapter = epub.EpubHtml(
            title=ncx_title,
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

    # Flat NCX: one entry per article for WeChat Reading long-press list.
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
