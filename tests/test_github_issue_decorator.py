from allure_commons.types import Severity
from selene import browser, by, be
import allure


@allure.tag('web')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'AironWarren')
@allure.feature('Задачи в репозитории')
@allure.story('Авторизированный пользователь может создать задачу в репозитории')
@allure.link('https://github.com', name='Testing')
def test_github_dynamic_steps():
    browser_config_window()
    open_main_page()
    looking_for_a_repository("AironWarren/lesson_9")
    opening_the_repository("AironWarren/lesson_9")
    issues()
    should_issue_1("#1")


@allure.step('Настраиваем размер страницы')
def browser_config_window():
    browser.config.window_width = 1800
    browser.config.window_height = 1800


@allure.step('Открываем главную страницу GitHub')
def open_main_page():
    browser.open("https://github.com")


@allure.step('Находи репозиторий {repo}')
def looking_for_a_repository(repo):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").send_keys(repo)
    browser.element(".header-search-input").submit()


@allure.step('Переходим на репозиторий {repo}')
def opening_the_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Переходим на вкладку issues')
def issues():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_issue_1(number):
    browser.element(by.partial_text(number)).should(be.visible)
