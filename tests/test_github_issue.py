from selene import browser, by, be


def test_github():
    browser.config.window_width = 1800
    browser.config.window_height = 1800
    browser.open("https://github.com")

    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys("AironWarren/lesson_2")
    browser.element(".header-search-input").submit()

    browser.element(by.link_text("AironWarren/lesson_2")).click()

    browser.element("#issues-tab").click()

    browser.element(by.partial_text("#76")).should(be.visible)
