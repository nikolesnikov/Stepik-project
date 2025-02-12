from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By

class BasketPage(BasePage):
    def basket_dont_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM_BLOCK), "В корзине есть товары"
    def basket_should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Нет сообщения, что корзина пуста"
