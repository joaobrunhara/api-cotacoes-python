from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Rota principal da nossa API
@app.route('/precos', methods=['GET'])
def buscar_precos():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    
    try:
        # O Python vai na internet e faz a requisição no site de economia
        resposta = requests.get(url)
        dados = resposta.json()
        
        # Extraindo os valores comerciais atuais
        dolar = dados['USDBRL']['bid']
        euro = dados['EURBRL']['bid']
        bitcoin = dados['BTCBRL']['bid']
        
        # Criando o relatório estruturado que nossa API vai devolver
        relatorio = {
            "status": "sucesso",
            "moedas": {
                "Dolar": f"R$ {float(dolar):.2f}",
                "Euro": f"R$ {float(euro):.2f}",
                "Bitcoin": f"R$ {float(bitcoin):.2f}"
            },
            "mensagem": "Dados obtidos em tempo real da internet!"
        }
        return jsonify(relatorio), 200

    except Exception as e:
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

# Rota de boas-vindas do site
@app.route('/', methods=['GET'])
def home():
    return "<h1>🤖 Minha Primeira API Web está online!</h1><p>Acesse <b>/precos</b> para ver as cotações.</p>"

if __name__ == '__main__':
    # Roda o servidor web na sua máquina local
    app.run(debug=True)