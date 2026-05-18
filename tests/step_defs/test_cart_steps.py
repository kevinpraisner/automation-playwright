import pytest
from pytest_bdd import scenarios, given, when, then
from playwright.sync_api import expect

# Carrega o cenário do carrinho
scenarios('../features/cart.feature')

@given('que o usuário adicionou o produto "Blue Top" ao carrinho')
def adiciona_blue_top(home_page):
    home_page.navigate_to_home()
    home_page.add_blue_top_to_cart()
    home_page.click_continue_shopping()

@given('acessou a página de revisão do pedido')
def acessa_carrinho(cart_page):
    cart_page.navigate_to_cart()

@when('ele clica na ação de remover o item do carrinho')
def remove_item(cart_page):
    cart_page.remove_item()

@then('o produto deve desaparecer instantaneamente da listagem do DOM')
def valida_remocao_dom(cart_page):
    expect(cart_page.page.locator("#product-1")).to_be_hidden(timeout=5000)

@then('o sistema deve exibir a mensagem informando que o carrinho está vazio')
def valida_mensagem_carrinho_vazio(cart_page):
    # Aguarda a mensagem aparecer e valida o texto
    cart_page.page.locator(cart_page.empty_cart_message).wait_for(state="visible", timeout=5000)
    mensagem = cart_page.get_text(cart_page.empty_cart_message)
    
    assert mensagem == "Cart is empty!", f"Mensagem esperada era 'Cart is empty!', mas veio '{mensagem}'"