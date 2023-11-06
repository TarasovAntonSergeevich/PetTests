from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_basket_button(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_BUTTON_LINK), "Basket button not presented"

    def basket_should_be_empty(self):
        assert "Ваша корзина пуста" in self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text, "Basket is not empty"