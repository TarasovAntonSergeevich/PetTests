from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON_LINK), "Add button is not presented"


    def add_product_in_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON_LINK)
        button.click()
        self.solve_quiz_and_get_code()

        try:
            book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME)
            expected_name = self.browser.find_element(*ProductPageLocators.EXPECTED_NAME)
            book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE)
            basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        except NoSuchElementException:
            assert False, "Element didn't founded on page, check selectors"

        assert expected_name.text == book_name.text, f"Expected book name {expected_name}, in message {book_name}; "
        assert book_price.text == basket_price.text, "Basket price didn't equal book price; "


    def no_success_message_product_page(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success mesage on page, expected: not on page; "


    def success_message_dissapear_product_page(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "After 4 seconds message didn't dissapear"
