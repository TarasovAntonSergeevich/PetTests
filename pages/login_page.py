from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        if "login" in url:
            assert True
        else:
            assert False, "Current url didn't contains 'login'"

    def should_be_login_form(self):
        errors = ""
        if not self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_LINK):
            errors += "Login email form is not presented; "
        if not self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_LINK):
            errors += "Login password form is not presented; "
        if not errors:
            assert True
        else:
            assert False, errors

    def should_be_register_form(self):
        errors = ""
        if not self.is_element_present(*LoginPageLocators.REG_EMAIL_LINK):
            errors += "Register email form is not presented; "
        if not self.is_element_present(*LoginPageLocators.REG_PASSWORD_LINK):
            errors += "Register password form is not presented; "
        if not self.is_element_present(*LoginPageLocators.REG_REPEAT_PASSWORD_LINK):
            errors += "Register repeat password form is not presented; "
        if not errors:
            assert True
        else:
            assert False, errors