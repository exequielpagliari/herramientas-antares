"""

			>	^Pish/carrier^We've brought in a carrier of our own, the ISN 2020187. It
			>	should be able to successfully engage the Constant Voice. However, if
			>	2020187 is destroyed, the mission will be aborted. It has its own group
			>	of escorts, including some Obish ships.

"""
file = input('Nombre de archivo a almacenar información:    ')

f = open(file, "w")

texto = input('Ingrese String a transformar:    ')

texto = texto.split()

N_tabs = int(input('Ingrese cantidad de identación:   '))

lineas = []

cadena = ''

identation = ''

for tab in range(N_tabs):
    identation = identation + '\t'

identation = identation + '>' + '\t'



while len(texto) > 0:
    cadena = identation
    if len(texto) > 11:
        for line in range(11):
            cadena =  cadena + texto.pop(0) + ' '
    else:
        for line in range(len(texto)):
            cadena = cadena + texto.pop(0) + ' '
    
    cadena = cadena + '\n'
    print(cadena)
    lineas.append(cadena)
    cadena = ''

    print(lineas)

f.writelines(lineas)
f.close

