import requests

res = requests.get(url='https://h-apigateway.conectagov.estaleiro.serpro.gov.br/api-cep/v1/consulta/cep/60130240')

print(res)

if res:
    print('SUCESSO')
    print(res.status_code)
    print(res.text)
else:
    print('ERRO')
