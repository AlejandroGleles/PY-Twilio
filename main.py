
import pandas as pd
# twilio -> enviar sms
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "your_auth_token"

client = Client(account_sid, auth_token)
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:

    tabela_vendas = pd.read_excel(f'{mes}.xlsx')

  
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]
        print(f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}')
        message = client.messages.create(
             to="+15558675309",
             from_="+15017250604",
             body=f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}')

        print(message.sid)




