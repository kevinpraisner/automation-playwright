# language: pt

@login
Funcionalidade: Autenticação de Usuário
  Como um cliente do e-commerce
  Quero acessar minha conta
  Para realizar compras de forma segura e fluida

  @happy_path
  Cenário: Login com credenciais válidas
    Dado que o usuário está na tela de Autenticação
    Quando ele insere o e-mail "teste_qa@automation.com" e a senha "123456"
    E clica no botão de login
    Então ele deve ver que está logado no sistema

  @edge_case
  Cenário: Tentativa de login com credenciais não cadastradas
    Dado que o usuário está na tela de Autenticação
    Quando ele tenta realizar o login com um e-mail aleatório e senha inválida
    Então o sistema deve bloquear o acesso
    E deve exibir a mensagem de erro: "Your email or password is incorrect!"