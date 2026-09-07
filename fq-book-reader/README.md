# fq-book → 微信读书适配 EPUB

将 [《这本书能让你连接互联网》](https://hoochanlon.github.io/fq-book/#/) 按官方侧边栏转成**手机阅读友好**的 EPUB。

## 成品

[`output/这本书能让你连接互联网.epub`](./output/这本书能让你连接互联网.epub)

## 移动端适配要点

- **83 个独立章节**（一篇原文 = 一章），微信读书长按目录可直接跳转
- 目录只保留篇章标题，不混入正文小标题
- 书内另有分组「目录」页（按原书栏目）
- 中文手机排版：行距、段首缩进、代码换行、引用块、配图占位
- 清理 Docsify 语法（`!> / ?>`、details、HTML 碎片）
- 章间链接可跳转；外链配图改为「〔配图〕+ URL」避免破版

## 导入微信读书

1. 下载 EPUB 到手机  
2. 用微信读书打开 / 本地导入  
3. 长按屏幕 → 目录，应能看到全部章节

## 重新生成

```bash
git clone --depth 1 https://github.com/hoochanlon/fq-book.git /tmp/fq-book
python3 scripts/convert_fq_book.py --docs-dir /tmp/fq-book/docs --output-dir output
```

依赖：`python3`、`ebooklib`、`markdown`。

原书许可：[CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
