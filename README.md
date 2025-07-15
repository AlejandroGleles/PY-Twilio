# PY-Twilio
# 📊 Notificação de Vendas por SMS com Python e Twilio

Projeto simples em **Python** para automatizar a verificação de metas de vendas mensais e envio de notificações via **SMS (Twilio)** quando a meta é batida.

---

## 🚀 Objetivo
Este projeto percorre arquivos `.xlsx` contendo os resultados de vendas mensais e, sempre que um vendedor ultrapassar **R$ 55.000,00 em vendas no mês**, o sistema:
1. Identifica o vendedor e o valor.
2. Exibe a informação no console.
3. Envia um **SMS automático** via API do Twilio notificando a conquista.

---

## 🔧 Tecnologias Utilizadas
- **Python 3.x**
- **Pandas** (manipulação de planilhas Excel)
- **OpenPyXL** (leitura de arquivos `.xlsx`)
- **Twilio API** (envio de SMS)

---

## 🗂️ Estrutura dos Arquivos
📂 Projeto
├─ janeiro.xlsx
├─ fevereiro.xlsx
├─ março.xlsx
├─ abril.xlsx
├─ maio.xlsx
├─ junho.xlsx
├─ main.py
└─ README.md

yaml
Copiar
Editar

Cada arquivo `.xlsx` deve conter no mínimo essas colunas:  
| Vendedor | Vendas |
|----------|--------|
| Fulano   | 60000  |

---

## 📝 Pré-requisitos
- Conta no [Twilio](https://www.twilio.com/)
- Chave `account_sid` e `auth_token` obtidos no painel do Twilio
- Ambiente virtual Python configurado com:
```bash
pip install pandas openpyxl twilio
▶️ Como Executar
1️⃣ Coloque as planilhas .xlsx no mesmo diretório do projeto.
2️⃣ Atualize seu código com as credenciais reais do Twilio:

python
Copiar
Editar
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"
3️⃣ Execute o código:

bash
Copiar
Editar
python main.py
🔍 Fluxo do Código
Varre os meses da lista ['janeiro','fevereiro','março','abril','maio','junho']

Abre cada arquivo .xlsx com pandas.read_excel()

Verifica se existe alguma venda acima de R$ 55.000,00

Envia SMS via Twilio API informando o mês, vendedor e valor da venda

Exibe o resultado no terminal

📬 Exemplo de Mensagem SMS Enviada
yaml
Copiar
Editar
No mês março alguém bateu a meta. 
Vendedor: Maria, Vendas: 60000
⚠️ Atenção
As chaves do Twilio não devem ser expostas publicamente em projetos reais (use dotenv em produção).

Os números de telefone to e from_ devem estar configurados corretamente no painel do Twilio.

📎 Exemplo de Saída no Console
yaml
Copiar
Editar
No mes março alguem bateu a meta. Vendedor: Maria, Vendas: 60000
SMXXXXXXXXXXXXXXXXXXXXXXXXXXXX sent
🤝 Licença
Este projeto é livre para fins de estudo e prática pessoal.
