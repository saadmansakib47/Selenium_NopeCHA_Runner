from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BrowserManager:
    def __init__(self, proxy=None, headless=True):
        self.proxy = proxy
        self.headless = headless
        self.driver = self._init_driver()

    def _init_driver(self):
        options = Options()
        if self.headless:
            options.add_argument("--headless=new")
        if self.proxy:
            options.add_argument(f'--proxy-server=http://{self.proxy["ip"]}:{self.proxy["port"]}')
        return webdriver.Chrome(options=options)

    def quit(self):
        self.driver.quit()
