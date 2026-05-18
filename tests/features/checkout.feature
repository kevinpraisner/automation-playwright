# language: pt

@checkout @e2e
Funcionalidade: Finalização de Compra (Checkout)
  Como um cliente do e-commerce
  Quero gerenciar meus produtos e minha conta
  Para realizar compras de forma segura e fluida

  @happy_path
  Cenário: Finalizar compra com usuário dinâmico gerado no checkout
    Dado que o usuário adicionou produtos ao carrinho de compras
    Quando ele prossegue para a tela de checkout
    E realiza um novo cadastro com dados dinâmicos gerados em tempo de execução
    E insere as informações de pagamento válidas
    Então o pedido deve ser concluído com sucesso
    E o sistema deve exibir a tela de confirmação "Order Placed"
    E a conta de teste deve ser excluída (Teardown) ao final do processo