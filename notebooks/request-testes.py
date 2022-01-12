import requests as rq

dados = {'garagem':2, 'ano': 2001, 'tamanho':140}
auth = rq.auth.HTTPBasicAuth('d', '123')

resp =rq.post('http://127.0.0.1:5000/cotacao/', json=dados, auth=auth)

print(resp.status_code)
print(resp.text)