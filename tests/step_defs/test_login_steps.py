import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from utils.data_factory import DataFactory

# 1. Carrega os cenários do arquivo feature
scenarios('../features/login.feature')

# ==========================================
# GIVEN (DADO)
# ==========================================
@given("que o usuário está na tela de Autenticação")
def acessa_tela_login(login_page):
    login_page.navigate_to_login()

# ==========================================
# WHEN (QUANDO E E)
# ==========================================
@when(parsers.parse('ele insere o e-mail "{email}" e a senha "{password}"'))
def insere_credenciais(login_page, email, password):
    login_page.fill_element(login_page.email_input, email)
    login_page.fill_element(login_page.password_input, password)

@when("clica no botão de login")
def clica_login(login_page):
    login_page.click_element(login_page.login_button)

@when("ele tenta realizar o login com um e-mail aleatório e senha inválida")
def login_invalido_dinamico(login_page):
    user_data = DataFactory.generate_user_data()
    login_page.do_login(user_data["email"], user_data["password"])

# ==========================================
# THEN (ENTÃO E E)
# ==========================================
@then("ele deve ver que está logado no sistema")
def verifica_login_sucesso(login_page):
    # Aguarda ativamente o botão de logout aparecer na DOM (timeout de 10 segundos)
    try:
        login_page.page.locator("a[href='/logout']").wait_for(state="visible", timeout=10000)
    except Exception:
        pytest.fail("Botão de logout não encontrado no tempo limite. O login falhou!")

@then("o sistema deve bloquear o acesso")
def verifica_bloqueio(login_page):
    assert "login" in login_page.page.url

@then(parsers.parse('deve exibir a mensagem de erro: "{mensagem}"'))
def verifica_mensagem_erro(login_page, mensagem):
    erro_atual = login_page.get_login_error_message()
    assert erro_atual == mensagem, f"Esperava '{mensagem}', mas recebeu '{erro_atual}'"