from .pages.login_page import LoginPage

"""pytest -v --tb=line --language=en test_login_page.py
"""


def test_guest_can_see_login_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()


def test_login_page_contains_login_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_form()


def test_login_page_contains_register_form(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_login_form()
