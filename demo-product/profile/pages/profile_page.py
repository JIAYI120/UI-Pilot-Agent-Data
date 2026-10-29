"""演示产品 - 个人资料 Page Object。"""

class ProfilePage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.get_by_test_id("profile-entry").click()
