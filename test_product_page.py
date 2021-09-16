from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
import pytest



@pytest.mark.parametrize('p_link', [pytest.param(i, marks=pytest.mark.xfail(i==7, reason='Пойманный баг')) for i in range(10)])
def test_guest_can_add_product_to_basket(browser,p_link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{p_link}"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    page = BasePage(browser, link)
    page.solve_quiz_and_get_code()
    page.should_be_correct_adding_product_name()
    page.should_be_correct_adding_product_price()
    
