import sys
from os import listdir
from os.path import isfile, join

#def leer(ruta):
def leer():    
    try:
        onlyfiles = [f for f in listdir("../InstanciasSAT") if isfile(join("../InstanciasSAT", f))]
        for f in onlyfiles:
            rutaL="../InstanciasSAT/"+f#Ruta a los archivos de lectura
            name= f.split(".")
            #print(name)
            rutaE="../InstanciasMiniZinc/reduccion_"+name[0]+".mzn"#Ruta a los archivos de escritura
            archivoR = open(rutaL, "r") 
            lineas = archivoR.readlines()
            result = {'variables': 0, 'constraints': 0, 'lines':[]}
            for linea in lineas:
                #linea.replace("%","")
                if linea[0] != 'c' and linea[0] != 'p' and linea[0] != '%' and linea[0] != '0' and linea[0] != '\n': result['lines'].append(linea) #Aade a lines las lineas que corresponden a clausulas
                if linea[0] == 'p':
                    lineaP = linea.split()
                    result['variables'] = int(lineaP[2])
                    result['constraints'] = int(lineaP[3])
            archivoR.close()
            convertir(rutaE,result)        
    except Exception as e:
        print("Error[leer]: ", e)
        return None

def convertir(ruta, datos):
    try: 
        archivoW = open(ruta, "w")
        #Construir definicion de variables
        for x in range(1, datos['variables']+1):
            archivoW.write("var 0..1: v"+ str(x) + "; var 0..1: n_v" + str(x) +";\n")
            archivoW.write("constraint v"+ str(x) + " + n_v" + str(x) +" = 1;\n\n")

        for linea in datos['lines']:
            elementos = linea.split()
            #print(elementos)
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
    except Exception as e:
        print("Error[convertir]: ", e)
        return None

def main (entrada):
    try:
        resultado = leer()
        #if len(entrada) == 3:
        #resultado = leer(entrada[1])
        #if resultado: convertir(entrada[2], resultado)
    except Exception as e:
        print("Error[main]: ", e)
            
main(sys.argv)