
file = input('Introduce nombre del archivo a leer:      ') 


datalist = []
f = open(file, "r")

text = f.readlines()

for line in text:
    if line[0] != '\t':
        breakline = line.find(":")
        datalist.append(line[0:breakline])
apend = 0
for lines in datalist:
    print('{} - {}'.format(apend,lines))
    apend += 1


linea = int(input('Selecciona número de recurso a leer:    '))

section = datalist[linea] + ':'
print(section)

for line in text




    
    


    
    
    

        





