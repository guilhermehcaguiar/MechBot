# 🔧 MechBot - Solução Inteligente para Gestão de Oficinas

O **MechBot** é um ecossistema de atendimento automatizado via WhatsApp (Meta API), projetado para transformar a recepção de oficinas mecânicas em uma operação 24/7 de alta eficiência. Desenvolvido com **Python 3.14.3**, ele elimina gargalos de atendimento e organiza o fluxo de entrada de serviços de forma profissional.

## 🌟 Funcionalidades de Alto Valor
* **Triagem Automatizada**: Menu inteligente que segmenta clientes entre orçamentos, consulta de status e suporte humano.
* **Filtro de Horário Comercial**: Gerenciamento dinâmico de respostas para períodos fora de expediente (Seg-Sex até 17:30, Sáb até 12h).
* **Protocolos de Segurança**: Validação via `VERIFY_TOKEN` e criptografia da Meta API.
* **Histórico de Atendimento**: Estrutura preparada para integração com bancos de dados e sistemas de gestão.

## 🚀 Arquitetura Técnica
O sistema utiliza tecnologias de ponta para garantir estabilidade e escalabilidade imediata:
* **Backend**: Flask (Python 3.14.3).
* **Servidor de Produção**: Gunicorn (Industrial Grade).
* **Infraestrutura**: Configurado para deploy otimizado em ambientes de nuvem como Render e Railway.

## ⚙️ Parâmetros de Configuração (Sistema)
Para o funcionamento da instância, o ambiente deve ser configurado com os seguintes parâmetros de segurança:
* `WHATSAPP_TOKEN`: Autenticação criptografada com a Meta.
* `VERIFY_TOKEN`: Chave de handshake para validação do Webhook.
* `PHONE_NUMBER_ID`: Identificador único da linha comercial.
* `PORT`: Gerenciamento dinâmico de porta para hospedagem.

## 💼 Vantagens Comerciais
1. **Redução de Custo**: Diminui a necessidade de equipe focada apenas em triagem inicial.
2. **Experiência do Cliente**: Respostas imediatas aumentam a taxa de conversão de orçamentos.
3. **Organização**: Dados como CPF, Placa e Modelo do Veículo são coletados antes mesmo do contato humano.

## ⚖️ Propriedade Intelectual e Licença
Este software e todo o seu código-fonte são de propriedade exclusiva de **Guilherme Aguiar**.
* Proibida a cópia, distribuição, engenharia reversa ou revenda sem autorização expressa do desenvolvedor.
* Todos os direitos reservados © 2026.