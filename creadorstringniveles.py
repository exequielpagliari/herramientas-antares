



def select_file():
    file = input('Nombre de archivo a almacenar información:    ')
    return file


def text_input():
    texto = input('Ingrese String a transformar:    ')
    texto = texto.split()
    return texto

def first_symbol():
    symbol = input('Ingresar símbolo para identación:    ')
    if symbol == '':
        symbol = '>'
    return symbol

def tabs_input():
    N_tabs = int(input('Ingrese cantidad de identación:   '))
    return N_tabs


def identacion(tabs):
    identation = ''
    symbol = first_symbol()
    for tab in range(tabs):
        identation = identation + '\t'
    if(symbol != ''):
        s = symbol
    else:
        s = '>'
    identation = identation + str(s) + '\t'
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

    try:
        file = open(f, "r")
        
    except FileNotFoundError:
        file = open(f, "w")
        file = open(f,'r')


    old_data = file.readlines()
    new_data = old_data + lineas

    file.close()
    file = open(f, "w")
    file.writelines(new_data)
    file.write('\n')
    file.close

while True:
    file = select_file()
    texto = text_input()
    tabs = tabs_input()
    grabar_archivo(file,cargar_texto(texto,tabs))


    