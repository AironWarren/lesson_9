from allure_commons.types import Severity
from selene import browser, by, be
import allure


def test_github_dynamic_steps():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.MINOR)
    allure.dynamic.label('owner', 'AironWarren')
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Авторизированный пользователь может создать задачу в репозитории')
    allure.dynamic.link('https://github.com', name='Testing')

    with allure.step('Настраиваем размер страницы'):
        browser.config.window_width = 1800
        browser.config.window_height = 1800

    with allure.step('Открываем главную страницу GitHub'):
        browser.open("https://github.com")

    with allure.step('Находи репозиторий'):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").send_keys("AironWarren/lesson_9")
        browser.element(".header-search-input").submit()

    with allure.step('Переходим на репозиторий'):
        browser.element(by.link_text("AironWarren/lesson_9")).click()

    with allure.step('Переходим на вкладку issues'):
        browser.element("#issues-tab").click()
    with allure.step("Проверяем наличие Issue с номером 1"):
        browser.element(by.partial_text("#1")).should(be.visible)
