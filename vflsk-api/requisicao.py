import requests
link = 'http://127.0.0.1:5000/totvendas'
requisicao = requests.get(link)
# print(f'requisicao: {requisicao}')
print(requisicao.json())
