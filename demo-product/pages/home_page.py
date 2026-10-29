"""演示产品 - 首页 Page Object。"""

class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)
