# utils/browser_manager.py
from playwright.sync_api import sync_playwright

class BrowserManager:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None

    def launch_browser(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True) 
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        return self.page

    def close_browser(self):
        if self.page:
            self.page.close()
        if self.context:
            self.context.close()
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()