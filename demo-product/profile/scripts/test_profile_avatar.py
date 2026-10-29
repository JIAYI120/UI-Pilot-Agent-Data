def test_profile_avatar(page):
    page.get_by_label("上传头像").set_input_files("avatar.png")
    assert page.get_by_text("上传成功").is_visible()
