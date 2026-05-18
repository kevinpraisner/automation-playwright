from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url = "https://automationexercise.com/login"
        
        # Seletores (Mapeamento dos elementos na tela)
        self.email_input = "input[data-qa='login-email']"
        self.password_input = "input[data-qa='login-password']"
        self.login_button = "button[data-qa='login-button']"
        self.error_message_label = ".login-form form p" # Seletor da mensagem de erro de login
        
    def navigate_to_login(self):
        """Acessa a página de login diretamente"""
        self.navigate(self.url)

    def do_login(self, email, password):
        """Preenche as credenciais e clica em login"""
        self.fill_element(self.email_input, email)
        self.fill_element(self.password_input, password)
        self.click_element(self.login_button)

    def get_login_error_message(self):
        """Retorna o texto da mensagem de erro"""
        # Espera o elemento ficar visível antes de pegar o texto
        self.page.locator(self.error_message_label).wait_for(state="visible")
        return self.get_text(self.error_message_label)