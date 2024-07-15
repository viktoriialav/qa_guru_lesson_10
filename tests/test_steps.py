import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_dynamic_github():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        s('.search-input-container').click()
        s('#query-builder-test').send_keys('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем tab Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issue #88'):
        s(by.partial_text('#88')).should(be.visible)


def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('88')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.search-input-container').click()
    s('#query-builder-test').send_keys(repo)
    s('#query-builder-test').submit()


@allure.step('Переходи по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем tab Issues')
def open_issue_tab():
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issue с #{number}')
def should_see_issue_with_number(number):
    s(by.partial_text('#' + number)).should(be.visible)

