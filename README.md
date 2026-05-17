# 🌐 API de Monitoramento de Cotações em Tempo Real

Este projeto consiste em um micro-serviço web e API RESTful desenvolvido em **Python** utilizando o framework **Flask**. O objetivo principal é realizar a integração com APIs financeiras externas para fornecer cotações atualizadas de moedas (Dólar, Euro e Bitcoin) em tempo real.

O projeto demonstra conceitos práticos de desenvolvimento backend, consumo de serviços web externos e disponibilização de dados estruturados em formato JSON.

## ⚙️ Tecnologias Utilizadas
* **Python 3.14**
* **Flask**: Criação e gerenciamento das rotas do servidor web.
* **Requests**: Consumo de API externa através do protocolo HTTP (verbo GET).

## 🚀 Como Executar o Projeto

1. Clone o repositório para a sua máquina:
   ```bash
   git clone [https://github.com/SEU-USUARIO/monitor-cotacoes-flask.git](https://github.com/SEU-USUARIO/monitor-cotacoes-flask.git)

2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt

3. Inicie o servidor de desenvolvimento:
   
python app_precos.py

4. Acesse as rotas diretamente no seu navegador:
* **Página Inicial**: http://127.0.0.1:5000/
* **Endpoint de Cotações**: http://127.0.0.1:5000/precos

## 🧠 Conceitos Praticados e Aprendidos
* **Arquitetura de APIs REST**: Integração de sistemas utilizando verbos HTTP.
* **Tratamento de Dados (JSON)**: Manipulação de dicionários complexos recebidos da web e serialização dos dados com a função jsonify().
* **Tratamento de Exceções**: Uso da estrutura try/except com o envio de códigos de status HTTP apropriados (200 OK para sucesso e 500 Internal Server Error para falhas), garantindo a resiliência do sistema caso o serviço de terceiros fique indisponível.
