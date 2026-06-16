#!/usr/bin/env python3
"""
HTML → PDF 转换脚本
使用 Playwright（Chromium）将 HTML 简历渲染为 PDF
支持中文字体、CSS @page 设置、精确 A4 打印

用法:
    python html_to_pdf.py input.html output.pdf
"""

import sys
import os
from pathlib import Path


def convert_html_to_pdf(html_path: str, pdf_path: str) -> str:
    """将 HTML 文件转换为 PDF"""
    html_path = os.path.abspath(html_path)
    pdf_path = os.path.abspath(pdf_path)

    if not os.path.exists(html_path):
        print(f"错误: HTML 文件不存在: {html_path}", file=sys.stderr)
        sys.exit(1)

    # 确保 PDF 输出目录存在
    Path(pdf_path).parent.mkdir(parents=True, exist_ok=True)

    html_uri = Path(html_path).as_uri()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("错误: playwright 未安装。请运行: pip install playwright && playwright install chromium", file=sys.stderr)
        sys.exit(1)

    with sync_playwright() as p:
        # 启动 Chromium（headless）
        browser = p.chromium.launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-setuid-sandbox",
                "--disable-dev-shm-usage",
                "--font-render-hinting=none",
            ],
        )

        context = browser.new_context()
        page = context.new_page()

        # 加载 HTML 文件
        page.goto(html_uri, wait_until="networkidle")

        # 等待字体加载完成
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(500)  # 额外等待渲染稳定

        # 生成 PDF
        # A4: 210mm x 297mm
        # 使用 prefer_css_page_size 让 CSS @page 设置生效
        page.pdf(
            path=pdf_path,
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={
                "top": "0",
                "bottom": "0",
                "left": "0",
                "right": "0",
            },
        )

        browser.close()

    # 验证 PDF 生成成功
    if os.path.exists(pdf_path):
        size_kb = os.path.getsize(pdf_path) / 1024
        print(f"✅ PDF 生成成功: {pdf_path} ({size_kb:.1f} KB)")
        return pdf_path
    else:
        print(f"错误: PDF 生成失败", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("用法: python html_to_pdf.py <input.html> <output.pdf>")
        sys.exit(1)

    convert_html_to_pdf(sys.argv[1], sys.argv[2])
