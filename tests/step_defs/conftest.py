import pytest
from pages.signup_page import SignupPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage
from playwright.sync_api import Page, Playwright
from pages.login_page import LoginPage
from pages.home_page import HomePage   # NOVO
from pages.cart_page import CartPage   # NOVO

@pytest.fixture(autouse=True)
def prepara_massa_de_dados(playwright: Playwright):
    api_context = playwright.request.new_context()
    payload = {
        "name": "QA Automator", "email": "teste_qa@automation.com", "password": "123456",
        "title": "Mr", "birth_date": "1", "birth_month": "January", "birth_year": "2000",
        "firstname": "QA", "lastname": "Automator", "company": "Tech",
        "address1": "Rua dos Testes, 123", "country": "United States", "zipcode": "10001",
        "state": "New York", "city": "New York", "mobile_number": "11999999999"
    }
    response = api_context.post("https://automationexercise.com/api/createAccount", form=payload)
    print(f"\n[API SETUP] Resposta do Servidor: {response.text()}")
    api_context.dispose()

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture
def home_page(page: Page):
    return HomePage(page)

@pytest.fixture
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture
def signup_page(page: Page):
    return SignupPage(page)

@pytest.fixture
def checkout_page(page: Page):
    return CheckoutPage(page)

@pytest.fixture
def payment_page(page: Page):
    return PaymentPage(page)