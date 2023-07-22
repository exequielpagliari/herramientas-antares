texto = ''
completo_texto = []
while texto != 'Q':

    texto = input('ingrese valores de string nivel:     ')

    texto = texto.replace('\t','')

    texto = texto.replace('>', '')
    if texto != 'Q':
        completo_texto.append(texto)



cadena = ''
for line in completo_texto:
    cadena = cadena + " " +  line
print(cadena)