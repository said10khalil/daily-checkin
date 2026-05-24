from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://hr.jitex.be/admin/")
    page.wait_for_load_state("networkidle")
    
    page.locator("input[type='text']").first.fill(os.environ["EMAIL"])
    page.locator("input[type='password']").first.fill(os.environ["PASSWORD"])
    page.locator("button[type='submit']").click()
    
    page.wait_for_timeout(5000)
    
    # طباعة كل الأزرار الموجودة في الصفحة
    buttons = page.locator("button").all()
    for btn in buttons:
        print(f"زرار: {btn.inner_text()}")
    
    links = page.locator("a").all()
    for link in links:
        print(f"لينك: {link.inner_text()}")
    
    browser.close()
