# 🚀 Automação E2E: Python + Playwright + Azure DevOps

Este repositório contém um projeto avançado de automação de testes End-to-End (E2E) desenvolvido para o e-commerce [Automation Exercise](https://automationexercise.com/). O foco principal é demonstrar a aplicação de Engenharia de Qualidade utilizando ferramentas modernas, arquitetura escalável e esteiras de CI/CD corporativas.

## 🛠️ Stack Tecnológica e Arquitetura
* **Linguagem:** Python 3+
* **Framework de Teste:** Pytest (Runner, Fixtures e Asserts)
* **Automação Web:** Playwright (Alta performance e Auto-waiting)
* **Padrão de Projeto:** Page Object Model (POM) puro
* **Geração de Dados:** Faker (Massa de dados dinâmica)
* **CI/CD:** Azure Pipelines

---

## 📋 Sumário
1. [Parte 1: Estratégia, BDD e Testes Exploratórios](#parte-1-estratégia-bdd-e-testes-exploratórios)
2. [Parte 2: Automação e Engenharia de Código](#parte-2-automação-e-engenharia-de-código)
3. [Parte 3: Integração Contínua (Azure Pipelines)](#parte-3-integração-contínua-azure-pipelines)
4. [Parte 4: Bug Report (Padrão Azure Boards)](#parte-4-bug-report-padrão-azure-boards)

---

## Parte 1: Estratégia, BDD e Testes Exploratórios

A cobertura de testes foi desenhada para validar desde o "Caminho Feliz" (Happy Path) até a resiliência do sistema contra injeções de dados e manipulação de sessão.

### 📝 Cenários BDD (Gherkin)

```gherkin
Funcionalidade: Fluxo de Compra, Carrinho e Autenticação
  Como um cliente do e-commerce
  Quero gerenciar meus produtos e minha conta
  Para realizar compras de forma segura e fluida

  # Cenário 1: E2E Completo
  Cenário: Finalizar compra com usuário dinâmico gerado no checkout
    Dado que o usuário adicionou produtos ao carrinho de compras
    Quando ele prossegue para a tela de checkout
    E realiza um novo cadastro com dados dinâmicos gerados em tempo de execução
    E insere as informações de pagamento válidas
    Então o pedido deve ser concluído com sucesso
    E o sistema deve exibir a tela de confirmação "Order Placed"
    E a conta de teste deve ser excluída (Teardown) ao final do processo

  # Cenário 2: Regra de Negócio (Carrinho)
  Cenário: Remoção de produtos e validação de estado do carrinho
    Dado que o usuário adicionou o produto "Blue Top" ao carrinho
    E acessou a página de revisão do pedido
    Quando ele clica na ação de remover o item do carrinho
    Então o produto deve desaparecer instantaneamente da listagem do DOM
    E o sistema deve exibir a mensagem informando que o carrinho está vazio

  # Cenário 3: Segurança e Autenticação (Caminho Triste)
  Cenário: Tentativa de login com credenciais não cadastradas
    Dado que o usuário está na tela de Autenticação
    Quando ele tenta realizar o login com um e-mail aleatório e senha inválida
    Então o sistema deve bloquear o acesso
    E deve exibir a mensagem de erro: "Sua conta ou senha está incorreta!"