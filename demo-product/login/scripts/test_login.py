def test_login(page):
    page.goto("https://example.com/login")
    page.get_by_label("账号").fill("demo")
    page.get_by_label("密码").fill("demo123")
    page.get_by_role("button", name="登录").click()
    assert page.get_by_text("首页").is_visible()
