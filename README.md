# 🚀 Automação E2E: Python + Playwright + Azure DevOps

Este repositório contém um framework de automação de testes End-to-End (E2E) e Unitários, desenvolvido para validar a qualidade da aplicação web [Automation Exercise](https://automationexercise.com/).

O projeto aplica as melhores práticas de Engenharia de Qualidade, utilizando o padrão **Page Object Model (POM)**, desenvolvimento guiado por comportamento (**BDD**) e integração contínua (**CI/CD**) com Azure DevOps.

---

## 📑 Sumário
1. [Stack Tecnológica](#-stack-tecnológica)
2. [Padrões e Arquitetura](#-padrões-e-arquitetura)
3. [Estrutura do Projeto](#-estrutura-do-projeto)
4. [Configuração do Ambiente Local](#-configuração-do-ambiente-local)
5. [Execução dos Testes](#-execução-dos-testes)
6. [Cenários em Gherkin](#-cenários-em-gherkin)
7. [Cobertura de Testes (Fluxos)](#-cobertura-de-testes-fluxos)
8. [Integração Contínua (Azure Pipelines)](#-integração-contínua-azure-pipelines)
9. [Bug Reports (Azure Boards)](#-bug-reports-azure-boards)

---

## 📐 Stack Tecnológica

| Camada | Tecnologia | Propósito |
| :--- | :--- | :--- |
| **Linguagem base** | Python 3 | Scripting ágil e tipagem dinâmica |
| **Motor de Automação** | Playwright (`pytest-playwright`) | Interação com o DOM, auto-waits nativos e cross-browser |
| **Executor de Testes** | Pytest | Orquestração da suíte de testes e fixtures |
| **Framework BDD** | `pytest-bdd` | Mapeamento de cenários em Gherkin nativo |
| **Massa de Dados** | Faker | Geração de dados dinâmicos em tempo de execução |
| **CI/CD** | Azure Pipelines | Automação da execução em nuvem |
| **Relatórios** | Pytest-HTML / Allure | Geração de evidências e métricas de execução |

---

## 💡 Padrões e Arquitetura

- **Page Object Model (POM):** Todo o mapeamento de elementos e ações de página estão isolados na camada `pages/`, separando a regra de negócio dos seletores técnicos e garantindo manutenibilidade a longo prazo.
- **Injeção de Dados via API:** Para evitar dependência de dados estáticos e otimizar o tempo de execução, utilizamos o `APIRequestContext` do Playwright no `conftest.py` para criar usuários diretamente via API em milissegundos antes do teste de UI iniciar — eliminando a fragilidade de formulários de cadastro como pré-condição.
- **Pirâmide de Testes:** Além dos testes End-to-End (E2E), o framework conta com **Testes Unitários** focados em validar a integridade das ferramentas internas, como o gerador de massa de dados dinâmicos (`DataFactory`).

---

## 🗂️ Estrutura do Projeto

```text
automation-playwright/
├── .azure/
│   └── azure-pipelines.yml        # Configuração da esteira CI/CD
├── pages/                         # Page Object Model (POM)
│   ├── base_page.py               # Funções genéricas reutilizáveis do Playwright
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── payment_page.py
│   └── signup_page.py
├── tests/
│   ├── features/                  # Cenários de teste escritos em Gherkin
│   │   ├── cart.feature
│   │   ├── checkout.feature
│   │   └── login.feature
│   ├── step_defs/                 # Mapeamento Gherkin → Python
│   │   ├── conftest.py            # Fixtures globais e injeção de usuário via API
│   │   ├── test_cart_steps.py
│   │   ├── test_checkout_steps.py
│   │   └── test_login_steps.py
│   └── unit_tests/                # Testes Unitários do Framework
│       └── test_data_factory.py
├── utils/
│   └── data_factory.py            # Geração de dados dinâmicos com Faker
├── .env.example                   # Modelo de variáveis de ambiente
├── pytest.ini                     # Configurações globais do executor
└── requirements.txt               # Dependências do projeto
```

---

## 🛠️ Configuração do Ambiente Local

### Pré-requisitos

- Python 3.10+
- Git

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/kevinpraisner/automation-playwright.git
cd automation-playwright
```

**2. Crie e ative o ambiente virtual:**
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
playwright install chromium
```

**4. Configure as variáveis de ambiente:**
```bash
# Copie o arquivo de exemplo e preencha com seus valores
cp .env.example .env
```

---

## 🚀 Execução dos Testes

O framework gera relatórios HTML e Allure automaticamente após qualquer execução.

### 1. Testes End-to-End (E2E)

**Modo Headless (padrão CI/CD — sem interface gráfica):**
```bash
pytest
```

**Modo Headed (navegador visível — ideal para debug local):**
```bash
pytest --headed
```

**Filtrar por funcionalidade via markers:**
```bash
pytest -m login
pytest -m cart
pytest -m checkout
pytest -m smoke          # apenas testes críticos
pytest -m "e2e and not edge_case"  # happy paths do E2E
```

### 2. Testes Unitários

Estes testes não abrem navegador. Validam em milissegundos se as classes utilitárias — como o `DataFactory` — estão gerando dicionários, e-mails e senhas nos formatos corretos exigidos pela aplicação.

```bash
pytest tests/unit_tests/ -v
```

### 3. Visualizar Relatório Allure

```bash
# Instalar o Allure CLI (necessário apenas uma vez)
npm install -g allure-commandline
# ou via Homebrew (Mac/Linux):
brew install allure

# Gerar e abrir o relatório no navegador após a execução dos testes
allure serve allure-results/
```

O relatório HTML alternativo é gerado automaticamente em `reports/report.html` e pode ser aberto diretamente no navegador sem instalação adicional.

---

## 📝 Cenários em Gherkin

Os cenários abaixo ilustram a abordagem BDD adotada no projeto, priorizando linguagem de negócio e valor do produto em detrimento de descrições técnicas de cliques.

### Fluxo de Autenticação (`login.feature`)

```gherkin
Funcionalidade: Autenticação de Usuário
  Como um cliente cadastrado
  Quero realizar login com minhas credenciais
  Para acessar minha conta e histórico de pedidos

  Cenário: Login com credenciais válidas
    Dado que o usuário possui uma conta ativa no sistema
    Quando ele informa e-mail e senha corretos na tela de login
    Então deve ser redirecionado para a página inicial autenticado
    E o menu deve exibir a opção "Logout"

  Cenário: Tentativa de login com e-mail não cadastrado
    Dado que o usuário acessa a página de login
    Quando ele informa um e-mail que não possui cadastro no sistema
    Então o sistema deve exibir a mensagem "Your email or password is incorrect!"
    E o usuário deve permanecer na página de login

  Cenário: Tentativa de login com senha incorreta
    Dado que o usuário acessa a página de login
    Quando ele informa um e-mail cadastrado com uma senha incorreta
    Então o sistema deve exibir a mensagem "Your email or password is incorrect!"
    E o usuário deve permanecer na página de login
```

### Fluxo de Carrinho (`cart.feature`)

```gherkin
Funcionalidade: Gestão do Carrinho de Compras
  Como um cliente navegando no e-commerce
  Quero gerenciar os produtos do meu carrinho
  Para controlar minha seleção antes de finalizar a compra

  Cenário: Adicionar produto ao carrinho e validar modal de confirmação
    Dado que o cliente está na página inicial da loja
    Quando ele adiciona um produto disponível ao carrinho
    Então o sistema deve exibir o modal de confirmação da adição
    E o ícone do carrinho deve refletir a quantidade atualizada

  Cenário: Remover produto do carrinho
    Dado que o cliente possui ao menos um produto no carrinho
    Quando ele remove o produto através do botão de exclusão
    Então o produto deve desaparecer da listagem do carrinho
    E o valor total deve ser recalculado corretamente

  Cenário: Tentar avançar para checkout com carrinho vazio
    Dado que o cliente não possui produtos no carrinho
    Quando ele tenta acessar diretamente a página de checkout
    Então o sistema deve impedir o avanço do fluxo
    E exibir uma mensagem informando que o carrinho está vazio
```

### Fluxo de Checkout (`checkout.feature`)

```gherkin
Funcionalidade: Checkout e Registro de Usuário Integrado
  Como um cliente do e-commerce
  Quero poder me registrar durante o processo de finalização de compra
  Para criar uma conta e concluir meu pedido em um fluxo unificado

  Cenário: Finalizar compra registrando novo usuário no checkout com sucesso
    Dado que o cliente adicionou produtos de interesse ao carrinho de compras
    Quando ele prossegue para a etapa de finalização da compra
    E opta por criar uma nova conta preenchendo seus dados cadastrais dinâmicos
    E confirma as informações de faturamento e endereço de entrega
    E insere dados válidos na etapa de pagamento
    Então o pedido deve ser processado e concluído com sucesso
    E o sistema deve exibir a confirmação "Congratulations! Your order has been confirmed!"
    E a nova conta do usuário deve constar como ativa e registrada no sistema

  Cenário: Acesso direto à página de pagamento sem autenticação ativa
    Dado que o usuário não possui sessão autenticada no sistema
    Quando ele tenta acessar diretamente a URL "/payment" pelo navegador
    Então o sistema deve bloquear o acesso à rota protegida
    E redirecionar o usuário para a página de login
```

---

## 🧪 Cobertura de Testes (Fluxos)

A automação cobre os 3 fluxos principais de conversão do e-commerce:

### Fluxo 1: Autenticação (`login.feature`)

#### Happy Path
- ✅ Login com credenciais válidas criadas dinamicamente via API

#### Edge Cases
- 🔴 Tentativa de login com e-mail não cadastrado no sistema
- 🔴 Tentativa de login com senha incorreta para e-mail válido

### Fluxo 2: Gestão de Carrinho (`cart.feature`)

#### Happy Path
- ✅ Adição de produtos e validação de modal de confirmação
- ✅ Remoção de produto com validação síncrona de exclusão no DOM

#### Edge Cases
- 🔴 Tentativa de avançar para checkout com carrinho vazio

### Fluxo 3: Checkout End-to-End (`checkout.feature`)

#### Happy Path
- ✅ Fluxo completo: Adicionar produto → Checkout → Cadastro dinâmico → Pagamento → Validação de "Order Placed" → Exclusão de conta (teardown automático)

#### Edge Cases
- 🔴 Acesso direto à página `/payment` sem sessão de usuário ativa (bypass de autenticação via URL)

---

## ☁️ Integração Contínua (Azure Pipelines)

O projeto possui integração nativa com o **Azure DevOps**. O arquivo `.azure/azure-pipelines.yml` provisiona uma máquina virtual Linux (`ubuntu-latest`) que executa automaticamente as seguintes etapas:

1. Instala a versão correta do Python
2. Baixa as dependências e os binários do Chromium
3. Executa toda a suíte de testes (E2E e Unitários)
4. Publica o artefato `report.html` diretamente na interface do Azure para análise do time de QA

A pipeline é acionada automaticamente a cada **Push** ou **Pull Request** direcionado à branch `main`.

---

## 🐛 Bug Reports (Azure Boards)

Durante o mapeamento exploratório e a construção dos scripts foram identificados 3 bugs na aplicação. Os Work Items abaixo seguem o padrão do **Azure Boards** para abertura de tickets formais.

---

### 🐛 Bug 1: Subscription Footer aceita e-mail inválido

| Campo | Detalhe |
| :--- | :--- |
| **Work Item Type** | Bug |
| **Título** | [Frontend / Footer] - Campo de subscription aceita string sem formato de e-mail válido |
| **State** | New |
| **Severity** | 3 - Medium |
| **Priority** | 2 |
| **Area Path** | `AutomationExercise\Frontend\Footer` |
| **System Info** | Google Chrome 125.0 / Windows 11 |
| **Reportado por** | Kevin (QA Analyst) |

**Passos para Reproduzir:**
1. Acessar `https://automationexercise.com/`
2. Rolar até o rodapé da página (seção *Subscription*)
3. Inserir o texto `teste_sem_arroba` no campo de e-mail
4. Clicar na seta de submit

**Resultado Esperado:**
O sistema deve bloquear o envio e exibir um aviso de validação (HTML5 nativo ou mensagem customizada) informando que o formato de e-mail é inválido.

**Resultado Atual:**
O sistema aceita qualquer string e exibe a mensagem de sucesso *"You have been successfully subscribed!"*, sem nenhuma validação de formato no front-end ou back-end.

**Critério de Aceitação:**
O bug estará resolvido quando o campo rejeitar strings sem o padrão `*@*.*` e exibir feedback de erro ao usuário antes do envio.


---

### 🐛 Bug 2: Campo Quantity aceita valor zero e negativo

| Campo | Detalhe |
| :--- | :--- |
| **Work Item Type** | Bug |
| **Título** | [Frontend / Product Detail] - Input de quantidade aceita valores 0 e negativos sem validação |
| **State** | New |
| **Severity** | 2 - High |
| **Priority** | 1 |
| **Area Path** | `AutomationExercise\Frontend\Product` |
| **System Info** | Google Chrome 125.0 / Windows 11 |
| **Reportado por** | Kevin (QA Analyst) |

**Passos para Reproduzir:**
1. Acessar a página de detalhes de qualquer produto (ex: `/product_details/1`)
2. Localizar o campo *Quantity*
3. Limpar o campo e inserir o valor `0` ou `-5`
4. Clicar em *Add to Cart*

**Resultado Esperado:**
O botão *Add to Cart* deve ser desabilitado para valores menores que 1, ou o sistema deve exibir uma mensagem de erro informando que a quantidade mínima permitida é 1.

**Resultado Atual:**
O produto é adicionado ao carrinho com a quantidade zerada ou negativa, quebrando o cálculo de totais e permitindo um estado inválido de pedido no sistema.

**Critério de Aceitação:**
O bug estará resolvido quando o campo `quantity` rejeitar qualquer valor menor que 1 com feedback visual ao usuário, impedindo a adição ao carrinho neste estado.


---

### 🐛 Bug 3: Página `/payment` acessível sem autenticação

| Campo | Detalhe |
| :--- | :--- |
| **Work Item Type** | Bug |
| **Título** | [Segurança / Routing] - Rota /payment acessível via URL direta sem sessão de usuário ativa |
| **State** | New |
| **Severity** | 1 - Critical |
| **Priority** | 1 |
| **Area Path** | `AutomationExercise\Backend\Auth` |
| **System Info** | Google Chrome 125.0 / Windows 11 |
| **Reportado por** | Kevin (QA Analyst) |

**Passos para Reproduzir:**
1. Abrir uma janela anônima (sem sessão autenticada)
2. Digitar diretamente `https://automationexercise.com/payment` na barra de endereços
3. Pressionar Enter

**Resultado Esperado:**
O sistema deve validar o token de sessão no back-end, bloquear o acesso à rota protegida e redirecionar o usuário imediatamente para `/login`.

**Resultado Atual:**
A página de pagamento com o formulário completo de cartão de crédito é renderizada normalmente para visitantes anônimos, expondo a interface de pagamento sem qualquer controle de autenticação.

**Critério de Aceitação:**
O bug estará resolvido quando qualquer tentativa de acesso direto à rota `/payment` sem sessão válida resultar em redirecionamento automático para `/login`, validado tanto no front-end (guard de rota) quanto no back-end (verificação de token).
