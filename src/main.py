from models import Mensagem_Recebida
from flask import Flask, request, jsonify
from bot_logic import MechBot
import os
from dotenv import load_dotenv

#carregando as variáveis do arquivo .env
load_dotenv()
app = Flask(__name__)
bot = MechBot()

#rota para receber mensagens direto do wpp
@app.route('/webhook', methods=['POST'])
def webhook():
   dados_brutos = request.get_json()
   nova_msg = Mensagem_Recebida(dados_brutos)
   resposta_bot = bot.responder(nova_msg.telefone_cliente, nova_msg.msg_cliente)
   return jsonify({"status": "success", "reply": resposta_bot}), 200

#função apenas para verificar se o bot está funcionando
@app.route('/health', methods=['GET'])
def health_check():
    return "Bot funcionando!", 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

#rodando o servidor Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
