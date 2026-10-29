"""演示产品 - 首页 Page Object。"""

class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def wait_ready(self):
        self.page.wait_for_load_state("networkidle")

    def is_logged_in(self) -> bool:
        return self.page.get_by_test_id("avatar").is_visible()

    def open_profile(self):
        self.page.get_by_test_id("avatar").click()
        self.page.get_by_role("menuitem", name="个人资料").click()
