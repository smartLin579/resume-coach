# Source Projects & Methodologies

本 skill 融合了以下 GitHub 开源项目的方法论。2026-06 调研时的 star 数据。

## 复用的方法论

### 1. Jichengyuuuuu/resume-builder-skill (⭐41)
**复用内容**：中文简历写作规则的核心框架
- 加粗概括 + 冒号格式（所有经历分点）
- 岗位定制技能维度表（11+ 岗位类型）
- 成就量化引导技巧
- 高阶顾问建议阶段（以高 1-2 级视角给 3-5 条建议）
- 页数控制策略（按工作年限）

**为什么复用**：这是 GitHub 上唯一的中文简历 Agent Skill，写作规则经过中文场景验证。

### 2. Paramchoudhary/ResumeSkills (⭐775)
**复用内容**：ATS 优化和 JD 对齐策略
- ATS 兼容性检查清单（文件格式、字体、区块标题、日期格式）
- 关键词提取方法（硬技能 / 软技能 / 文化匹配）
- Resume Tailor 的 Section-by-Section 调整策略
- Job Description Analyzer 的匹配度计算框架

**为什么复用**：20 个独立 Skill 集合，ATS 和 JD 分析逻辑最完整。

### 3. srbhr/Resume-Matcher (⭐27,374)
**参考但未直接复用**：FastEmbed 简历-JD 匹配度计算的思路
- 本 skill 用 LLM 推理代替向量匹配，更适合对话式场景

## 本 skill 相对于已有项目的增强

| 能力 | 已有项目 | resume-coach |
|------|---------|-------------|
| 对话式引导 | ❌ 都是一键/材料输入 | ✅ 5 阶段分步聊天 |
| 叙事主线（§4.0） | ❌ 未覆盖 | ✅ 根据目标方向重新框架所有经历 |
| PDF 导出 | ❌ 最多 HTML/DOCX | ✅ Playwright Chromium → PDF |
| 国内 ATS 适配 | ❌ 面向英文/LinkedIn | ✅ BOSS直聘/猎聘格式规范 |
| JD 无但有方向 | ❌ 只支持有 JD 的 tailoring | ✅ 方向驱动的叙事重构 |

## 环境依赖
- Python 3.x + Playwright（Chromium）已安装
- PDF 转换脚本：`scripts/html_to_pdf.py`
- 测试脚本：`scripts/test_e2e.py`

## 未来改进方向
- 支持 DOCX 格式输出（部分企业 ATS 只接受 Word）
- 增加英文简历模板（投外企/海外岗）
- 增加"多版本管理"——同一用户针对不同 JD 维护多个简历版本
- 探索 weasyprint 作为 Playwright 的备选（更轻量，但不支持部分 CSS）
