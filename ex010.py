import urllib.request
import json

real = float(input('How much do you have in your wallet? R$'))

contents = urllib.request.urlopen("http://economia.awesomeapi.com.br/json/USD-BRL/1").read()
quotation = float(json.loads(contents)[0]['high'])

print('In the current quotation of the dollar you have US$:{:.2f}'.format(real / quotation))