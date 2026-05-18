from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://automationexercise.com/"
        
        # O produto "Blue Top" tem o data-product-id="1"
        self.add_to_cart_blue_top = "a[data-product-id='1'].add-to-cart"
        self.continue_shopping_btn = "button.btn-success.close-modal"
        
    def navigate_to_home(self):
        self.navigate(self.url)
        
    def add_blue_top_to_cart(self):
        # O site tem dois botões para o mesmo produto (um no hover). Usamos o .first para clicar no primeiro.
        self.page.locator(self.add_to_cart_blue_top).first.click()
        
    def click_continue_shopping(self):
        # Clica no botão verde de continuar comprando no modal que aparece
        self.click_element(self.continue_shopping_btn)