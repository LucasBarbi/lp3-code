import requests

cep = '17011160'
res = requests.get(
    f'https://viacep.com.br/ws/{cep}/json/')

if res:
    print('SUCESSO!')
    print('Dados do cep: ')
    dados_cep = res.json()

    for chave, valor in dados_cep.items():
        print(chave, '=', valor)
else:
    print('ERRO: Não foi possível localizar informações do cep.')
