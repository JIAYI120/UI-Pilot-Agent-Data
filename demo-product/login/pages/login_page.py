"""演示产品 - 登录页 Page Object。"""

class LoginPage:
    def __init__(self, page):
        self.page = page

    def login(self, user: str, password: str):
        self.page.get_by_label("账号").fill(user)
        self.page.get_by_label("密码").fill(password)
        self.page.get_by_role("button", name="登录").click()
