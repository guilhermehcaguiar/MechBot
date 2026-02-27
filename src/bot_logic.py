class MechBot:
    def __init__(self):
        self.sessoes = {}
    def responder(self, telefone, mensagem):
        texto= mensagem.strip().lower()
        if telefone not in self.sessoes:
            self.sessoes[telefone] = {"estado": "MENU"}
            return self.exibir_menu()
        estado_atual = self.sessoes[telefone]["estado"]
        if estado_atual == "MENU":
            if texto == "1":
                self.sessoes[telefone]["estado"] = "PERGUNTA_CADASTRO"
                return "Você já é cliente cadastrado na nossa oficina?\n1 - Sim\n2 - Não"
            elif texto == "2":
                self.sessoes[telefone]["estado"] = "CONSULTA_PLACA"
                return "Para acompanhar seu serviço, informe a placa do veículo."
            else:
                return "Opção inválida. Digite 1 ou 2."
        elif estado_atual == "PERGUNTA_CADASTRO":
            if texto in ["1", "sim", "s", "ss"]:
                self.sessoes[telefone]["estado"] = "AGUARDANDO_DADOS"
                return "Ótimo! Informe apenas seu CPF ou a Placa do veículo."
            elif texto in ["2", "não", "nao", "n"]:
                self.sessoes[telefone]["estado"] = "AGUARDANDO_DADOS"
                return "Seja bem-vindo! Informe: Nome, Telefone para contato, CPF, Placa e Endereço completo com CEP."
            else:
                return "Por favor, responda com 1 (Sim) ou 2 (Não)."
        elif estado_atual == "AGUARDANDO_DADOS":
            # Aqui limpamos a sessão para o próximo contato
            del self.sessoes[telefone] 
            return "Obrigado! Recebemos seus dados. Um consultor entrará em contato em breve."
        elif estado_atual == "CONSULTA_PLACA":
            placa = texto.upper()
            del self.sessoes[telefone] 
            return "Obrigado! Um consultor entrará em breve em contato para informar o status do veículo."
    def exibir_menu(self):
        return (
            "🔧 *Bem-Vindo à Oficina Atend-Car*\n"
            "Como posso ajudar hoje?\n"
            "1 - Orçamento\n"
            "2 - Status do Serviço"
        )
