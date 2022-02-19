import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='en',
                     help='Choose language: any')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption("language")
    browser = None
    if browser_name in ('chrome', 'c'):
        print('\nstart chrome browser for test..')
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name in ('firefox', 'f'):
        print('\nstart firefox browser for test..')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        print('Browser {} still is not implemented'.format(browser_name))
    yield browser
    print('\nquit browser..')
    browser.quit()
