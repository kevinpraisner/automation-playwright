# language: pt

@cart
Funcionalidade: Gerenciamento do Carrinho de Compras
  Como um cliente do e-commerce
  Quero gerenciar os itens no meu carrinho
  Para ter controle sobre o que vou comprar

  @edge_case
  Cenário: Remoção de produtos e validação de estado do carrinho
    Dado que o usuário adicionou o produto "Blue Top" ao carrinho
    E acessou a página de revisão do pedido
    Quando ele clica na ação de remover o item do carrinho
    Então o produto deve desaparecer instantaneamente da listagem do DOM
    E o sistema deve exibir a mensagem informando que o carrinho está vazio