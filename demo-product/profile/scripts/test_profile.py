def test_profile_nickname(page):
    page.get_by_label("昵称").fill("演示用户")
    page.get_by_role("button", name="保存").click()
    assert page.get_by_text("保存成功").is_visible()
