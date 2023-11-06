from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current url didn't contain 'login'"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_LINK), "Login email form is not presented; "
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_LINK), "Login password form is not presented; "

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_LINK), "Register email form is not presented; "
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_LINK), "Register password form is not presented; "
        assert self.is_element_present(*LoginPageLocators.REG_REPEAT_PASSWORD_LINK), "Register repeat password form is not presented; "
