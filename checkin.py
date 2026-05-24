from playwright.sync_api import sync_playwright
import os

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://hr.jitex.be/admin/")
    page.fill("[name='username']", os.environ["EMAIL"])
    page.fill("[name='password']", os.environ["PASSWORD"])
    page.click("button[type='submit']")
    page.wait_for_timeout(3000)
    page.click("text=Check In")
    print("✅ تم!")
    browser.close()
