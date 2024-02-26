import pandas as pd
from twilio.rest import Client
# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACf763bec1df10f69237ad44370c5d2af1"
auth_token  = "b40ef90bf2979c88283ed00fe665c898"
client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5531982688401",
            from_="+19253508712",
            body="Hello from Python!")
        print(message.sid)

