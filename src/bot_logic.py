import requests
import os
from datetime import datetime
class MechBot:
    def __init__(self):
        self.atendimento_ativo = {}
        self.url = f"https://graph.facebook.com/{os.getenv('VERSION')}/{os.getenv('PHONE_NUMBER_ID')}/messages"
        self.token = os.getenv('WHATSAPP_TOKEN')
    def is_horario_comercial(self):
        agora = datetime.now()
        dia_semana = agora.weekday()
        hora_decimal = agora.hour + agora.minute / 60
        if 0 <= dia_semana <= 4:
            return 8 <= hora_decimal < 17.5
        if dia_semana == 5:
            return 8 <= hora_decimal < 12
        return False
    def enviar_mensagem(self, telefone, texto):
        if not self.token:
            print(f"Sinal de {telefone}. Resposta: {texto}")
            return
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": telefone,
            "type": "text",
            "text": {"body": texto}
        }
        try:
            response = requests.post(self.url, headers=headers, json=payload)
            print(f"DEBUG API META: {response.status_code} - {response.text}") 
        except Exception as e:
            print(f"Erro na API: {e}")
    def responder(self, telefone, mensagem):
        texto = mensagem.strip().lower()
        if not self.is_horario_comercial():
            resposta = (
                "🌙 *Olá! No momento estamos fechados.*\n\n"
                "Nosso horário é:\n"
                "Seg a Sex: 08h às 17:30\n"
                "Sábado: 08h às 12h\n\n"
                "Deixe sua mensagem e retornaremos em breve! 🚗"
            )
            self.enviar_mensagem(telefone, resposta)
            return resposta

        if telefone not in self.atendimento_ativo:
            self.atendimento_ativo[telefone] = {"etapa": "MENU"}
            resposta = self.exibir_menu()
        else:
            etapa = self.atendimento_ativo[telefone]["etapa"]
            if etapa == "MENU":
                if texto == "1":
                    self.atendimento_ativo[telefone]["etapa"] = "PERGUNTA_CADASTRO"
                    resposta = "Você já é cliente cadastrado na nossa oficina?\n1 - Sim\n2 - Não"
                elif texto == "2":
                    self.atendimento_ativo[telefone]["etapa"] = "CONSULTA_PLACA"
                    resposta = "Para acompanhar seu serviço, informe a *PLACA* do veículo."
                elif texto == "3":
                    self.atendimento_ativo[telefone]["etapa"] = "ATENDENTE"
                    resposta = "👨‍💻 Entendido! Um consultor falará com você em breve."
                else:
                    resposta = "⚠️ Opção inválida. Digite 1, 2 ou 3."
            elif etapa == "PERGUNTA_CADASTRO":
                self.atendimento_ativo[telefone]["etapa"] = "AGUARDANDO_DADOS"
                if texto in ["1", "sim", "s"]:
                    resposta = "Ótimo! Por favor, informe seu *CPF* para localizarmos seu cadastro."
                else:
                    resposta = "Seja bem-vindo! Para iniciarmos, informe seu *NOME COMPLETO* e o *MODELO* do veículo."
            elif etapa == "AGUARDANDO_DADOS":
                del self.atendimento_ativo[telefone]
                resposta = "Obrigado! Recebemos suas informações. Um consultor entrará em contato para seguir com o orçamento. 📝"
            elif etapa == "CONSULTA_PLACA":
                del self.atendimento_ativo[telefone]
                resposta = f"Recebi a placa *{texto.upper()}*. Estamos verificando o status no sistema e te avisaremos em instantes! 🔍"
        self.enviar_mensagem(telefone, resposta)
        return resposta
    def exibir_menu(self):
        return (
            "🔧 *Oficina Atend-Car*\n"
            "Como podemos ajudar hoje?\n\n"
            "1 - Solicitar Orçamento\n"
            "2 - Ver Status do Serviço\n"
            "3 - Falar com Atendente"
        )