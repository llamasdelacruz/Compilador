
class Lexico():

    def __init__(self):
        print("Aqui esta la clase para colocar los metodo que vas hacer aldo")

    def comprobar_inicio_fin(self,cadena):
        contador_start=0
        contador_fin=0
        for i in range(len(cadena)):
            if(cadena[i]=="S" or cadena[i]=="T" or cadena[i]=="A" or cadena[i]=="R" or cadena[i]=="T"):
                contador_start+=1
            elif(cadena[i]=="E" or cadena[i]=="N" or cadena[i]=="D"):
                contador_fin+=1
        
        if(contador_start==5 or contador_fin==3):
            print("Es una palabra reservada valida")
        else:
            print("Error en palabra reservada")
    
    def comprobar_nombre_variable(self,cadena):
        contador_minusculas=0
        for i in range(len(cadena)):
            codigo_ascii_minusculas=ord(cadena[i])
            if(codigo_ascii_minusculas>=97 and codigo_ascii_minusculas<=122):
                contador_minusculas+=1
            else:    
                contador_minusculas=0   
                break                        
        if(contador_minusculas>0):
            print("Es una variable valida")
        else:
            print("No es una variable valida")   
    
    def comprobar_palabras_reservadas(self,cadena):
        contador_palabras_reservadas=0
        for i in range(len(cadena)):
            if(cadena[i]=="I" or cadena[i]=="F" or cadena[i]=="C" or cadena[i]=="S" or cadena[i]=="B" or cadena[i]=="O"):
                contador_palabras_reservadas+=1
                
        if (contador_palabras_reservadas>0):
            print("Es una palabra reservada valida")
        else:
            print("No es una palabra reservada valida")                

    def comprobar_operadores(self,cadena):
        contador_operadores=0
        for i in range(len(cadena)):
            if(cadena[i]=="+" or cadena[i]=="-" or cadena[i]=="*" or cadena[i]=="/" or cadena[i]=="="):
                contador_operadores+=1
        if(contador_operadores>0):
            print("El operador es valido")
        else:
            print("El operador es invalido")   
                     
    def comprobar_decimales(self,cadena):
        contador_puntos=0
        for i in range(len(cadena)):
            if(cadena[i]=="."):
                contador_puntos+=1
            elif(cadena[0]=="."):
                contador_puntos=0
        if(contador_puntos>0):
            print("EL numero es correcto")
        else:
            print("El numero es incorrecto")   
    
    def comprobar_comentarios(self,cadena):
        contador_comentario=0
        for i in range(len(cadena)):
            if(cadena[0]=="#"):
                contador_comentario+=1
        if(contador_comentario>0):
            print("El comentario es valido")
        else:
            print("Error de cadena no valido")
    def analizar(self,texto):
        lineas = texto.split("\n")
        
        


if __name__ == "__main__":
    objecto = Lexico()
    texto = "INICIO\nInt alo;\nalo = 22 + 3;\noutput alo;\nFIN"
    objecto.analizar(texto)
    cadena=str(input("Dame una cadena por favor : "))
    #objecto.comprobar_inicio_fin(cadena)
    #objecto.comprobar_nombre_variable(cadena)
    #objecto.comprobar_palabras_reservadas(cadena)
    #objecto.comprobar_operadores(cadena)
    #objecto.comprobar_decimales(cadena)
    #objecto.comprobar_comentarios(cadena)