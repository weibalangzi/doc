# Grok Bot 使用介绍 · 手机阅读版

把 X 上关于 **Grok Bot** 的使用介绍推文/文章，整理成可在 **微信读书 / 手机** 阅读的 EPUB。

## 包含内容

1. **X 推文/文章精华**：幕僚长模式、组织图玩法、十分钟搭队、一周九课等（中文整理 + 出处）
2. **官方入门摘要**：docs.x.ai Get started 要点
3. **《Grok Bot 橙皮书》全文**：KinGao294 开源中文手册（v260823）

## 生成 EPUB

```bash
pip install ebooklib markdown
python3 grok-bot-reader/scripts/build_epub.py
```

输出：`grok-bot-reader/output/Grok-Bot-使用介绍-手机阅读版.epub`

## 导入微信读书

1. 把 EPUB 传到手机（隔空投送 / 网盘 / 邮件附件）
2. 用微信读书打开导入，或「我 → 书架 → + → 导入」
3. 长按目录可跳转各章（每篇独立章节；X 精华已按小节拆章）

## 手机排版要点

- 中文阅读行高 / 边距 / 左对齐长标题
- 小节标题层级校正（章下从 H2 起）
- 宽表转卡片式键值块，避免横滑
- 关闭 nl2br，减少手机上过密断行
- NCX 短标题，方便微信读书长按目录

## 来源

- https://docs.x.ai/grok-bot/
- https://github.com/KinGao294/grok-bot-orange-book
- 公开 X 文章（Alex Finn / Nate Herk / @ridark_eth / @zodchiii 等）
