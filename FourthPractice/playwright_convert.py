import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        # Navigate to the HTML file
        html_path = f"file:///{os.path.abspath('FourthPractice.html').replace(chr(92), '/')}"
        await page.goto(html_path, wait_until="networkidle")
        
        # Save as PDF
        await page.pdf(path="FourthPractice.pdf", format="A4", print_background=True, 
                       margin={'top': '20px', 'right': '20px', 'bottom': '20px', 'left': '20px'})
        await browser.close()

asyncio.run(main())
