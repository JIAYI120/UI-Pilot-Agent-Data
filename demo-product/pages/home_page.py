"""演示产品 - 首页 Page Object。"""

class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def wait_ready(self):
        self.page.wait_for_load_state("networkidle")
