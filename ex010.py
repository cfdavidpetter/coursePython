import urllib.request
import json

def quotation(coin):
    contents = urllib.request.urlopen("http://economia.awesomeapi.com.br/json/" + coin + "-BRL/1").read()
    return float(json.loads(contents)[0]['high'])

real = float(input('How much do you have in your wallet? R$'))

coins = [
    ('USD', 'dollar'),
    ('EUR', 'euro'),
    ('GBP', 'pound sterling'),
    ('ARS', 'argentine peso'),
    ('JPY', 'japanese yen'),
    ('CHF', 'swiss franc'),
    ('CNY', 'chinese yuan'),
]

for coin in coins:
    print('In the current quotation of the {} you have $:{:.2f}'.format(coin[1], real / quotation(coin[0])))