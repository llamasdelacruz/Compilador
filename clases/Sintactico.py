from Lista_Personalizada import Lista_p
from String_Personalizado import String_p
class Sintactico():
    
    def __init__(self):

        self.parseo = {
            "estado": "n",
            "apuntador": 1,
            "pila":Lista_p([],"pila"),
            "sentencia_actual": Lista_p([Lista_p(["#"],"numeral")],"sentencia_actual"),
            "lista_own":{}
        }
         
        """self.gramatica = {

            "programa":[["START","sentencias","END"]],
            "sentencias":["declaraVar","comentario","mensajePantalla","asignacion","operacion","obtenerDatosPantalla",
                          ["declaraVar","sentencias"],["comentario","sentencias"],["mensajePantalla","sentencias"],
                           ["asignacion","sentencias"],["operacion","sentencias"],["obtenerDatosPantalla","sentencias"]
                           ],

            "declaraVar":[["tipoDato","nomVar",";"],
                          ["tipoDato","nomVar",",","nomVar",";"]
                          ],
            
            "tipoDato":["INT","FLOAT","BOOLEAN","STRING","CHAR"],

            "asignacion":[["nomVar","=","nomVar",";"],
                          ["nomVar","=","numeros",";"],
                          ["nomVar","=","operacion",";"],
                          ["nomVar","=","TRUE",";"],
                          ["nomVar","=","FALSE",";"]
                         ],

            "operacion":[["nomVar","operadores","nomVar",";"],
                         ["nomVar","operadores","numeros",";"],
                         ["numeros","operadores","numeros",";"],
                         ["numeros","operadores","nomVar",";"]
                         ],

            "operdores":["+","-","*","/"],

            "numeros":[1],

            "nomVar":[1],

            "comentario":["#","mensaje"],

            "mensajePantalla":[["OUTPUT","'","mensaje","'",";"],
                               ["OUTPUT","'","mensaje","'",",","nomVar",";"]
                               ],

            "obtenerDatosPantalla":["INPUT","nomVar",";"],

            "mensaje":[1]
            
        }"""


        #self.cadena = ["START", "INT","$n",",","$I", ";", "END","#"]
        self.gramatica = {
            "S":[["a","A","d"], 
                 ["a","B"]
                 ],
            "A":["c","d"],
            "B":[["c","c","d"],
                 ["d","d","c"]
                 ]          
        }
        self.cadena = ["a","d","d","c","#"]


    def analizar(self):
        # realiza el analisis

        self.parseo = {
            "estado": "n",
            "apuntador": 0,
            "pila":[],
            "sentencia": Lista_p([Lista_p(["#"],"numeral","sentencia")],"sentencia_actual")
        }
        self.parseo["sentencia"].append_start(Lista_p(["S"],"S" + str(self.parseo["apuntador"]),"pila"))
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

                elif(elemento == self.cadena[self.parseo["apuntador"]] and elemento != "#"):

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
                

                elif(elemento == self.cadena[self.parseo["apuntador"]] and elemento == "#"):

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

                    elif(alternativa_elemento >= cantidad_alternativas_elemento and key_elemento == "S"):
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
                                    key_elemento,"caja",nombre_padre_elemento
                                )
                            )

    

            print(self.parseo["estado"],(self.parseo["apuntador"]+1),self.parseo["pila"],self.parseo["sentencia"])

            apuntador +=1
        

   

if __name__ == "__main__":
    objecto = Sintactico()
    objecto.analizar()
  
   