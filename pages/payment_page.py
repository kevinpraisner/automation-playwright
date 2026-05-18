from pages.base_page import BasePage

class PaymentPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.name_on_card = "input[data-qa='name-on-card']"
        self.card_number = "input[data-qa='card-number']"
        self.cvc = "input[data-qa='cvc']"
        self.expiry_month = "input[data-qa='expiry-month']"
        self.expiry_year = "input[data-qa='expiry-year']"
        self.pay_button = "button[data-qa='pay-button']"
        self.success_message = "[data-qa='order-placed'] > b"

    def fill_payment_details(self, name, card, cvc, month, year):
        self.fill_element(self.name_on_card, name)
        self.fill_element(self.card_number, card)
        self.fill_element(self.cvc, cvc)
        self.fill_element(self.expiry_month, month)
        self.fill_element(self.expiry_year, year)
        self.click_element(self.pay_button)

    def get_success_message(self):
        self.page.locator(self.success_message).wait_for(state="visible", timeout=10000)
        return self.get_text(self.success_message)