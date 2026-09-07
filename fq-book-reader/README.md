# fq-book → EPUB（微信读书可导入）

将 [《这本书能让你连接互联网》](https://hoochanlon.github.io/fq-book/#/)（Docsify）按官方 `_sidebar.md` 目录转换为 **EPUB**，便于微信读书等本地阅读器导入。

## 成品

| 文件 | 说明 |
|------|------|
| [`output/这本书能让你连接互联网.epub`](./output/这本书能让你连接互联网.epub) | 可导入微信读书的电子书 |
| [`output/fq-book.md`](./output/fq-book.md) | 转换用中间 Markdown（可再跑 pandoc） |

原书许可为 [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)，仅供非商用学习。

## 导入微信读书

1. 把 `这本书能让你连接互联网.epub` 传到手机（隔空投送、网盘、电脑助手等）
2. 微信读书 → **我** → **书架** / **本地导入**（或系统「打开方式」选微信读书）
3. 导入后即可离线阅读；目录来自原书侧边栏章节

> 书中插图多为外链（postimg / IPFS），离线时图片可能无法显示，正文完整。

## 重新生成

```bash
git clone --depth 1 https://github.com/hoochanlon/fq-book.git /tmp/fq-book
python3 scripts/convert_fq_book.py \
  --docs-dir /tmp/fq-book/docs \
  --output-dir output
```

依赖：`pandoc`（用于 Markdown → EPUB3）。
