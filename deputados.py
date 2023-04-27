import requests

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
res = requests.get(url=url).json()



for deputado in res['dados']:
    if deputado['siglaUf'] == 'SP':
        print(
        deputado['id'],
        deputado['nome'],
        deputado['siglaUf'],
        deputado['siglaPartido']
        )

total_deputados = len(res['dados'])
print(f'Total de deputados localizados:')