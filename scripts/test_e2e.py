#!/usr/bin/env python3
"""
端到端测试：用虚拟人物数据，生成真实 HTML + PDF 简历
验证 resume-coach skill 的完整生成流程
"""
import os
import sys
from pathlib import Path

# 测试数据：5年前端工程师
RESUME_HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>李明_前端工程师_简历</title>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
@page { size: A4; margin: 14mm 16mm; }
html { font-size: 14px; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: -apple-system, "Microsoft YaHei", "PingFang SC", "Helvetica Neue", sans-serif; color: #333333; line-height: 1.6; background: #f0f0f0; }
.resume { max-width: 780px; margin: 0 auto; background: #FFFFFF; padding: 40px 48px; }
.resume-header { text-align: center; margin-bottom: 20px; padding-bottom: 16px; border-bottom: 2px solid #1a5276; }
.resume-header h1 { font-size: 26px; font-weight: 700; color: #1a5276; letter-spacing: 4px; margin-bottom: 8px; }
.resume-header .subtitle { font-size: 15px; color: #555; margin-bottom: 6px; font-weight: 500; }
.resume-header .contact { font-size: 13px; color: #777; }
.resume-header .contact span { margin: 0 6px; }
.resume-header .contact .sep { color: #ccc; }
.resume-summary { margin-bottom: 18px; padding: 12px 16px; background: #f8f9fa; border-left: 3px solid #1a5276; border-radius: 0 4px 4px 0; }
.resume-summary p { font-size: 13.5px; color: #555; line-height: 1.7; }
.resume-section { margin-bottom: 18px; }
.resume-section h2 { font-size: 16px; font-weight: 700; color: #1a5276; margin-bottom: 10px; padding-bottom: 5px; border-bottom: 1px solid #e0e0e0; letter-spacing: 1px; }
.skills-grid { display: flex; flex-wrap: wrap; gap: 6px 0; }
.skill-line { width: 100%; font-size: 13px; line-height: 1.8; }
.skill-line .skill-label { font-weight: 600; color: #1a5276; margin-right: 4px; }
.experience-item { margin-bottom: 14px; }
.experience-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 4px; }
.experience-header .company { font-size: 14.5px; font-weight: 700; color: #333; }
.experience-header .company .role { font-weight: 500; color: #555; margin-left: 8px; }
.experience-header .date { font-size: 12.5px; color: #888; white-space: nowrap; }
.experience-list { list-style: none; padding-left: 0; }
.experience-list li { font-size: 13px; color: #555; line-height: 1.7; padding-left: 14px; position: relative; margin-bottom: 3px; }
.experience-list li::before { content: "•"; position: absolute; left: 0; top: 0; color: #1a5276; font-weight: bold; }
.experience-list li strong { color: #333; font-weight: 600; }
.project-item { margin-bottom: 12px; }
.project-header { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 3px; }
.project-header .project-name { font-size: 13.5px; font-weight: 600; color: #444; }
.project-header .project-role { font-size: 12.5px; color: #888; }
.education-item { display: flex; justify-content: space-between; align-items: baseline; }
.education-item .school { font-size: 14px; font-weight: 600; color: #333; }
.education-item .degree { font-size: 13px; color: #666; }
.education-item .date { font-size: 12.5px; color: #888; white-space: nowrap; }
@media print {
  body { background: #FFFFFF; font-size: 12pt; }
  .resume { max-width: 100%; margin: 0; padding: 0; box-shadow: none; }
  .resume-section, .experience-item { page-break-inside: avoid; }
  a { color: #333; text-decoration: none; }
}
</style>
</head>
<body>
<div class="resume">
  <header class="resume-header">
    <h1>李明</h1>
    <div class="subtitle">高级前端工程师</div>
    <div class="contact">
      <span>上海</span><span class="sep">|</span>
      <span>139-1234-5678</span><span class="sep">|</span>
      <span>liming@email.com</span><span class="sep">|</span>
      <span>github.com/liming-dev</span>
    </div>
  </header>

  <div class="resume-summary">
    <p>5 年前端开发经验，专注 React 生态和工程化体系建设。主导搭建企业级组件库和微前端架构，覆盖 200+ 页面、30+ 业务线。擅长性能优化，曾将首屏加载时间从 4.2s 降至 1.1s。</p>
  </div>

  <section class="resume-section">
    <h2>专业技能</h2>
    <div class="skills-grid">
      <div class="skill-line"><span class="skill-label">编程语言：</span>TypeScript / JavaScript / HTML5 / CSS3 / Node.js</div>
      <div class="skill-line"><span class="skill-label">框架：</span>React / React Native / Vue 3 / Next.js</div>
      <div class="skill-line"><span class="skill-label">工程化：</span>Webpack / Vite / Turborepo / Monorepo / CI/CD</div>
      <div class="skill-line"><span class="skill-label">性能优化：</span>首屏优化 / 懒加载 / Tree-shaking / Service Worker / Web Vitals</div>
      <div class="skill-line"><span class="skill-label">可视化：</span>D3.js / ECharts / Three.js / Canvas / WebGL</div>
    </div>
  </section>

  <section class="resume-section">
    <h2>工作经历</h2>
    <div class="experience-item">
      <div class="experience-header">
        <div class="company">字节跳动 <span class="role">— 高级前端工程师</span></div>
        <div class="date">2022.03 - 至今</div>
      </div>
      <ul class="experience-list">
        <li><strong>微前端架构：</strong>主导设计基于 Module Federation 的微前端架构，整合 8 个子应用，首屏加载从 4.2s 降至 1.1s，覆盖日活 500 万+ 用户</li>
        <li><strong>组件库建设：</strong>从 0 搭建企业级 React 组件库（60+ 组件），被 30+ 业务线采用，减少重复代码 40%</li>
        <li><strong>性能监控：</strong>搭建前端性能监控平台（Web Vitals 采集），覆盖 200+ 页面，首屏合格率从 62% 提升至 95%</li>
      </ul>
    </div>
    <div class="experience-item">
      <div class="experience-header">
        <div class="company">美团 <span class="role">— 前端开发工程师</span></div>
        <div class="date">2020.07 - 2022.02</div>
      </div>
      <ul class="experience-list">
        <li><strong>数据可视化：</strong>开发基于 ECharts 的实时数据大屏系统，支持 50+ 维度数据展示，服务运营团队日常决策</li>
        <li><strong>工程优化：</strong>将 Webpack 构建从 V4 升级到 V5，构建速度提升 60%，产物体积减少 35%</li>
      </ul>
    </div>
  </section>

  <section class="resume-section">
    <h2>项目经验</h2>
    <div class="project-item">
      <div class="project-header">
        <div class="project-name">企业级微前端架构升级</div>
        <div class="project-role">前端架构负责人</div>
      </div>
      <ul class="experience-list">
        <li><strong>背景：</strong>原有单体应用 80 万行代码，构建 25 分钟，多团队协作冲突严重</li>
        <li><strong>方案：</strong>采用 Module Federation + Turborepo 拆分为 8 个微应用，统一设计 token 和组件库</li>
        <li><strong>成果：</strong>构建时间降至 3 分钟，首屏 LCP 从 4.2s 降至 1.1s，团队迭代效率提升 50%</li>
      </ul>
    </div>
  </section>

  <section class="resume-section">
    <h2>教育背景</h2>
    <div class="education-item">
      <div>
        <span class="school">华东理工大学</span>
        <span class="degree">— 软件工程 · 本科</span>
      </div>
      <div class="date">2016.09 - 2020.06</div>
    </div>
  </section>
</div>
</body>
</html>"""


def main():
    # 1. 生成 HTML
    desktop = Path(os.path.expanduser("~/Desktop"))
    html_path = desktop / "李明_前端工程师_简历.html"
    pdf_path = desktop / "李明_前端工程师_简历.pdf"

    html_path.write_text(RESUME_HTML, encoding="utf-8")
    print(f"✅ HTML 已生成: {html_path} ({len(RESUME_HTML)} chars)")

    # 2. 转换 PDF
    script_path = os.path.expanduser("~/.hermes/skills/resume-coach/scripts/html_to_pdf.py")
    venv_python = r"C:\Users\Administrator\AppData\Local\hermes\hermes-agent\.venv\Scripts\python.exe"

    import subprocess
    result = subprocess.run(
        [venv_python, script_path, str(html_path), str(pdf_path)],
        capture_output=True, text=True, timeout=30
    )

    if result.returncode == 0:
        print(result.stdout.strip())
    else:
        print(f"❌ PDF 转换失败: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    # 3. 验证文件
    html_size = html_path.stat().st_size / 1024
    pdf_size = pdf_path.stat().st_size / 1024
    print(f"\n📊 文件验证:")
    print(f"   HTML: {html_path.name} ({html_size:.1f} KB)")
    print(f"   PDF:  {pdf_path.name} ({pdf_size:.1f} KB)")
    print(f"\n✅ 端到端测试通过！HTML + PDF 全链路正常。")


if __name__ == "__main__":
    main()
