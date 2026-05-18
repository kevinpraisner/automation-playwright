from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://automationexercise.com/view_cart"
        
        self.delete_button = ".cart_quantity_delete"
        # O elemento "b" dentro do parágrafo é onde fica o texto de carrinho vazio
        self.empty_cart_message = "#empty_cart p.text-center b" 
        
    def navigate_to_cart(self):
        self.navigate(self.url)
        
    def remove_item(self):
        self.click_element(self.delete_button)

    def proceed_to_checkout(self):
        self.click_element(".check_out")
        
    def click_login_register_modal(self):
        self.click_element("u:has-text('Register / Login')")