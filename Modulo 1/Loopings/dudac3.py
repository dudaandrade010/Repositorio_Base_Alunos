palavra = input('digite sua palavra')
vogais = 'a,e,i,o,u'
contador=0
for i in palavra:
    if i in vogais:
        contador=contador+1
        print(i, 'é vogal',contador)
    else:
        print('a palavra nao tem vogais')
