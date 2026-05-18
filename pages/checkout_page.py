from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.comment_input = "textarea[name='message']"
        self.place_order_btn = "a[href='/payment']"

    def place_order(self, comment="Pedido E2E automatizado pelo Playwright"):
        self.fill_element(self.comment_input, comment)
        self.click_element(self.place_order_btn)