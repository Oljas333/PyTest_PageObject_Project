from selenium.webdriver.common.by import By


class MainPageLocators:
    # LOGIN_LINK = (By.CSS_SELECTOR, '#registration_link')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_USERNAME_INPUT = (By.CSS_SELECTOR, 'input#id_login-username')
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#id_login-password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, 'input#id_registration-email')
    REGISTRATION_PASSWORD_INPUT1 = (By.CSS_SELECTOR, 'input#id_registration-password1')
    REGISTRATION_PASSWORD_INPUT2 = (By.CSS_SELECTOR, 'input#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    PRODUCT_COST_LABEL = (By.CSS_SELECTOR, 'p[class="price_color"]')
    PRODUCT_NAME_LABEL = (By.CSS_SELECTOR, 'div[class*="product_main"]>h1')
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, 'button[class*="btn-add-to-basket"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div[class*="alert-success"]')
    PRODUCT_NAME_IN_MESSAGE_SUCCSESS = (By.CSS_SELECTOR, f'{SUCCESS_MESSAGE[1]}>div[class^="alertinner"]>strong')
    PRICE_IN_MESSAGE_CHANGE_COST = (By.CSS_SELECTOR, 'div[class*="alert-info"]>div[class^="alertinner"] strong')


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group>a[href*="basket"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class CartPageLocators(object):
    LIST_PRODUCTS = (By.CSS_SELECTOR, 'form#basket_formset')
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
