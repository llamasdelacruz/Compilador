
from difflib import SequenceMatcher
class Lexico():

    def __init__(self):
        self.tabla_tokens = {}
        self.reservadas_minusculas = ["int","float","char","string","boolean","output","input","start","end"]
       
    
    def comprobar_nombre_variable(self,cadena):
        #nos dice si la variable tiene $ seguido de puras letras minusculas
        contador_minusculas=0
        for i in range(len(cadena)):
            codigo_ascii_minusculas=ord(cadena[i])
            if(cadena[0]=="$"):
                if(codigo_ascii_minusculas>=97 and codigo_ascii_minusculas<=122):
                    #print("Entre al if anidado")
                    contador_minusculas+=1
                else:
                    contador_minusculas=0    
            else:    
                contador_minusculas=0   
                break                        
        if(contador_minusculas>0):
            #print("Es una variable valida")
            return True
        else:
            #print("No es una variable valida")   
            return False
    
    def comprobar_palabras_reservadas(self,cadena):
        # nos dice si la palabra reservada es valida
        contador_palabras_reservadas=0
        if(cadena=="INT"):
            contador_palabras_reservadas+=1
        elif(cadena=="FLOAT"):
            contador_palabras_reservadas+=1
        elif(cadena=="CHAR"):
            contador_palabras_reservadas+=1
            
        elif(cadena=="STRING"):
            contador_palabras_reservadas+=1
        
        elif(cadena=="BOOLEAN"):
            contador_palabras_reservadas+=1
        
        elif(cadena=="OUTPUT"):
            contador_palabras_reservadas+=1
        
        elif(cadena=="INPUT"):
            contador_palabras_reservadas+=1

        elif(cadena=="START"):
            contador_palabras_reservadas+=1

        elif(cadena=="END"):
            contador_palabras_reservadas+=1

        else:
            contador_palabras_reservadas=0           
                    
                
        if (contador_palabras_reservadas>0):
            #print("Es una palabra reservada valida")
            return True
        else:
            #print("No es una palabra reservada valida")     
            return False           

    def comprobar_operadores(self,cadena):
        # nos dice si el operador es valido
        contador_suma=0
        contador_resta=0
        contador_multi=0
        contador_division=0
        contador_igual=0
        for i in range(len(cadena)):
            if(cadena[i]=="+"):
                contador_suma+=1
            elif(cadena[i]=="-"):
                contador_resta+=1
            elif(cadena[i]=="*"):
                contador_multi+=1
            elif(cadena[i]=="/"):
                contador_division+=1
            elif(cadena[i]=="="):
                contador_igual+=1
                
        if(contador_suma>1 or contador_resta>1 or contador_multi>1 or contador_division>1 or contador_igual>1):
            contador_suma=0
            contador_resta=0
            contador_division=0
            contador_multi=0
            contador_igual=0     
        if(contador_suma==1 or contador_resta==1 or contador_multi==1 or contador_division==1 or contador_igual==1):
            #print("El operador es valido")
            return True
        else:
            #print("El operador es invalido") 
            return False  
                     
    def comprobar_decimales(self,cadena):
        # nos dice si el numero es correcto, si es entero o decimal
        contador_numeros=0
        contador_puntos=0
        contador_simbolos_especiales=0
        for i in range(len(cadena)):
            codigo_ascii_punto=ord(cadena[i])
            #print("Este es el codigo ascii cada vuelta",codigo_ascii_punto)

            if(codigo_ascii_punto>=48 and codigo_ascii_punto<=57):
                contador_numeros+=1
            elif(contador_numeros>=1 and codigo_ascii_punto==46):
                contador_puntos+=1    
                #print("Esto vale en contador punto con dos puntos : ", contador_puntos)
            elif(codigo_ascii_punto==46):
                contador_puntos+=1    
            #----- Seccion del numero 32 al 47 ------------------------------    
            if(codigo_ascii_punto==32 or codigo_ascii_punto==33 or codigo_ascii_punto==34 or codigo_ascii_punto==35 or codigo_ascii_punto==36 or codigo_ascii_punto==38 or codigo_ascii_punto==39 or codigo_ascii_punto==40 or codigo_ascii_punto==41 or codigo_ascii_punto==42 or codigo_ascii_punto==43 or codigo_ascii_punto==44 or codigo_ascii_punto==45 or codigo_ascii_punto==47 or codigo_ascii_punto==58 or codigo_ascii_punto==59 or codigo_ascii_punto==60 or codigo_ascii_punto==61 or codigo_ascii_punto==62 or codigo_ascii_punto==63 or codigo_ascii_punto==64):
                #print("Entre a la condicion")
                contador_simbolos_especiales+=1
                contador_puntos=0
                contador_numeros=0
                break
                
                         
        #print("Este es el contador numeros al salir del ciclo: " ,contador_numeros)
        #print("Este es el contador puntos al salir del ciclo : ", contador_puntos)   
        
        if(contador_numeros>1 and contador_puntos==0):
             #print("Es un numero correcto entero")
             return True
             
        elif(contador_numeros>1 and contador_puntos==1):
             #print("Es un numero correcto  decimal")  
             return True
             
        elif(contador_puntos>=2 or contador_puntos>2):
            #print("Es un numero incorrecto")  
            return False    
        
        elif(contador_puntos==1):
            #print("Es un numero incorrecto")  
            return False
            
        if(contador_simbolos_especiales>=1):
            #print("Es un numero incorrecto") 
            return False          
            
            
    def partir_por_palabras(self,linea):
        #En este metodo se parten por palabras o numeros la linea que nos pasaron
        linea_nueva = []
        #partir por espacios primero
        partir1 = linea.split()

        #partimos por operadores
        #vemos si tiene un operador 
        for palabra in partir1:

            palabra_completa = ""
            singno_anterior = ""

            for letra in palabra:
                
                # partimos las palabras en base a los operadores
                if(letra == "=" or letra == "+" or letra == "*" or letra == "/" 
                   or letra == "-" or letra == ";" or letra == "'" or letra == "," or letra == "#" ):


                    if(singno_anterior != letra and palabra_completa != "" ):
                        linea_nueva.append(palabra_completa.strip())
                        palabra_completa = ""
                        
                    singno_anterior = letra
                 
                else:
                    # aca llegan las letras normales
                    if(singno_anterior != ""):
                        linea_nueva.append(palabra_completa.strip())
                        singno_anterior = ""
                        palabra_completa = ""
                        
                palabra_completa += letra

                  
            linea_nueva.append(palabra_completa.strip())

        print(linea_nueva)
        return linea_nueva
    
        
    def agregar_tokens(self,token,tipo,linea):
        #agrega un token al diccionario si no se encuentra y si lo hace agrega la linea en la que esta
        if(token in self.tabla_tokens.keys()):
            self.tabla_tokens[token]["referencia"].append(linea)
        else:
            self.tabla_tokens[token] = {"tipo": tipo, 'declara':linea, "referencia":[]}

    def analizar(self,texto):
        #en este metodo se gestionan los erores y los tokens de el codigo dado
        #este metodo junta todo los de arriba para analizar el lexico del codigo

        lineas = texto.split("\n")

        for linea in lineas:
            palabras_linea = linea.split() #espacios
            abertura = 0
            cierre = 0
            print(palabras_linea)
            for palabra in palabras_linea:
                #vemos si es un comentario
                if("#" == palabra or palabra[0] == "#"):
                    print("No se analiza es un comentario:"+ palabra)
                    break
                #vemos si es texto 
                elif("'" == palabra or palabra[0] == "'" or palabra[-1] == "'"):
                    
                    
                    if(("'" == palabra and abertura == 0) or (palabra[0] == "'" and abertura == 0) ):
                        print("inicio de string:",palabra)
                        abertura = 1
                    elif(("'" == palabra and cierre == 0) or (palabra[-1] == "'" and cierre == 0)):
                        cierre = 1

                    if(abertura == 1 and cierre == 1):
                        abertura = 0
                        cierre = 0
                        print("fin de string:",palabra)

                # para evaluar operadores
                elif(palabra == "+" or palabra.count("+") == len(palabra) or 
                     palabra == "-" or palabra.count("-") == len(palabra) or 
                     palabra == "*" or palabra.count("*") == len(palabra) or
                     palabra == "=" or palabra.count("=") == len(palabra) or
                     palabra == "/" or palabra.count("/") == len(palabra)):
                    
                    print("Es un operador:",palabra)

                # para evaluar los caracteres validos
                elif(palabra == "," or palabra == ";"):
                    print("Carcater valido:",palabra)

                #checa si  una palabra reservada
                elif(palabra.isupper() or self.es_palabra_reservada_minusculas(palabra)):
                    print("Palabra reservada:",palabra)

                #checa si es un numero 
                elif( palabra.isnumeric() or (palabra[0].isdigit() and self.porcentaje_numeros(palabra))):
                    print("Es un numero:",palabra)

                #checa que sea una variable
                elif( palabra[0] == "$" or  palabra.islower() or palabra.isalpha()):
                    print("es una variable:", palabra)

                else:
                    print("Cadena incorrecta de caracteres:",palabra)


    def es_palabra_reservada_minusculas(self,cadena):
        # ve si es una palabra reservada en minisculas y si lo es manda true
        cadena = cadena.lower()
        is_true = False
        for i in self.reservadas_minusculas:
        
            if(cadena == i):
                is_true = True
                break

        return is_true
    


    def porcentaje_numeros(self,cadena):
        # ve si el porcentaje de numeros en la cadena es del 80%
        # si lo es regresa true, ignoramos el punto
        #lo parte pir caracteres
        caracteres = [ i for i in cadena] 
        #print(caracteres)
        esunnumero_lista = list(map(lambda c: True if c == "." else c.isdigit() ,caracteres))
        #print(esunnumero_lista)

        porcentaje_numeros = (esunnumero_lista.count(True)*100)/len(esunnumero_lista)     
        #print(porcentaje_numeros) 

        if(len(caracteres) <= 3):

            numeros =  esunnumero_lista.count(True)
            no_numeros = esunnumero_lista.count(False)

            if(numeros >= no_numeros ):
                return True
            else:
                return False
        else:   

            if(porcentaje_numeros >= 75):
                return True
            else:
                return False


if __name__ == "__main__":
    objecto = Lexico()
    #objecto.partir_por_palabras("'alo==2.67893',22++*+- 4.s#3")
    texto = "INICIO\nInt alo;\nalo = 22 + 3;\noutput alo;\nFIN"
    texto = " 7777  34,45 2,0 3.5 ;;;+- ss a898"
    objecto.analizar(texto) 
    #print(objecto.porcentaje_numeros("89.00"))
    #objecto.partir_por_palabras("OUTPUT output $ESTO 'hola ,$mani 33a")
    #m = SequenceMatcher(None, "boolean", "B@olean").ratio()
    #print(m)

