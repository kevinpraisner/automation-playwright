import pytest
from pytest_bdd import scenarios, given, when, then
from utils.data_factory import DataFactory

scenarios('../features/checkout.feature')

@given('que o usuário adicionou produtos ao carrinho de compras')
def adiciona_produtos(home_page):
    home_page.navigate_to_home()
    home_page.add_blue_top_to_cart()
    home_page.click_continue_shopping()

@when('ele prossegue para a tela de checkout')
def prossegue_checkout(cart_page):
    cart_page.navigate_to_cart()
    cart_page.proceed_to_checkout()
    cart_page.click_login_register_modal()

@when('realiza um novo cadastro com dados dinâmicos gerados em tempo de execução')
def realiza_cadastro(signup_page, cart_page, checkout_page):
    # Faker para gerar dados que nunca vão colidir com a API
    user_data = DataFactory.generate_user_data()
    
    signup_page.start_signup(user_data['name'], user_data['email'])
    signup_page.fill_account_info(user_data)
    signup_page.click_continue()
    
    # Após logar, o site volta pra home, voltar ao carrinho e conclui.
    cart_page.navigate_to_cart()
    cart_page.proceed_to_checkout()
    checkout_page.place_order()

@when('insere as informações de pagamento válidas')
def insere_pagamento(payment_page):
    payment_page.fill_payment_details("QA Tester", "4111222233334444", "123", "12", "2030")

@then('o pedido deve ser concluído com sucesso')
def pedido_concluido():
    pass # A validação real ocorre no próximo step

@then('o sistema deve exibir a tela de confirmação "Order Placed"')
def valida_order_placed(payment_page):
    msg = payment_page.get_success_message()
    assert msg == "ORDER PLACED!", f"Falha: Esperado 'ORDER PLACED!', recebido '{msg}'"

@then('a conta de teste deve ser excluída (Teardown) ao final do processo')
def exclui_conta(signup_page):
    signup_page.delete_account()