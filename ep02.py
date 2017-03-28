#Ep02 - Inspermon
import json
import random
with open('inspermons.json') as arquivo:
    inspermon = json.load(arquivo)

while True:
    açao_usuario = input('Você pode andar e procurar Inspermons ou dormir para recuperar sua vida. \n Digite 1 para andar ou 0 para dormir: ')
    if açao_usuario == 0:
