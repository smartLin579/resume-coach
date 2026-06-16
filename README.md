# Resume Coach — 对话式简历优化 Skill

通过对话式聊天引导用户完成简历信息收集，自动优化措辞、量化成就、对齐JD关键词，最终生成精美PDF简历可直接上传BOSS直聘等招聘平台。

## 特性

- 🎯 对话式引导：分5阶段聊天收集信息，每次只问2-3个问题
- 📄 智能简历生成：成就优先、加粗概括格式、岗位定制技能维度
- 🎯 JD动态调整：自动提取关键词、计算匹配度、输出匹配度报告
- 📋 ATS优化：BOSS直聘/猎聘友好格式
- 🎨 精美PDF导出：HTML→Playwright自动转换，无水印

## 平台支持

| 平台 | 对话引导 | PDF自动导出 | 安装方式 |
|------|---------|------------|---------|
| **Hermes Agent** | ✅ 完整支持 | ✅ 完整支持 | `~/.hermes/skills/`（开箱即用） |
| **Claude Code** | ✅ 完整支持 | ⚠️ 需手动 | `npx skills add smartLin579/resume-coach` |
| **Codex** | ✅ 完整支持 | ⚠️ 需手动 | `npx skills add smartLin579/resume-coach` |
| **Cursor** | ✅ 完整支持 | ⚠️ 需手动 | 复制 `SKILL.md` 到 `.cursor/skills/` |
| **Windsurf** | ✅ 完整支持 | ⚠️ 需手动 | 类似 Cursor |
| **纯对话工具**（ChatGPT/Claude） | ⚠️ 需手动导入 prompt | ⚠️ 需手动 | 复制 SKILL.md 内容 |

> **⚠️ 重要说明**：PDF 导出需要 Python + Playwright。在 Claude Code/Codex/Cursor 等工具中，对话引导功能完全可用，但 PDF 需要手动执行转换脚本或浏览器打印。

## 安装

### Hermes Agent（推荐）

```bash
# skill 已在 ~/.hermes/skills/resume-coach/
# 直接说"帮我写简历"即可使用
```

### Claude Code / Codex / Cursor

```bash
# 方式1：一键安装（支持 npx skills 的工具）
npx skills add smartLin579/resume-coach

# 方式2：手动安装
git clone https://github.com/smartLin579/resume-coach.git
# Claude Code: 复制 SKILL.md 到 ~/.claude/skills/
# Codex: 复制 SKILL.md 到 ~/.codex/skills/
# Cursor: 复制 SKILL.md 到 .cursor/skills/
```

### 纯对话工具（ChatGPT/Claude）

复制 `SKILL.md` 的全部内容，作为对话开场词发送给 AI。

## 使用方法

### 在 Hermes Agent 中（完整功能）

```
你: 帮我写简历

我: 你好！你想投什么岗位？有具体的职位名称吗？

你: 我想投AI Coding方向...

# 对话结束后，自动生成 HTML + PDF 保存到桌面
```

### 在 Claude Code/Codex/Cursor 中（对话引导可用）

```
你: 帮我写简历

AI:（启动对话式信息收集）

# 信息收集完成后，AI 会输出 HTML 代码
# 你需要手动：
# 1. 把 HTML 保存为 .html 文件
# 2. 用浏览器打开 → Ctrl+P 打印为 PDF
# 或执行：python scripts/html_to_pdf.py resume.html resume.pdf
```

### 在 ChatGPT/Claude 对话中

复制 `SKILL.md` 全部内容，粘贴作为第一轮对话的开场词，然后回答 AI 的问题。对话结束后，复制 AI 生成的 HTML 代码保存为文件，再用浏览器打印为 PDF。

## 文件结构

```
resume-coach/
├── SKILL.md                      # 核心：对话流程 + 优化规则
├── templates/
│   └── resume-template.html      # HTML模板
├── scripts/
│   ├── html_to_pdf.py            # PDF转换（需Python）
│   └── test_e2e.py               # 端到端测试
├── examples/
│   ├── README.md
│   └── frontend-engineer-resume-example.pdf  # 示例输出
└── references/
    └── source-projects-and-methodologies.md
```

## 依赖（PDF转换功能）

**可选**：对话引导功能无需依赖。PDF转换需要：

- Python 3.8+
- Playwright

```bash
pip install playwright
playwright install chromium
```

### 不安装 Playwright 也能用

在 Claude Code/Codex/Cursor 中，AI 会生成 HTML 代码，你直接：
1. 保存为 `.html` 文件
2. 浏览器打开
3. Ctrl+P → 另存为 PDF

## 方法论来源

融合了以下开源项目：
- resume-builder-skill (41⭐) — 中文简历写作规则
- ResumeSkills (775⭐) — ATS优化、JD对齐
- Resume-Matcher (27k⭐) — ATS模拟

详见 `references/source-projects-and-methodologies.md`

## 端到端测试

```bash
# 测试 PDF 转换功能（需要 Python + Playwright）
python ~/.hermes/skills/resume-coach/scripts/test_e2e.py
```

## License

MIT

---

**由 [smartLin579](https://github.com/smartLin579) 开发，基于 Hermes Agent 技术栈**