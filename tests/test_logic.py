import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from bot_logic import MechBot
def iniciar_simulacao():
    bot = MechBot()
    id_teste = "12345"
    print("Teste MechBot Ativo")
    print("Digite 'EXIT' para sair")
    print("Bot: ", bot.responder(id_teste, ""))
    while True:
        comando = input("Você: ")
        
        if comando.lower() == "EXIT":
            break
            
        resposta = bot.responder(id_teste, comando)
        print(f"Bot: {resposta}\n")

if __name__ == "__main__":
    iniciar_simulacao()
