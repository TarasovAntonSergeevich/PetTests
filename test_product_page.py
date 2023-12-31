import pytest
import time
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

links =["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


def test_guest_can_add_see_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_button()


@pytest.mark.parametrize('link', links)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()


@pytest.mark.parametrize('link', links)
@pytest.mark.xfail(reason="Message is contains always, this test just for fun :D")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.no_success_message_product_page()


@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.no_success_message_product_page()


@pytest.mark.parametrize('link', links)
@pytest.mark.xfail(reason="Message didnt disappear and never dissapeared")
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_basket()
    page.success_message_dissapear_product_page()

@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.parametrize('link', links)
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.parametrize('link', links)
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    new_page = BasketPage(browser, browser.current_url)
    new_page.basket_should_be_empty()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    @pytest.mark.parametrize('link', links)
    def setup(self, browser, link):
        email = str(time.time()) + "@fakemail.org"
        password = "fakepassword"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.parametrize('link', links)
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.add_product_in_basket()

    @pytest.mark.parametrize('link', links)
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.no_success_message_product_page()
