# features/environment.py
import os
from playwright.sync_api import sync_playwright
from utils.browser_manager import BrowserManager


def before_all(context):
    
    context.browser_manager = BrowserManager()

def before_scenario(context, scenario):
    
    context.page = context.browser_manager.launch_browser()

def after_scenario(context, scenario):
    
    if scenario.status == 'failed':
        # Capturar captura de pantalla en caso de fallo
        screenshot_dir = "reports/screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{scenario.name.replace(' ', '_')}_failed.png")
        context.page.screenshot(path=screenshot_path)
        print(f"Captura de pantalla tomada: {screenshot_path}")
        
        from allure_commons.types import AttachmentType
        import allure
        allure.attach.file(screenshot_path, name="Failure Screenshot", attachment_type=AttachmentType.PNG)
    context.browser_manager.close_browser()

def after_all(context):
    
    
    pass