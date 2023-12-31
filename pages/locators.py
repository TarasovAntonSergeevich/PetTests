from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON_LINK = (By.CSS_SELECTOR, '[href="/ru/basket/"]')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_BUTTON_LINK = (By.CSS_SELECTOR, '[href="/ru/basket/"]')
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators():
    LOGIN_EMAIL_LINK = (By.CSS_SELECTOR, '[name="login-username"]')
    LOGIN_PASSWORD_LINK = (By.CSS_SELECTOR, '[name="login-password"]')
    REG_EMAIL_LINK = (By.CSS_SELECTOR, '[name="registration-email"]')
    REG_PASSWORD_LINK = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REG_REPEAT_PASSWORD_LINK = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[value="Register"]')

class ProductPageLocators():
    ADD_BUTTON_LINK = (By.CSS_SELECTOR, '[value="Добавить в корзину"]')
    BOOK_NAME = (By.CLASS_NAME, "alertinner > strong")
    EXPECTED_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BOOK_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")