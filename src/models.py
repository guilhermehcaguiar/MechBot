class Mensagem_Recebida:
    def __init__(self, dados_json):
        self.msg_cliente = dados_json.get('message', '').strip()
        self.telefone_cliente = dados_json.get('from', 'desconhecido')
    def __repr__(self):
        return f"<Atendimento: {self.telefone_cliente} -> {self.msg_cliente[:20]}>"
