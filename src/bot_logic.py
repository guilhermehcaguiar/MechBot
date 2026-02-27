class MechBot:
    #dicionario armazena o estado atual do atendimento para cada telefone, permitindo que o bot se "lembre" do estado do cliente
    def __init__(self):
        self.atendimento_ativo = {}
    def responder(self, telefone, mensagem):
        texto= mensagem.strip().lower()

        #se o cliente não tiver um atendimento ativo, inicia um novo atendimento e exibimos o menu
        if telefone not in self.atendimento_ativo:
            self.atendimento_ativo[telefone] = {"etapa_atendimento": "MENU"}
            return self.exibir_menu()
        
        #se o cliente já tiver um atendimento ativo, verifica a etapa atual para direcionar a resposta
        estado_atual = self.atendimento_ativo[telefone]["etapa_atendimento"]
        if estado_atual == "MENU":
            if texto == "1":
                self.atendimento_ativo[telefone]["etapa_atendimento"] = "PERGUNTA_CADASTRO"
                return "Você já é cliente cadastrado na nossa oficina?\n1 - Sim\n2 - Não"
            elif texto == "2":
                self.atendimento_ativo[telefone]["etapa_atendimento"] = "CONSULTA_PLACA"
                return "Para acompanhar seu serviço, informe a placa do veículo."
            else:
                return "Opção inválida. Digite 1 ou 2."
        elif estado_atual == "PERGUNTA_CADASTRO":
            if texto in ["1", "sim", "s", "ss"]:
                self.atendimento_ativo[telefone]["etapa_atendimento"] = "AGUARDANDO_DADOS"
                return "Ótimo! Informe apenas seu CPF ou a Placa do veículo."
            elif texto in ["2", "não", "nao", "n"]:
                self.atendimento_ativo[telefone]["etapa_atendimento"] = "AGUARDANDO_DADOS"
                return "Seja bem-vindo! Informe: Nome, Telefone para contato, CPF, Placa e Endereço completo com CEP."
            else:
                return "Por favor, responda com 1 (Sim) ou 2 (Não)."
        elif estado_atual == "AGUARDANDO_DADOS":
            del self.atendimento_ativo[telefone] 
            return "Obrigado! Recebemos seus dados. Um consultor entrará em contato em breve."
        elif estado_atual == "CONSULTA_PLACA":
            placa = texto.upper()
            del self.atendimento_ativo[telefone] 
            return "Obrigado! Um consultor entrará em breve em contato para informar o status do veículo."
        #se o estado atual não for reconhecido, reseta o atendimento.

    def exibir_menu(self):
        return (
            "🔧 *Bem-Vindo à Oficina Atend-Car*\n"
            "Como posso ajudar hoje?\n"
            "1 - Orçamento\n"
            "2 - Status do Serviço"
        )
