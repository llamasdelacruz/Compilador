
class Codigo_intermedio():

   
    def es_numero(self,numero): 
        # esta funcion verifica si el numero es un entero o un flotante
        try:
            float(numero)
            return True
        except ValueError:
            return False
                       
    def jerarquia_operadores(self,cadena):
        # esta funcion crea la jerarquia, por medio de listas, encapsula las multiplicaciones
        # las divisiones, y al final las sumas y restas junto con las multiplicaciones y divisiones
        # crea una especie de arbol, para poder hacer las operaciones con prioridad de operadores

        lista_numeros = cadena.split(" ")
     
        parada = len(lista_numeros)
        index = 0
        segunda_vuelta = False


        while(parada != 1):

        
            # si el index es menor a la parada, es porque aun hay elementos en la lista
            caracter = lista_numeros[index]
            if(segunda_vuelta):
                if(caracter == "+" or caracter == "-"):
                    # si el elemento es + o -, se encapsula
                    lista_temp = [lista_numeros[index-1], lista_numeros[index], lista_numeros[index+1]]
                    lista_numeros[index] = lista_temp
                    lista_numeros.pop(index+1)
                    lista_numeros.pop(index-1)

                    index -= 1
                  
                
            else:

                if(caracter == "*" or caracter == "/"):
                    # si el elemento es * o /, se encapsula
                    lista_temp = [lista_numeros[index-1], lista_numeros[index], lista_numeros[index+1]]
                    lista_numeros[index] = lista_temp
                    lista_numeros.pop(index+1)
                    lista_numeros.pop(index-1)

                    index -= 1
                   
           
            index += 1

            parada = len(lista_numeros)

            if(index == parada):

                index = 0
                segunda_vuelta = True

        return lista_numeros
    
    def hay_listas(self,lista):
        bandera = False
    
        for i in lista:
            if(type(i) is list):
                bandera = True
                break

        return bandera
    

    def jerarquia_con_signos_de_agrupacion(self,lista):
        # esta funcion coloca los  corchetes, parentesis y llaves, en una sola lista, sin listas anidadas
        index = 0
        parada = len(lista)
        abertura = "("
        cierre = ")"
        while(True):

            if(self.hay_listas(lista)):

                if(index < parada):

                    chunk = lista[index]


                    if(type(chunk) is list):

                        if(abertura == "("):
                            abertura = "{"
                            cierre = "}"

                        elif(abertura == "{"):
                            abertura = "["
                            cierre = "]"

                        elif(abertura == "["):
                            abertura = "("
                            cierre = ")"
                        
                        lista.pop(index)

                        lista.insert(index,abertura)
                        lista.insert(index+1,cierre)
                        
                        for i in chunk:

                            index +=1
                            lista.insert(index,i)
          
                else:
                    index = -1
                    
            else:
                break

           
            index += 1

            parada = len(lista)

        return lista

    def notacion_polaca(self,cadena):

        variable = cadena.split(" ")
        cadena_operaciones = " ".join(variable[2:])

        lista_anidada = self.jerarquia_operadores(cadena_operaciones)
        lista_con_signos = self.jerarquia_con_signos_de_agrupacion(lista_anidada)

        pilas = variable[0]+"="+" ".join(lista_con_signos) + "\n"
        temp_operandos = [variable[0]]
        temp_operadores = ["="]

        largo = len(lista_con_signos)
        index = 0

        resultado_pila = ""
        

        while(index < largo):

            digito = lista_con_signos[index]
            if(self.es_numero(digito) or digito[0] == "$"):
                temp_operandos.append(digito)
            else:
                temp_operadores.append(digito)
                if(digito == "}" or digito == "]" or digito == ")"):

                    index_penultimo = len(temp_operadores) - 2
                    
                    # este saca todo lo de la pila
                    #pila_alreves = [temp_operandos[i] for i in range(len(temp_operandos)-1,-1,-1)]
                    #este saca solo dos
                    index_ultimo = len(temp_operandos) - 1
                    if(index_ultimo > 0):
                        pila_alreves = [temp_operandos[index_ultimo], temp_operandos[index_ultimo-1]]
                    elif(index_ultimo == 0):
                        pila_alreves = [temp_operandos[index_ultimo]]
                    
                    resultado_pila += " ".join(pila_alreves)
                    resultado_pila += temp_operadores[index_penultimo]

                    # copia_pilas = [temp_operandos.copy(),temp_operadores.copy(),resultado_pila]

                    # este imprime la pila como una pila en vertical
                    operandos_alreves = (temp_operandos.copy())
                    operadores_alreves = (temp_operadores.copy())
                    operadores_alreves.reverse()
                    operandos_alreves.reverse()

                   
                    string_operandos =  "\n".join(str(operandos_alreves).split(","))
                    string_operadores = "\n".join(str(operadores_alreves).split(","))

                    
                    
                    pilas += " \n" +string_operandos + " \n\n" + string_operadores + " \n" + resultado_pila + "\n\n"
                    # --------------------------------------------------------------------------------------------
                    # print(temp_operandos)
                    # print(temp_operadores)
                    # print(resultado_pila)
                    # saca todos los operandos 
                    # temp_operandos = []
                    # saca solo dos
                    if(index_ultimo > 0):
                        temp_operandos.pop(index_ultimo)
                        temp_operandos.pop(index_ultimo-1)
                    elif(index_ultimo == 0):
                        
                        temp_operandos.pop(index_ultimo)
                   #--------------------------------------------------------------------------------------------------

                    temp_operadores.pop(index_penultimo+1)
                    temp_operadores.pop(index_penultimo)
                    temp_operadores.pop(index_penultimo-1)

                    
                    
            index += 1

        #pila_alreves = [temp_operandos[i] for i in range(len(temp_operandos)-1,-1,-1)]
        largo_operandos = len(temp_operandos)
        if( largo_operandos == 1):
            pilas += str(temp_operandos)+ " \n" + str(temp_operadores) + " \n" + resultado_pila +temp_operandos[0] + "=\n"
        elif( largo_operandos == 2):
            pilas += str(temp_operandos)+ " \n" + str(temp_operadores) + " \n" + resultado_pila +temp_operandos[0] + temp_operandos[1]  + "=\n"
        else:
            pilas += str(temp_operandos)+ " \n" + str(temp_operadores) + " \n" + resultado_pila + "=\n"

        pilas += "\n ______________________________________________ \n" 
        # pilas.append([temp_operandos,temp_operadores,resultado_pila+" ="])
        # print(temp_operandos)
        # print(temp_operadores)
        # print(resultado_pila+" =")

        return pilas

    def codigo_p(self,cadena):

        variable = cadena.split(" ")
        cadena_operaciones = " ".join(variable[2:])
       

        lista_anidada = self.jerarquia_operadores(cadena_operaciones)
        lista_con_signos = self.jerarquia_con_signos_de_agrupacion(lista_anidada)

        instrucciones = "lda "+variable[0] + ";\n"
        temp_operandos = []
        temp_operadores = []

        largo = len(lista_con_signos)
        index = 0
        id = 0
        while(index < largo):

            digito = lista_con_signos[index]
            if(self.es_numero(digito) or digito[0] == "$"):

                temp_operandos.append(digito)

                if(self.es_numero(digito)):
                    instrucciones += "Idc "+ digito + ";\n"
                else:
                    instrucciones += "lod "+ digito + ";\n"
            else:
                temp_operadores.append(digito)
                if(digito == "}" or digito == "]" or digito == ")"):

                    index_penultimo_operadores = len(temp_operadores) - 2
                    index_ultimo_operandos = len(temp_operandos) - 1

                    operador = temp_operadores[index_penultimo_operadores]

                    if(operador ==  "+"):
                        instrucciones += "adi;\n"
                    elif(operador == "-"):
                        instrucciones += "sbi;\n"
                    elif(operador == "*"):
                        instrucciones += "mpi;\n"
                    elif(operador == "/"):
                        instrucciones += "div;\n"

                    temp_operandos.pop(index_ultimo_operandos)
                    temp_operandos.pop(index_ultimo_operandos-1)

                    # cuando se realiza una operacion, el resultado de esa operacion se guarda con su id, puesto que 
                    # no necesitamos el resultado de la operacion, solo una evidencia de que se hizo la operacion
                    # eso representa con su id, asi se puede tratar como que la operacion utiliza dos operandos y un operador
                    temp_operandos.append(str(id))
                    
                    temp_operadores.pop(index_penultimo_operadores+1)
                    temp_operadores.pop(index_penultimo_operadores)
                    temp_operadores.pop(index_penultimo_operadores-1)


                    id += 1
                    
            index += 1

        instrucciones += "sto;\n \n"
        
        return instrucciones


    def triplos(self,cadena):

        variable = cadena.split(" ")
        cadena_operaciones = " ".join(variable[2:])

        lista_anidada = self.jerarquia_operadores(cadena_operaciones)
        lista_con_signos = self.jerarquia_con_signos_de_agrupacion(lista_anidada)
  

        instrucciones = []
        temp_operandos = []
        temp_operadores = []

        largo = len(lista_con_signos)
        index = 0
        id = 0
        while(index < largo):

            digito = lista_con_signos[index]
            if(self.es_numero(digito) or digito[0] == "$"):

                temp_operandos.append(digito)
            else:
                temp_operadores.append(digito)
                if(digito == "}" or digito == "]" or digito == ")"):

                    index_penultimo_operadores = len(temp_operadores) - 2
                    index_ultimo_operandos = len(temp_operandos) - 1

                    operador = temp_operadores[index_penultimo_operadores]

                    instrucciones.append(["["+str(id)+"]",operador,temp_operandos[index_ultimo_operandos-1],temp_operandos[index_ultimo_operandos]])

                    temp_operandos.pop(index_ultimo_operandos)
                    temp_operandos.pop(index_ultimo_operandos-1)

                    # cuando se realiza una operacion, el resultado de esa operacion se guarda con su id, puesto que 
                    # no necesitamos el resultado de la operacion, solo una evidencia de que se hizo la operacion
                    # eso representa con su id, asi se puede tratar como que la operacion utiliza dos operandos y un operador
                    temp_operandos.append("["+str(id)+"]")
                    
                    temp_operadores.pop(index_penultimo_operadores+1)
                    temp_operadores.pop(index_penultimo_operadores)
                    temp_operadores.pop(index_penultimo_operadores-1)


                    id += 1
                    
            index += 1
        instrucciones.append(["["+str(id)+"]","=",variable[0],temp_operandos[0]])
        

     
        # for i in instrucciones:
           
        #     print("dir "+i[0],"op "+i[1],"n1: "+i[2],"n2: "+i[3])
        return instrucciones

    def cuadruplos(self,cadena):

        variable = cadena.split(" ")
        cadena_operaciones = " ".join(variable[2:])
       

        lista_anidada = self.jerarquia_operadores(cadena_operaciones)
        lista_con_signos = self.jerarquia_con_signos_de_agrupacion(lista_anidada)

        instrucciones = []
        temp_operandos = []
        temp_operadores = []

        largo = len(lista_con_signos)
        index = 0
        id = 1
        while(index < largo):

            digito = lista_con_signos[index]
            if(self.es_numero(digito) or digito[0] == "$"):

                temp_operandos.append(digito)
            else:
                temp_operadores.append(digito)
                if(digito == "}" or digito == "]" or digito == ")"):

                    index_penultimo_operadores = len(temp_operadores) - 2
                    index_ultimo_operandos = len(temp_operandos) - 1

                    operador = temp_operadores[index_penultimo_operadores]

                    instrucciones.append([operador,temp_operandos[index_ultimo_operandos-1],temp_operandos[index_ultimo_operandos],"v"+str(id)])

                    temp_operandos.pop(index_ultimo_operandos)
                    temp_operandos.pop(index_ultimo_operandos-1)

                    # cuando se realiza una operacion, el resultado de esa operacion se guarda como su id, puesto que 
                    # no necesitamos el resultado de la operacion, solo una evidencia de que se hizo la operacion
                    # eso representa con su id, asi se puede tratar como que la operacion utiliza dos operandos y un operador
                    temp_operandos.append("v"+str(id))
                    
                    temp_operadores.pop(index_penultimo_operadores+1)
                    temp_operadores.pop(index_penultimo_operadores)
                    temp_operadores.pop(index_penultimo_operadores-1)


                    id += 1
                    
            index += 1
        instrucciones.append(["=",temp_operandos[0],"-", variable[0]])
        

     
        # for i in instrucciones:
           
        #     print("op "+i[0],"n1: "+i[1],"n2: "+i[2], "Aux "+i[3])
        return instrucciones
   
    def obtener_operaciones(self,texto):
        lineas = texto.split("\n")
        
        operaciones = []
        for linea in lineas:

            nueva = linea.split(";")

            for i in nueva:
                
         
                if(i.strip() != ""):
                    elementos = (i.strip()).split(" ")
                    # le quitamos los espacios en blanco que hay en la lista
                    elementos_nuevos = [i for i in elementos if i != "" and i != " "]
                    
                    if(len(elementos_nuevos) > 3 and elementos_nuevos[1] == "="):
                        cadena_operaciones = " ".join(elementos_nuevos)
                        operaciones.append(cadena_operaciones)

        return operaciones
    
    def analizar(self,texto):
        #genera todo el Codigo_intermedio de esta fase
        operaciones = self.obtener_operaciones(texto)
        notacion_polaca_lista = ""
        codigo_p_lista = ""
        triplos_lista = []
        cuadruplos_lista = []
        filas_triplos = 0
        filas_cuadruplos = 0

        for i in operaciones:
        
            notacion_polaca_lista += self.notacion_polaca(i) + "\n"
            codigo_p_lista += self.codigo_p(i) + "\n"

            lista_tr = self.triplos(i)
            triplos_lista.append(lista_tr)

            lista_cu = self.cuadruplos(i)
            cuadruplos_lista.append(lista_cu)

            filas_triplos += len(lista_tr)+1
            filas_cuadruplos += len(lista_cu)+1

        return [notacion_polaca_lista,codigo_p_lista,triplos_lista,cuadruplos_lista,filas_triplos,filas_cuadruplos]
        #print(notacion_polaca)
        #print(codigo_p)
        #print(triplos)
        #print(cuadruplos)


       

if __name__ == "__main__":
    cadena = "$i = 4 - 8 / 4"
    #l = " START \n OUTPUT ' juan hola ' ; $l = 34 / 4 ; $e = 23 - 3 / 5 ; \n $er = 23 - 3; $m = 12 ; \n END"
    m = Codigo_intermedio()
    #m.analizar(l)
    l = m.notacion_polaca(cadena)
    print(l)
    #m.codigo_p(cadena)
    #m.triplos(cadena)
    #m.cuadruplos(cadena)





