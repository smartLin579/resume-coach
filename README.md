# Resume Coach — 对话式简历优化 Skill

通过对话式聊天引导用户完成简历信息收集，自动优化措辞、量化成就、对齐JD关键词，最终生成精美PDF简历可直接上传BOSS直聘等招聘平台。

## 快速开始

对 Hermes Agent 说 **"帮我写简历"**，即可启动对话式简历优化流程。

## 特性

- 🎯 对话式引导：分5阶段聊天收集信息，每次只问2-3个问题
- 📄 智能简历生成：成就优先、加粗概括格式、岗位定制技能维度
- 🎯 JD动态调整：自动提取关键词、计算匹配度、输出匹配度报告
- 📋 ATS优化：BOSS直聘/猎聘友好格式
- 🎨 精美PDF导出：HTML→Playwright自动转换，无水印

## 安装

Hermes Agent 用户：skill 已在 `~/.hermes/skills/resume-coach/`，直接使用即可

手动安装：
```bash
git clone https://github.com/[your-username]/resume-coach.git ~/.hermes/skills/resume-coach
```

## 文件结构

```
resume-coach/
├── SKILL.md                      # 核心：对话流程 + 优化规则
├── templates/
│   └── resume-template.html      # HTML模板
└── scripts/
    ├── html_to_pdf.py            # PDF转换
    └── test_e2e.py               # 端到端测试
```

## 依赖

- Python 3.8+
- Playwright（PDF转换）
  ```bash
  pip install playwright && playwright install chromium
  ```

## 方法论来源

融合了以下开源项目：
- resume-builder-skill (41⭐) — 中文简历写作规则
- ResumeSkills (775⭐) — ATS优化、JD对齐
- Resume-Matcher (27k⭐) — ATS模拟

## 端到端测试

```bash
python ~/.hermes/skills/resume-coach/scripts/test_e2e.py
```

## License

MIT
