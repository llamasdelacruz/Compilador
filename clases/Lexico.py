
from difflib import SequenceMatcher
class Lexico():

    def __init__(self):
        self.tabla_tokens = {}
        self.reservadas_minusculas = ["int","float","char","string","boolean","output","input","start","end"]
        self.regla_1 ={}
    
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
        
    def comprobar_nombre_variable(self,cadena):
        #nos dice si la variable tiene $ seguido de puras letras minusculas
        contador_minusculas=0
        if(cadena[0] == "$"):
            if(len(cadena) > 1):
                for i in range(len(cadena)):
                    if(i == 0 and cadena[i] == "$"):
                        contador_minusculas+=1
                    elif(cadena[i] == "$" and i > 0):
                        contador_minusculas=0
                        break  
                    else:
                        codigo_ascii_minusculas=ord(cadena[i])
                        
                        if(codigo_ascii_minusculas>=97 and codigo_ascii_minusculas<=122):
                            #print("Entre al if anidado")
                            contador_minusculas+=1
                        else:
                            contador_minusculas=0  
                            break  
                                    
        if(contador_minusculas>0):
            #print("Es una variable valida")
            return True
        else:
            #print("No es una variable valida")   
            return False

                    
        
    def agregar_tokens(self,token,tipo,linea):
        #agrega un token al diccionario si no se encuentra y si lo hace agrega la linea en la que esta
        if(token in self.tabla_tokens.keys()):
            self.tabla_tokens[token]["referencia"].append(linea)
        else:
            self.tabla_tokens[token] = {"tipo": tipo, "declara":linea, "referencia":[]}

    def analizar(self,texto):
        #en este metodo se gestionan los erores y los tokens de el codigo dado
        #este metodo junta todo los de arriba para analizar el lexico del codigo
        errores = ""
        lineas = texto.split("\n")

        numero_linea = 0


        for linea in lineas:
            palabras_linea = linea.split() # todas las palabras
            abertura = 0
            cierre = 0
            cantidad_elementos = len(palabras_linea)

            numero_linea += 1
            for i in range(0,cantidad_elementos):
                palabra = palabras_linea[i]

           

                #vemos si es un comentario
                if("#" == palabra or palabra[0] == "#"):
                    #print("No se analiza es un comentario:"+ palabra)
                    self.agregar_tokens("#","Caracter",numero_linea)
                    break
                #vemos si es texto 
                elif("'" == palabra or palabra[0] == "'" or palabra[-1] == "'" or palabra == "'"):
                    
                    

                    if(palabra[0] == "'" and palabra[-1] == "'" and len(palabra) > 1):
                        self.agregar_tokens("'","Caracter",numero_linea)
                        self.agregar_tokens("'","Caracter",numero_linea)
                    else:
                        self.agregar_tokens("'","Caracter",numero_linea)
                        if(("'" == palabra and abertura == 0) or (palabra[0] == "'" and abertura == 0) ):
                            #print("inicio de string:",palabra)
                            abertura = 1
                        elif(("'" == palabra and cierre == 0 and abertura == 1) or (palabra[-1] == "'" and cierre == 0 and abertura == 1) 
                             or (palabra == "'" and cierre == 0 and abertura == 1)):
                            cierre = 1
                        else:
                            if(len(palabra) == 1):
                                #print("Caracter incorrecto",palabra)
                                errores += "\n Error de léxico !!!!! En línea "+ str(numero_linea) +" En caracter invalido " + palabra
                            else:
                                errores += "\n Error de léxico !!!!! En línea "+ str(numero_linea) +" Cadena incorrecta de caracteres " + palabra
                                #print("Cadena incorrecta de caracteres:",palabra)


                        if(abertura == 1 and cierre == 1):
                            abertura = 0
                            cierre = 0
                            #print("fin de string:",palabra)
                elif(abertura == 1):
                    continue
                # para evaluar operadores
                elif(palabra == "+" or palabra.count("+") == len(palabra) or 
                     palabra == "-" or palabra.count("-") == len(palabra) or 
                     palabra == "*" or palabra.count("*") == len(palabra) or
                     palabra == "=" or palabra.count("=") == len(palabra) or
                     palabra == "/" or palabra.count("/") == len(palabra)):
                    
                    #print("es un operador:",palabra)
                    if(self.comprobar_operadores(palabra)):
                        self.agregar_tokens(palabra,"Operador",numero_linea)
                    else:
                        errores += "\n Error de léxico !!!!! En línea "+ str(numero_linea) +" En operador " + palabra

                # para evaluar los caracteres validos
                elif(palabra == ","  or palabra == ";" ):
                    
                    self.agregar_tokens(palabra[0],"Caracter",numero_linea)

                #checa si  una palabra reservada
                elif( self.mayusculas_todas(palabra)
                     or self.es_palabra_reservada_minusculas(palabra)):
                    #print("Entre a la funcion",palabra)
                    
                    # vemos si hay otro elemento adelante de el
                    if(palabra[0] == "$"):
                        if((i+1) <= (cantidad_elementos-1)):
                            # vemos si el siguiente elemento es un operador
                            if( palabras_linea[i+1] == "+" or palabras_linea[i+1].count("+") == len(palabras_linea[i+1]) or 
                                palabras_linea[i+1] == "-" or palabras_linea[i+1].count("-") == len(palabras_linea[i+1]) or 
                                palabras_linea[i+1] == "*" or palabras_linea[i+1].count("*") == len(palabras_linea[i+1]) or
                                palabras_linea[i+1] == "=" or palabras_linea[i+1].count("=") == len(palabras_linea[i+1]) or
                                palabras_linea[i+1] == "/" or palabras_linea[i+1].count("/") == len(palabras_linea[i+1])):
                                

                                if(self.comprobar_nombre_variable(palabra)):
                                    self.agregar_tokens(palabra,"Identificador",numero_linea)
                                else:
                                    errores += "\n Error de léxico !!!!! En línea "+ str(numero_linea) +" En variable "+ palabra

                                #print("es una variable:", palabra)
                            else:
                                if(i == 0):
                                    
                                    if(self.comprobar_palabras_reservadas(palabra)):
                                        self.agregar_tokens(palabra,"Palabra reservada",numero_linea)
                                    else:
                                       errores += "\n Error de léxico !!!!! En línea "+ str(numero_linea) +" En palabra reservada " + palabra
                                    #print("Es una palabra reservada:",palabra)

                                else:
                                    if(self.comprobar_nombre_variable(palabra)):
                                        self.agregar_tokens(palabra,"Identificador",numero_linea)
                                    else:
                                        errores += "\n Error de léxico !!!!! En línea "+ str(numero_linea) + " En variable "+ palabra

                                    #print("es una variable:", palabra)
                        else:

                            if(self.comprobar_palabras_reservadas(palabra)):
                                self.agregar_tokens(palabra,"Palabra reservada",numero_linea)
                            else:
                                errores += "\n Error de léxico !!!!! En línea "+ str(numero_linea) +" En palabra reservada " + palabra
                                #print('Error de palabra reservada:',palabra)
                            #print("Es una palabra reservada:",palabra)
                            
                    else:
                        if(self.comprobar_palabras_reservadas(palabra)):
                            self.agregar_tokens(palabra,"Palabra reservada",numero_linea)
                        else:

                            errores += "\n Error de léxico !!!!! En línea "+ str(numero_linea) +" En palabra reservada " + palabra
                            #print('Error de palabra reservada:',palabra)

                        #print("Es una palabra reservada:",palabra)    
            
                #checa si es un numero 
                elif( palabra.isdigit() or 
                     palabra[0].isdigit() and self.porcentaje_numeros(palabra)):
                
                    if(palabra.isdigit() or self.decimales(palabra)):
                        #print("Numero valido")
                        self.agregar_tokens(palabra,"Caracter",numero_linea)
                    else:
                        errores += "\n Error de léxico !!!!! En línea " + str(numero_linea) +" En número incorrecto " + palabra
                        #print('Error de numero:',palabra)
                    
                #checa que sea una variable
                elif(palabra[0] == "$" or (palabra.isalpha() and palabra.islower())):
                    
                    if(self.comprobar_nombre_variable(palabra)):

                        self.agregar_tokens(palabra,"Identificador",numero_linea)
                    else:
                        errores += "\n Error de léxico !!!!! En línea "+ str(numero_linea) +" En variable " + palabra
                        #print("Error de variable:", palabra) 
                    
                    #print("es una variable:", palabra) 

                else:
                    if(len(palabra) == 1):
                        #print("Caracter incorrecto",palabra)
                        errores += "\n Error de léxico !!!!! En línea "+ str(numero_linea) +" En caracter invalido " + palabra
                    else:
                        errores += "\n Error de léxico !!!!! En línea "+ str(numero_linea) +" Cadena incorrecta de caracteres " + palabra
                        #print("Cadena incorrecta de caracteres:",palabra)

        return errores




    def porcentaje_numeros(self,cadena):
        # ve si el porcentaje de numeros en la cadena es del 80%
        # si lo es regresa true, ignoramos el punto y la coma
        #lo parte pir caracteres
        caracteres = [ i for i in cadena] 
        #print(caracteres)
        esunnumero_lista = list(map(lambda c: True if c == "." or c == "," else c.isdigit() ,caracteres))
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
            
    def decimales(self,cadena):

        punto = 0
        bandera = True
        for i in range(len(cadena)):
         

            if(cadena[i].isdigit() == False and cadena[i] != "."):
                bandera = False
                break

            if(cadena[i] == '.' and i == 0 or cadena[i] == '.' and i == len(cadena)-1):
                bandera = False
                punto +=1
                break
            if(i > 0 and punto == 0 and cadena[i] == "."):
                punto = 1
            elif(i > 0 and punto == 1 and cadena[i] == "."):
                bandera = False
                punto +=1
                break
            
        return bandera
            
    def es_palabra_reservada_minusculas(self,cadena):
        # ve si es una palabra reservada en minisculas y si lo es manda true
        cadena = cadena.lower()

        is_true = False
        for i in self.reservadas_minusculas:
        
            if(cadena.find(i) != -1):
                is_true = True
                break

        return is_true
            
    def parecido_palabra_reservada(self,cadena):
        # que tan parecida es la cadena a una palabra reservada
        
        cadena = cadena.lower()
        parecido_mas_grande = 0
        palabra_reservada = ""
        for i in self.reservadas_minusculas:

            concidencia = SequenceMatcher(None, i, cadena).ratio()
           
            if(parecido_mas_grande < concidencia):
                parecido_mas_grande  = concidencia
                palabra_reservada = i.upper()
            
       
        if(parecido_mas_grande >= 0.50):
            return palabra_reservada
        else:
            palabra_reservada = ""
            return palabra_reservada
        


    def mayusculas_todas(self,cadena):
        caracteres = [ i for i in cadena] 
        #print(caracteres)
        letras = list(map(lambda c: c.isupper() ,caracteres))
        if(len(letras) == letras.count(True)):
            return True
        else:
            return False
        
    def minusculas_todas(self,cadena):
        caracteres = [ i for i in cadena] 
        #print(caracteres)
        letras = list(map(lambda c: True if c.islower() and c.isalpha() else False ,caracteres))
        if(len(letras) == letras.count(True)):
            return True
        else:
            return False
    
    def crear_reglas(self,palabra):
        cantidad_elementos = len(palabra)
        for i in range(0,cantidad_elementos):
            if(palabra[i]=="Programa"):
                self.regla_1= {"n": i, "Programa":palabra[i], "complemento":["#"]}
                print("Entre a la condicion")
                
        print("Esto es lo que llega a crear reglas",palabra)
        print("Esto es lo que llega a crear reglas",self.regla_1)
    
   

if __name__ == "__main__":
    objecto = Lexico()
    
    
    texto = " START \n 'Dame un dato entero: ' ; \n END \n START"
    objecto.analizar(texto)
    #print(objecto.porcentaje_numeros(text))
    #print(objecto.parecido_palabra_reservada(text) )
    #objecto.analizar(texto)
    #print(objecto.minusculas_todas(text))
    #print(m.isalnum())
    print(objecto.tabla_tokens)
    

    
