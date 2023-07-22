



def select_file():
    file = input('Nombre de archivo a almacenar información:    ')
    return file


def text_input():
    texto = input('Ingrese String a transformar:    ')
    texto = texto.split()
    return texto

def tabs_input():
    N_tabs = int(input('Ingrese cantidad de identación:   '))
    return N_tabs


def identacion(tabs):
    identation = ''
    for tab in range(tabs):
        identation = identation + '\t'

    identation = identation + '>' + '\t'
    return identation

def cargar_texto(texto,tabs):
    cadena = ''
    lineas = []
    while len(texto) > 0:
        cadena = identacion(tabs)
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
    return lineas

def grabar_archivo(f,lineas):
    f = open(f, "w")
    f.writelines(lineas)
    f.close

while True:
    file = select_file()
    texto = text_input()
    tabs = tabs_input()
    grabar_archivo(file,cargar_texto(texto,tabs))


    