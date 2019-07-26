import sys
def leer(ruta):
    try:
        archivoR = open(ruta, "r") 
        lineas = archivoR.readlines()
        result = {'variables': 0, 'constraints': 0, 'lines':[]}
        for linea in lineas:
            if linea[0] != 'c' and linea[0] != 'p' and linea[0] != '%' and linea[0] != '0' and linea[0] != '\n': result['lines'].append(linea) #Anade a lines las lineas que corresponden a clausulas
            if linea[0] == 'p':
                lineaP = linea.split()
                result['variables'] = int(lineaP[2])
                result['constraints'] = int(lineaP[3])
        archivoR.close()
        return result
    except Exception as e:
        print("Error[leer]: ", e)
        return None

def convertir(ruta, datos):
    archivoW = open(ruta, "w")
    #Construir definicion de variables
    for x in range(1, datos['variables']+1):
        archivoW.write("var 0..1: v"+ str(x) + "; var 0..1: n_v" + str(x) +";\n")
        archivoW.write("constraint v"+ str(x) + " + n_v" + str(x) +" = 1;\n\n")

    for linea in datos['lines']:
        elementos = linea.split()
        elementos.pop()
        archivoW.write("constraint ")
        iterator = 0
        if elementos[iterator][0] == '-':
            elementos[iterator] = elementos[iterator].replace("-","")
            archivoW.write("n_v"+elementos[iterator])
        else:
            archivoW.write("v"+elementos[iterator])
        iterator += 1
        while iterator < len(elementos):
            archivoW.write(" + ")
            if elementos[iterator][0] == "-":
                elementos[iterator] = elementos[iterator].replace("-","")
                archivoW.write("n_v"+elementos[iterator])
            else:
                archivoW.write("v"+elementos[iterator])
            iterator += 1
        archivoW.write(" >= 1;\n")
    archivoW.write("solve satisfy;")

def main (entrada):
    try:
        if len(entrada) == 3:
            input_file = entrada[1]
            output_file = entrada[2]
            resultado = leer(input_file)
            if resultado: convertir(output_file, resultado)
    except Exception as e:
        print("Error[main]: ", e)
            
main(sys.argv)