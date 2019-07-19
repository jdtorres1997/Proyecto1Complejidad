variables = {
    '1': 'a',
    '2': 'b',
    '3': 'c',
    '4': 'd',
    '5': 'e',
    '6': 'f',
    
}
def leer():
    archivoR = open("pruebaDatos.txt", "r") 
    lineas = archivoR.readlines()
    result = {'variables': 0, 'constraints': 0, 'lines':[]}
    for linea in lineas:
        if linea[0] != 'c' and linea[0] != 'p': result['lines'].append(linea) #Añade a lines las lineas que corresponden a clausulas
        if linea[0] == 'p':
            lineaP = linea.split()
            result['variables'] = lineaP[2]
            result['constraints'] = lineaP[3]
    archivoR.close()
    return result

def convertir(datos):
    archivoW = open("pruebaResultados.txt", "w")
    for linea in datos:
        elements = linea.split()
        for e in elements:
            pass

datos_leidos = leer()

convertir(datos_leidos)