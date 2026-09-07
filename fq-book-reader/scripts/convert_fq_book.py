#!/usr/bin/env python3
"""Convert hoochanlon/fq-book (Docsify) into EPUB for mobile readers."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

SIDEBAR_LINK_RE = re.compile(r"^\s*\*\s+\[([^\]]+)\]\(([^)]+)\)\s*$")
SIDEBAR_SECTION_RE = re.compile(r"^\s*\*\s+([^\[\*\n][^\n]*?)\s*$")
ALERT_RE = re.compile(
    r"^>\s*\[!(?P<label>important|tip|note|warning|caution|info)\]\s*(?P<body>.*)$",
    re.IGNORECASE | re.MULTILINE,
)
DETAILS_OPEN_RE = re.compile(
    r"<details>\s*<summary>(.*?)</summary>",
    re.IGNORECASE | re.DOTALL,
)
HTML_TAG_RE = re.compile(r"</?(?:font|br|b|i|u|span|div|p|summary|details)[^>]*>", re.IGNORECASE)
INTERNAL_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\((?!https?://|mailto:|#)([^)]+\.md)(?:#[^)]*)?\)")


def parse_sidebar(sidebar_text: str) -> tuple[list[tuple[str | None, str, str]], list[str]]:
    """Return [(section, title, rel_path), ...] and section-only headings in order."""
    chapters: list[tuple[str | None, str, str]] = []
    current_section: str | None = None
    sections: list[str] = []

    for raw in sidebar_text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.strip() == "*":
            continue
        link = SIDEBAR_LINK_RE.match(line)
        if link:
            title, rel = link.group(1).strip(), link.group(2).strip()
            chapters.append((current_section, title, rel))
            continue
        section = SIDEBAR_SECTION_RE.match(line)
        if section:
            name = section.group(1).strip()
            # skip nested blank / decorative items
            if name.startswith("特别篇"):
                current_section = name
                sections.append(name)
                continue
            current_section = name
            sections.append(name)
    return chapters, sections


def normalize_alerts(text: str) -> str:
    label_map = {
        "important": "重要",
        "tip": "提示",
        "note": "说明",
        "warning": "警告",
        "caution": "注意",
        "info": "信息",
    }

    def repl(m: re.Match[str]) -> str:
        label = label_map.get(m.group("label").lower(), m.group("label"))
        body = m.group("body").strip()
        if body:
            return f"> **【{label}】** {body}"
        return f"> **【{label}】**"

    return ALERT_RE.sub(repl, text)


def strip_htmlish(text: str) -> str:
    text = DETAILS_OPEN_RE.sub(r"**\1**\n", text)
    text = re.sub(r"</?details>", "", text, flags=re.IGNORECASE)
    text = HTML_TAG_RE.sub("", text)
    # docsify absolute in-book links like /abc/4dns?id=...
    text = re.sub(
        r"\[([^\]]+)\]\(/([^)?#]+)(?:\?id=([^)#]+))?(?:#([^)]+))?\)",
        lambda m: f"[{m.group(1)}](#{m.group(3) or m.group(4) or m.group(2)})",
        text,
    )
    return text


def rewrite_internal_links(text: str, title_by_path: dict[str, str]) -> str:
    def repl(m: re.Match[str]) -> str:
        label, path = m.group(1), m.group(2).lstrip("./")
        # keep label; append chapter hint if known
        mapped = title_by_path.get(path) or title_by_path.get(Path(path).name)
        if mapped and mapped != label:
            return f"[{label}（见「{mapped}」）](#)"
        return f"[{label}](#)"

    return INTERNAL_MD_LINK_RE.sub(repl, text)


def neutralize_remote_images(text: str) -> str:
    """Keep image URLs as readable links so pandoc does not embed/fetch them."""

    def repl(m: re.Match[str]) -> str:
        alt = (m.group(1) or "").strip()
        url = m.group(2).strip()
        label = alt if alt else "插图"
        return f"[{label}]({url})"

    return re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", repl, text)


def clean_chapter(text: str, title_by_path: dict[str, str]) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = normalize_alerts(text)
    text = strip_htmlish(text)
    text = neutralize_remote_images(text)
    text = rewrite_internal_links(text, title_by_path)
    # demote top-level H1 so book title remains the only book H1
    text = re.sub(r"^#\s+", "## ", text, count=1, flags=re.MULTILINE)
    # collapse excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def build_book_markdown(docs_dir: Path, chapters: list[tuple[str | None, str, str]]) -> str:
    title_by_path = {rel: title for _, title, rel in chapters}
    parts: list[str] = [
        "% 《这本书能让你连接互联网》\n",
        "% hoochanlon\n",
        "% \n",
        "\n",
        "# 《这本书能让你连接互联网》\n\n",
        "原书在线版：https://hoochanlon.github.io/fq-book/#/\n\n",
        "源仓库：https://github.com/hoochanlon/fq-book\n\n",
        "许可：Creative Commons BY-NC 4.0（允许非商用分享与演绎）\n\n",
        "本 EPUB 由 Docsify Markdown 源文件按官方目录自动转换，"
        "供微信读书等本地阅读器导入使用。原书插图为外链，"
        "已改为文中可点击链接（不嵌入图片），保证体积小、可离线读正文。\n\n",
        "---\n\n",
    ]

    last_section: str | None = None
    missing: list[str] = []

    for section, title, rel in chapters:
        path = docs_dir / rel
        if not path.is_file():
            missing.append(rel)
            continue
        if section and section != last_section:
            parts.append(f"# {section}\n\n")
            last_section = section
        body = clean_chapter(path.read_text(encoding="utf-8", errors="replace"), title_by_path)
        # ensure chapter title present
        if not body.lstrip().startswith("##"):
            body = f"## {title}\n\n{body}"
        else:
            # replace first heading text with sidebar title for consistency
            body = re.sub(r"^##\s+.+$", f"## {title}", body, count=1, flags=re.MULTILINE)
        parts.append(body)
        parts.append("\n\n")

    if missing:
        parts.append("# 转换说明\n\n")
        parts.append("以下目录条目在源仓库中缺失，已跳过：\n\n")
        for rel in missing:
            parts.append(f"- `{rel}`\n")
        parts.append("\n")

    return "".join(parts)


def run_pandoc(md_path: Path, epub_path: Path) -> None:
    cmd = [
        "pandoc",
        str(md_path),
        "-f",
        "markdown+pipe_tables+fenced_code_blocks+strikeout+autolink_bare_uris",
        "-t",
        "epub3",
        "-o",
        str(epub_path),
        "--toc",
        "--toc-depth=3",
        "--metadata",
        "title=《这本书能让你连接互联网》",
        "--metadata",
        "author=hoochanlon",
        "--metadata",
        "lang=zh-CN",
        "--metadata",
        "rights=CC BY-NC 4.0",
        "--split-level=1",
    ]
    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=Path("/tmp/fq-book/docs"),
        help="Path to fq-book docs/ directory",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "output",
        help="Directory for generated files",
    )
    args = parser.parse_args()

    docs_dir: Path = args.docs_dir
    out_dir: Path = args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    sidebar = (docs_dir / "_sidebar.md").read_text(encoding="utf-8")
    chapters, _ = parse_sidebar(sidebar)
    if not chapters:
        print("No chapters found in _sidebar.md", file=sys.stderr)
        return 1

    book_md = build_book_markdown(docs_dir, chapters)
    md_path = out_dir / "fq-book.md"
    epub_path = out_dir / "这本书能让你连接互联网.epub"

    md_path.write_text(book_md, encoding="utf-8")
    run_pandoc(md_path, epub_path)

    print(f"Chapters: {len(chapters)}")
    print(f"Wrote: {md_path}")
    print(f"Wrote: {epub_path} ({epub_path.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
