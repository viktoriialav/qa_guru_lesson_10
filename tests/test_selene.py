from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com/')

    s('.search-input-container').click()
    s('#query-builder-test').send_keys('eroshenkoam/allure-example')
    s('#query-builder-test').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#88')).should(be.visible)




