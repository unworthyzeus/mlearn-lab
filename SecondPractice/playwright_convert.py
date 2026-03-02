import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        html_path = f"file:///{os.path.abspath('SecondPracticeV2.html').replace(chr(92), '/')}"
        await page.goto(html_path)
        await page.pdf(path="SecondPracticeV2.pdf", format="A4", print_background=True)
        await browser.close()

asyncio.run(main())
