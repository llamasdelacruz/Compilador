
class Lexico():

    def __init__(self):
        self.tabla_tokens = {}

    def comprobar_inicio_fin(self,cadena):
        # nos dice si las palabras de inicio y fin estan bien
        contador_start=0
        contador_fin=0
        if(cadena=="START"):
            contador_start+=1
        elif(cadena=="END"):
            contador_fin+=1
        else:
            contador_fin=0
            contador_start=0        
        
        if(contador_start>0 or contador_fin>0):
            #print("Es una palabra reservada valida")
            return True
        else:
            #print("Error en palabra reservada")
            return False
    
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
            
           
    
    def comprobar_comentarios(self,cadena):
        # si el comentario tiene la #
        contador_comentario=0
        for i in range(len(cadena)):
            if(cadena[0]=="#"):
                contador_comentario+=1
        if(contador_comentario>0):
            return True
        else:
            return False
        
    def comprobar_caracteres(self,cadena):
        #ve si la cadena es un caracter valido
        if(cadena == "'" or cadena == "," or cadena == ";" or cadena == "#"):
            return True
        else:
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
            pass
                
            


if __name__ == "__main__":
    objecto = Lexico()
    #objecto.partir_por_palabras("'alo==2.67893',22++*+- 4.s#3")
    #texto = "INICIO\nInt alo;\nalo = 22 + 3;\noutput alo;\nFIN"
    texto = "  \n INICIO\nInt alo;\nalo=22+3;\n  output alo ;\nFIN"
    #objecto.partir_por_palabras("Input variable ++ START 45 67 90.0")
    cadena=str(input("Dame una cadena por favor : "))
    #objecto.agregar_tokens("cj","operador",2)
    #objecto.agregar_tokens("mara","identificador",4) 
    #objecto.agregar_tokens("mara","identificador",9)
    #objecto.agregar_tokens("mara","identificador",11)
    #objecto.agregar_tokens("cj","operador",10)
    #print(objecto.tabla_tokens)
    #objecto.comprobar_inicio_fin(cadena)
    #print(objecto.comprobar_nombre_variable(cadena))
    #objecto.comprobar_palabras_reservadas(cadena)
    #objecto.comprobar_operadores(cadena)
    #objecto.comprobar_decimales(cadena)
    #objecto.comprobar_comentarios(cadena)


