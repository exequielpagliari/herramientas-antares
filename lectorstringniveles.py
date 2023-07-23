
def select_file():
    file = input('Nombre de archivo a almacenar información:    ')
    return file

def grabar_archivo(f,lineas):
    file = open(f, "r")
    old_data = file.readlines()
    new_data = old_data + lineas

    file.close()
    file = open(f, "w")
    file.writelines(new_data)
    file.write('\n')
    file.close


def input_text():
    text = input('ingrese valores de string nivel:     ')
    return text

def tab_replace(text):
    text = str(text).replace('\t','')
    return text

def symbol_replace(text):
    text = str(text).replace('>', '')
    return text


def read_text():
    completo_texto = []
    texto = ''
    while texto != 'Q':

        texto = input_text()

        texto = tab_replace(texto)
        print(texto)
        texto = symbol_replace(texto)
        if texto != 'Q':
            texto = texto + " "
            completo_texto.append(texto)

    return completo_texto


def print_cadena(completo_texto):
    cadena = ''
    for line in completo_texto:
        cadena = cadena + " " +  line
    print(cadena)
    return completo_texto


while True:
    file = select_file()
    lineas = print_cadena(read_text())
    grabar_archivo(file,lineas)