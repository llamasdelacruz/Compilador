
from difflib import SequenceMatcher
class Lexico():

    def __init__(self):
        self.tabla_tokens = {}
        self.reservadas_minusculas = ["int","float","char","string","boolean","output","input","start","end"]
       
    
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

        return linea_nueva
    
        
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

        for linea in lineas:
            palabras_linea = linea.split() # todas las palabras
            abertura = 0
            cierre = 0
            cantidad_elementos = len(palabras_linea)

            for i in range(0,cantidad_elementos):
                palabra = palabras_linea[i]

                palabra = self.quitar_caracteres(palabra)

                #vemos si es un comentario
                if("#" == palabra or palabra[0] == "#"):
                    #print("No se analiza es un comentario:"+ palabra)
                    self.agregar_tokens("#","Caracter",lineas.index(linea)+1)
                    break
                #vemos si es texto 
                elif("'" == palabra or palabra[0] == "'" or palabra[-1] == "'"):
                    
                    self.agregar_tokens("'","Caracter",lineas.index(linea)+1)
                    
                    if(("'" == palabra and abertura == 0) or (palabra[0] == "'" and abertura == 0) ):
                        #print("inicio de string:",palabra)
                        abertura = 1
                    elif(("'" == palabra and cierre == 0) or (palabra[-1] == "'" and cierre == 0)):
                        cierre = 1

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
                        self.agregar_tokens(palabra,"Operador",lineas.index(linea)+1)
                    else:
                        errores += "\n Error de léxico !!!!! En operador"

                # para evaluar los caracteres validos
                elif((palabra == "," and palabra.count(",") == len(palabra)) or 
                     (palabra == ";" and palabra.count(";") == len(palabra))):
                    
                    self.agregar_tokens(palabra[0],"Caracter",lineas.index(linea)+1)

                #checa si  una palabra reservada
                elif( palabra.isupper() or palabra.isalpha() or self.es_palabra_reservada_minusculas(palabra)):
                    
                    # vemos si hay otro elemento adelante de el
                    if(palabra[:3] == "$V@" or palabra[:3] == "$v@"):
                        if((i+1) <= (cantidad_elementos-1)):
                            # vemos si el siguiente elemento es un operador
                            if( palabras_linea[i+1] == "+" or palabras_linea[i+1].count("+") == len(palabras_linea[i+1]) or 
                                palabras_linea[i+1] == "-" or palabras_linea[i+1].count("-") == len(palabras_linea[i+1]) or 
                                palabras_linea[i+1] == "*" or palabras_linea[i+1].count("*") == len(palabras_linea[i+1]) or
                                palabras_linea[i+1] == "=" or palabras_linea[i+1].count("=") == len(palabras_linea[i+1]) or
                                palabras_linea[i+1] == "/" or palabras_linea[i+1].count("/") == len(palabras_linea[i+1])):
                                
                              
                                despues = palabra[3:]

                                if(despues.isdigit()):
                                    self.agregar_tokens(palabra,"Identificador",lineas.index(linea)+1)
                                else:
                                    errores += "\n Error de léxico !!!!! En variable"

                                print("es una variable:", palabra)
                            else:
                                if(i == 0):
                                    
                                    if(self.comprobar_palabras_reservadas(palabra)):
                                        self.agregar_tokens(palabra,"Palabra reservada",lineas.index(linea)+1)
                                    else:
                                        errores += "\n Error de léxico !!!!! En palabra reservada"
                                        
                                    print("Es una palabra reservada:",palabra)

                                else:
                                    despues = palabra[3:]
                                    if(despues.isdigit()):
                                        self.agregar_tokens(palabra,"Identificador",lineas.index(linea)+1)
                                    else:
                                        errores += "\n Error de léxico !!!!! En variable"
                                        print('Error de variable:',palabra)
                                    print("es una variable:", palabra)
                        else:

                            if(self.comprobar_palabras_reservadas(palabra)):
                                self.agregar_tokens(palabra,"Palabra reservada",lineas.index(linea)+1)
                            else:

                                errores += "\n Error de léxico !!!!! En palabra reservada"
                                print('Error de palabra reservada:',palabra)
                            print("Es una palabra reservada:",palabra)
                            
                    else:
                        if(self.comprobar_palabras_reservadas(palabra)):
                            self.agregar_tokens(palabra,"Palabra reservada",lineas.index(linea)+1)
                        else:
                            errores += "\n Error de léxico !!!!! En palabra reservada"
                            print('Error de palabra reservada:',palabra)

                        print("Es una palabra reservada:",palabra)    

                #checa si es un numero 
                elif( palabra.isnumeric()  or 
                     (palabra[0].isdigit() and self.porcentaje_numeros(palabra))
                     or (palabra[0] == "." and self.porcentaje_numeros(palabra))):
                
                    if(palabra.isdigit() or self.decimales(palabra)):
                        print("Numero valido")
                        self.agregar_tokens(palabra,"Caracter",lineas.index(linea)+1)
                    else:
                        errores += "\n Error de léxico !!!!! En número incorrecto"
                        print('Error de numero:',palabra)
                    
                #checa que sea una variable
                elif( palabra[:3] == "$v@" or palabra[:3] == "$V@"):
                    despues = palabra[3:]
                    if(despues.isdigit()):

                        self.agregar_tokens(palabra,"Identificador",lineas.index(linea)+1)
                    else:
                        errores += "\n Error de léxico !!!!! En variable"
                        print("Error de variable:", palabra) 
                    
                    print("es una variable:", palabra) 

                else:
                    if(len(palabra) == 1):
                        print("Caracter incorrecto",palabra)
                        errores += "\n Error de léxico !!!!! En caracter invalido"
                    else:
                        errores += "\n Error de léxico !!!!! Cadena incorrecta de caracteres"
                        print("Cadena incorrecta de caracteres:",palabra)

        return errores


    def es_palabra_reservada_minusculas(self,cadena):
        # ve si es una palabra reservada en minisculas y si lo es manda true
        cadena = cadena.lower()
        if(cadena[:3] == "$v@" or cadena[:3] == "$V@"):
            cadena = cadena[3:]

        is_true = False
        for i in self.reservadas_minusculas:
        
            if(cadena == i):
                is_true = True
                break

        return is_true



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
            
    def parecido_palabra_reservada(self,cadena):
        # que tan parecida es la cadena a una palabra reservada
        
        cadena = cadena.lower()
        if(cadena[:3] == "$v@" or cadena[:3] == "$V@"):
            cadena = cadena[3:]

        parecido_mas_grande = 0
        for i in self.reservadas_minusculas:

            concidencia = SequenceMatcher(None, i, cadena).ratio()
            if(concidencia > parecido_mas_grande):
                parecido_mas_grande  = concidencia
                break
        print(cadena,concidencia)
        if(parecido_mas_grande >= 0.50):
            return True
        else:
            return False
        
    def quitar_caracteres(self,cadena):

        if(cadena[-1] == ","):
            cadena = cadena[:-1]
        elif(cadena[-1] == ";"):
            cadena = cadena[:-1]

        return cadena
    
    def decimales(self,cadena):

        punto = 0
        bandera = True
        for i in range(len(cadena)):
         

            if(cadena[i].isdigit() == False and cadena[i] != "."):
                bandera = False
                break

            if(cadena[i] == '.' and i == 0):
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
            





if __name__ == "__main__":
    objecto = Lexico()
    
    
    texto = "StarT12"
    
    objecto.analizar(texto)
  
    #print(m.isalnum())
    #print(objecto.tabla_tokens)
    

    
