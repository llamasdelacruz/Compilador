from Lista_Personalizada import Lista_p
from String_Personalizado import String_p
class Sintactico():
    
    def __init__(self):

        self.parseo = {
            "estado": "n",
            "apuntador": 0,
            "pila":[],
            "sentencia": Lista_p([Lista_p(["#"],"numeral","sentencia")],"sentencia_actual")
        }
         
        self.gramatica = {

            "programa": [["START","sentencias","END"]],
            "sentencias":[["declaraVar"],
                          ["declaraVar","sentencias"],
                          ["comentario"],
                          ["comentario","sentencias"],
                          ["asignacion"],
                          ["asignacion","sentencias"],
                          ["operacion"],
                          ["operacion","sentencias"],
                          ["mensajePantalla"],
                          ["mensajePantalla","sentencias"],
                          ["obtenerDato"],
                          ["obtenerDato","sentenias"]
                          ],
            "declaraVar":[
                            ["tipoDato","nomVar",";"],
                            ["tipoDato","nomVar",",","nomVar",";"]
                        ],
            "tipoDato":[["INT"],["FLOAT"],["BOOLEAN"],["STRING"],["CHAR"]],
            "asignacion":[
                            ["nomVar","=","nomVar",";"],
                            ["nomVar","=","numero",";"],
                            ["nomVar","=","operacion",";"],
                            ["nomVar","=","TRUE",";"],
                            ["nomVar","=","FALSE",";"]
                          ],

            "operacion":[
                        ["nomVar","operadores","nomVar",";"],
                        ["nomVar","operadores","numeros",";"],
                        ["numeros","operadores","numeros",";"],
                        ["numeros","operadores","nomVar",";"]
                         ],

            "operadores":[["+"],["-"],["*"],["/"]],

            "mensajePantalla":[
                            ["OUTPUT","'","msj","'",";"],
                            ["OUTPUT","'","msj","'",",","nomVar",";"]
                        ],
            
            "comentario": [
                           ["#","msj"],
                           ["#"]
                           ],
            "obtenerDato":[["INPUT","nomVar",";"]],

            "nomVar":[["$l"]]        
        }

        self.cadena = []
        """self.gramatica = {
            "S":[["a","A","d"], 
                 ["a","B"]
                 ],
            "A":["c","d"],
            "B":[["c","c","d"],
                 ["d","d","c"]
                 ]          
        }
        self.cadena = ["a","d","d","c","#"]"""

    def analizar(self):
        # realiza el analisis

        self.parseo = {
            "estado": "n",
            "apuntador": 0,
            "pila":[],
            "sentencia": Lista_p([Lista_p(["#"],"numeral","sentencia")],"sentencia_actual")
        }
        self.parseo["sentencia"].append_start(Lista_p(["programa"],"programa" + str(self.parseo["apuntador"]),"pila"))
        print(self.parseo["estado"],(self.parseo["apuntador"]+1),self.parseo["pila"],self.parseo["sentencia"])
        cadena_len = len(self.cadena)
        apuntador = 0
    
        while(apuntador < cadena_len):
            print( str(apuntador+2),"##################################################################")
            if(self.parseo["estado"] == "n"):

                
                elemento = self.parseo["sentencia"][0][0]
                nombre_padre = self.parseo["sentencia"][0].get_name_padre()
            
                
                if(elemento in self.gramatica):
                    # expansion del arbol 1
                    print("expansion del arbol 1")
                    if(self.parseo["sentencia"][0][-1] == elemento):

                        self.parseo["sentencia"].remove_start()
                    else:
                        self.parseo["sentencia"][0].remove_start()

                    nombre_elemento = elemento + str(0)
                    self.parseo["pila"].append(Lista_p([elemento,0],nombre_elemento,nombre_padre))

                    self.parseo["sentencia"].append_start(
                        Lista_p(
                                self.gramatica[elemento][0],"caja",nombre_elemento
                            )
                        )

                elif(elemento == self.cadena[self.parseo["apuntador"]] and nombre_padre != "sentencia" ):

                    # concordancioa de un simbolo 2
                    print("concordancia de un simbolo 2")
                    if(self.parseo["sentencia"][0][-1] == elemento):

                        self.parseo["sentencia"].remove_start()
                    else:
                        self.parseo["sentencia"][0].remove_start()

                    string_elemento = String_p(elemento)
                    string_elemento.set_name_padre(nombre_padre)

                    self.parseo["pila"].append(string_elemento)
                    self.parseo["apuntador"] = self.parseo["apuntador"]+1
                

                elif(elemento == self.cadena[self.parseo["apuntador"]] and elemento == "#" and nombre_padre == "sentencia" ):

                    # terminacion con exito 3
                    print("terminacion con exito 3")
                    if(self.parseo["sentencia"][0][-1] == elemento):

                        self.parseo["sentencia"].remove_start()
                    else:
                        self.parseo["sentencia"][0].remove_start()

                    self.parseo["estado"] = "t"
                    self.parseo["apuntador"] = self.parseo["apuntador"]+1
                    self.parseo["sentencia"].append_start([""])

                    print(self.parseo["estado"],(self.parseo["apuntador"]+1),self.parseo["pila"],self.parseo["sentencia"])
                    break
                elif(elemento != self.cadena[self.parseo["apuntador"]]):
                    # no concordancia de un simbolo 4
                    print("NO!!!! concordancia de un simbolo 4")
                    self.parseo["estado"] = "r"
                    
            else:
                elemento = self.parseo["pila"][-1]
                # el nombre de la lista padre de la primera lista en sentencias
                nombre_padre_caja = self.parseo["sentencia"][0].get_name_padre()

                if(type(elemento) is String_p):

                    # retroceso a la entrada 5
                    print("retroceso a la entrada 5")
                    nombre_padre_elemento = self.parseo["pila"][-1].get_name_padre()
                    
                    self.parseo["pila"].pop()

                    if(nombre_padre_caja == nombre_padre_elemento):
                      
                        self.parseo["sentencia"][0].append_start(str(elemento))

                    else:

                        caja_nueva = Lista_p(
                                [str(elemento)],"caja",nombre_padre_elemento
                            )
                        self.parseo["sentencia"].append_start(caja_nueva)

                    self.parseo["apuntador"] = self.parseo["apuntador"]-1


                else:
                    # siguiente alternativa 6
                    print("siguiente alternativa 6")
                    key_elemento = elemento[0]
                    nombre_elemento_caja_old = elemento.get_name()
                    nombre_padre_elemento = elemento.get_name_padre()
                    alternativa_elemento = elemento[1]+1
                    nombre_elemento_caja_new = key_elemento + str(alternativa_elemento)
                    
                    cantidad_alternativas_elemento = len(self.gramatica[key_elemento])

                    if(alternativa_elemento < cantidad_alternativas_elemento):
                        # si es que hay otra alternativa 6a
                        print("si es que hay otra alternativa 6a")
                        # cambia el el nombre de la caja del elemeto
                        self.parseo["pila"][-1].set_name(nombre_elemento_caja_new)
                        # le suma uno a la alternativa
                        self.parseo["pila"][-1][1] = alternativa_elemento

                        if(nombre_padre_caja == nombre_elemento_caja_old):

                            self.parseo["sentencia"].remove_start()

                        self.parseo["sentencia"].append_start(
                            Lista_p(
                                    self.gramatica[key_elemento][alternativa_elemento],"caja",nombre_elemento_caja_new
                                )
                        )
                        
                        
                        self.parseo["estado"] = "n"

                    elif(alternativa_elemento >= cantidad_alternativas_elemento and key_elemento == "programa"):
                        # cuando no hay otra alternativa 6b
                        print("cuando no hay otra alternativa 6b")
                        print("la cadena no se acepta")
                        self.parseo["estado"] = "e"
                        print(self.parseo["estado"],(self.parseo["apuntador"]+1),self.parseo["pila"],self.parseo["sentencia"])
                        break
                    else:
                        # retroceso a la entrada 6c
                        print("retroceso a la entrada 6c")
                        self.parseo["pila"].pop()

                        if(nombre_padre_caja == nombre_elemento_caja_old):

                            self.parseo["sentencia"].remove_start()

                        siguiente_elemento_name = self.parseo["sentencia"][0].get_name_padre()

                        if(nombre_padre_elemento == siguiente_elemento_name):
                            self.parseo["sentencia"][0].append_start(key_elemento)
                        else:
                            self.parseo["sentencia"].append_start(
                            Lista_p(
                                    [key_elemento],"caja",nombre_padre_elemento
                                )
                            )

    

            print(self.parseo["estado"],(self.parseo["apuntador"]+1),self.parseo["pila"],self.parseo["sentencia"])

            apuntador = self.parseo["apuntador"]
        
    def establecer_cadena(self,texto):
        # crea la cadena que se va a utilizar en el retroceso
        self.cadena = []
        lineas = texto.split("\n")
        for linea in lineas:
            
            palabras_linea = linea.split() # todas las palabras
            abertura = False
            
            cantidad_elementos = len(palabras_linea)

            for i in range(0,cantidad_elementos):
                palabra = palabras_linea[i]

                if(abertura):
                    
                    if(palabra == "'"):
                        abertura = False
                        self.cadena.append("'")

                    elif(palabra[len(palabra)-2] != "'" and palabra[-1] == "'"):
                        # significa que la cadena no es esta m'' si no esta m' y esa si puede cerrar 
                        abertura = False
                        self.cadena.append("'")
                else:
                    # ver sin es un comentario con msj
                    if("#" == palabra or palabra[0] == "#"):

                        if(palabra == "#" and cantidad_elementos > i+1):
                            self.cadena.append("#")
                            self.cadena.append("msj")
                        elif(palabra[0] == "#" and palabra != "#"):
                            self.cadena.append("#")
                            self.cadena.append("msj")
                        else:
                            self.cadena.append("#")
                        break
                        
                    elif(palabra[0] == "'" and palabra[-1] == "'" and len(palabra) > 1 ):
                        # significa que es una sola palabra como 'hola'
                        self.cadena.append("'")
                        self.cadena.append("msj")
                        self.cadena.append("'")

                    elif((palabra[0] == "'" and len(palabra)>1)):
                        self.cadena.append("'")
                        self.cadena.append("msj")
                        abertura = True

                    elif(palabra == "'"):
                        self.cadena.append(palabra)
                        self.cadena.append("msj")
                        abertura = True

                    else:
                        
                        self.cadena.append(palabra)
                

               

        self.cadena.append("#")
        print(self.cadena)
       

   

if __name__ == "__main__":
    texto = " START #n \n  INT $l ; \n END" 
    objecto = Sintactico()
    objecto.establecer_cadena(texto)
    objecto.analizar()
  
   