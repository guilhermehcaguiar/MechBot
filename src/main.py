from models import Mensagem_Recebida
from flask import Flask, request, jsonify
from bot_logic import MechBot
import os
from dotenv import load_dotenv
#load_dotenv()
app = Flask(__name__)
bot = MechBot()
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if mode and token:
            if mode == 'subscribe' and token == os.getenv('VERIFY_TOKEN'):
                return challenge, 200
            else:
                return 'Forbidden', 403
    elif request.method == 'POST':
        dados_brutos = request.get_json()
        nova_msg = Mensagem_Recebida(dados_brutos)
        resposta_meta = bot.responder(nova_msg.telefone_cliente, nova_msg.msg_cliente)
        print(f"DEBUG: Resposta da Meta -> {resposta_meta}")
        return jsonify({"status": "success"}), 200
@app.route('/health', methods=['GET'])
def health_check():
    return "Bot funcionando!", 200
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
