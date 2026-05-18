from pages.base_page import BasePage

class SignupPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Seletores
        self.signup_name = "input[data-qa='signup-name']"
        self.signup_email = "input[data-qa='signup-email']"
        self.signup_button = "button[data-qa='signup-button']"
        self.password = "input[data-qa='password']"
        self.first_name = "input[data-qa='first_name']"
        self.last_name = "input[data-qa='last_name']"
        self.address1 = "input[data-qa='address']"
        self.state = "input[data-qa='state']"
        self.city = "input[data-qa='city']"
        self.zipcode = "input[data-qa='zipcode']"
        self.mobile_number = "input[data-qa='mobile_number']"
        self.create_account_btn = "button[data-qa='create-account']"
        self.continue_btn = "a[data-qa='continue-button']"
        self.delete_account_btn = "a[href='/delete_account']"

    def start_signup(self, name, email):
        self.fill_element(self.signup_name, name)
        self.fill_element(self.signup_email, email)
        self.click_element(self.signup_button)

    def fill_account_info(self, user_data):
        """Preenche o formulário usando o dicionário gerado pelo Faker"""
        self.fill_element(self.password, user_data['password'])
        self.fill_element(self.first_name, user_data['first_name'])
        self.fill_element(self.last_name, user_data['last_name'])
        self.fill_element(self.address1, user_data['address'])
        self.fill_element(self.state, user_data['state'])
        self.fill_element(self.city, user_data['city'])
        self.fill_element(self.zipcode, user_data['zipcode'])
        self.fill_element(self.mobile_number, user_data['mobile_number'])
        self.click_element(self.create_account_btn)

    def click_continue(self):
        self.click_element(self.continue_btn)

    def delete_account(self):
        """Teardown: Exclui a conta para limpar o banco e clica em continuar"""
        self.click_element(self.delete_account_btn)
        self.page.locator("h2[data-qa='account-deleted']").wait_for(state="visible")
        self.click_continue()