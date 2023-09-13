
class Semantico():

    def __init__(self) -> None:

        self.tabla = {
            "tipo":[],
            "nombre":[]
        }

    
        
    def comprobar_tipo_variable(self,cadena):
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
        else:
            contador_palabras_reservadas=0           
                    
        if (contador_palabras_reservadas>0):
            #print("Es una palabra reservada valida")
            return True
        else:
            #print("No es una palabra reservada valida")     
            return False  
        
    def agregar_variable(self,tipo,nombre):

        self.tabla["tipo"].append(tipo)
        self.tabla["nombre"].append(nombre)

    def buscar_variable_existe(self,nombre):
        
        if(nombre in self.tabla["nombre"]):
            return True
        else:
            return False
        

    def buscar_tipo_variable(self,nombre):
        indice = self.tabla["nombre"].index(nombre)
        return self.tabla["tipo"][indice]

        
    def comprobar_relleno_del_mismo_tipo(self,tipo_variable,relleno):
        bandera = False

        if(tipo_variable == "INT"):
            
            for i in relleno:
                
                if(i == "+" or i == "-"  or i == "/" or i == "*" or i == ";" ):

                    continue

                else:    
                    if(i[0] == "$"):
                        if(self.buscar_tipo_variable(i) == "INT"):
                            bandera = True
                        else:
                            bandera = False
                            break
                    else:
                        if(i.isdigit()):
                            bandera = True
                        else:
                            bandera = False
                            break
                    
        elif(tipo_variable == "FLOAT"):
            
            for i in relleno:
                
                if(i == "+" or i == "-"  or i == "/" or i == "*" or i == ";" ):
                    continue
                else:    
                    if(i[0] == "$"):
                        if(self.buscar_tipo_variable(i) == "FLOAT" or self.buscar_tipo_variable(i) == "INT"):
                            bandera = True
                        else:
                            bandera = False
                            break
                    else:
                        try:
                            float(i)
                            bandera = True
                        except:
                            bandera = False
                            break
                       

        elif(tipo_variable == "CHAR"):
            for i in relleno:
                if(i == ";"):
                    continue
                else:
                    if(i == "+" or i == "-"  or i == "/" or i == "*" ):
                        bandera = False
                        break
                    else:    
                        if(i[0] == "$"):
                            if(self.buscar_tipo_variable(i) == "CHAR"):
                                bandera = True
                            else:
                                bandera = False
                                break
                        else:
                            if(len(i) == 3):
                                bandera = True
                            else:
                                bandera = False
                                break

        elif(tipo_variable == "STRING"):
            for i in relleno:
                if(i == ";"):
                    continue
                else:
                    if(i == "+" or i == "-"  or i == "/" or i == "*" ):
                        bandera = False
                        break
                    else:    
                        if(i[0] == "$"):
                            if(self.buscar_tipo_variable(i) == "STRING"):
                                bandera = True
                            else:
                                bandera = False
                                break
                        else:
                            if(i == "TRUE" or i == "FALSE"):
                                bandera = False
                                break
                            else:
                                try:
                                    float(i)
                                    bandera = False
                                except:
                                    bandera = True
                                    break
                
            
        elif(tipo_variable == "BOOLEAN"):
            for i in relleno:
                if(i == ";"):
                    continue
                else:
                    if(i == "+" or i == "-"  or i == "/" or i == "*" ):
                        bandera = False
                        break
                    else:    
                        if(i[0] == "$"):
                            if(self.buscar_tipo_variable(i) == "BOOLEAN"):
                                bandera = True
                            else:
                                bandera = False
                                break
                        else:
                            if(i == "TRUE" or i == "FALSE"):
                                bandera = True
                            else:
                                bandera = False
                                break
            
       
        return bandera
        


    def analizar(self,texto):
       
        lineas = texto.split("\n")
        errores = ""
        numero_linea = 0


        for linea in lineas:
            palabras_linea = linea.split() # todas las palabras
            cantidad_elementos = len(palabras_linea)
       
            numero_linea += 1
            i = 0
            tipo =  ""
            while(i < cantidad_elementos):
            
                palabra = palabras_linea[i]


                if(self.comprobar_tipo_variable(palabra)):

                    tipo = palabra

                elif(palabra[0] == "$"):


                    if(tipo != ""):
                        # ve si la variable se esta declarando mas de una vez

                        if(self.buscar_variable_existe(palabra) == False):
                            self.agregar_variable(tipo,palabra)
                        else:
                            errores += "Error en la linea "+str(numero_linea)+" en la variable "+palabra+", variable duplicada\n"
                
                    else:
                        if(self.buscar_variable_existe(palabra) and palabras_linea[i+1] == "="):
                            # aqui se ve que la variable que se  usa ya esta declarada y veremos si el relleno coinncidden
                            tipo_variable = self.buscar_tipo_variable(palabra)
                            relleno = palabras_linea[i+2:]
                            if(self.comprobar_relleno_del_mismo_tipo(tipo_variable,relleno) == False):
                                errores += "Error en la linea "+str(numero_linea)+" operandos incompatibles \n"
                            
                        elif(self.buscar_variable_existe(palabra) == False):
                            # aqui se ve que la variable que se  usa ya esta declarada
                            errores += "Error en la linea "+str(numero_linea)+" variable " + str(palabra) + " identificador no definido \n"
               
                i+= 1
                print(palabra)

        print(self.tabla)
        print(errores)




    






if __name__ == "__main__":
    objecto = Semantico()
    texto = "START \n STRING $hola , $a ; \n $hola = 'maeria' ; \n CHAR $j ; \n $j = 'k' ; \n OUTPUT 'Dame un dato entero: ' ; \n INPUT $a ;\n END"
    objecto.analizar(texto)
  
    

   