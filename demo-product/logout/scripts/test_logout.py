def test_logout(page):
    page.get_by_role("button", name="退出登录").click()
    assert page.get_by_text("登录").is_visible()
