from clases.Lista_Personalizada import Lista_p
from clases.String_Personalizado import String_p

class Optimizacion():

    def __init__(self):
        self.pila = []

    def convertir_numero(self,numero):
        try:
            num = int(numero)
            return num
        except ValueError:
            num = float(numero)
            return num
        
    def es_numero(self,numero): 
        # esta funcion verifica si el numero es un entero o un flotante
        try:
            float(numero)
            return True
        except ValueError:
            return False
        
    def es_numero_entero(self,numero):
        try:
            int(numero)
            return True
        except ValueError:
            return False
        
    def hay_listas(self,lista):
        bandera = False
    
        for i in lista:
            if(type(i) is list):
                bandera = True
                break

        return bandera
        
    def son_todos_numeros(self,lista):
        largo = len(lista)
        bandera = True
        for i in range(0,largo):
            
            if(lista[i] == "+" or lista[i] == "*" or lista[i] == "/" or lista[i] == "-"):
                continue
            else:
                if(self.es_numero(lista[i]) == False):
                    bandera = False
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


    def jerarquia_operadores(self,lista_numeros):
        # esta funcion crea la jerarquia, por medio de listas, encapsula las multiplicaciones
        # las divisiones, y al final las sumas y restas junto con las multiplicaciones y divisiones
        # crea una especie de arbol, para poder hacer las operaciones con prioridad de operadores
     
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
    


    def buscar_operaciones_asignaciones(self):
        # este metodo busca las variables que sean una asignacion
        # despues las guarda en una lista para procesarlas despues
    
        length = len(self.pila)
        contador = 0
        numero_asignacion = 0
        lista_operaciones = []
        lista_temp = []
        hayoperacion = False

        while(contador < length):

            
            elemento = self.pila[contador]


            if(type(elemento) is Lista_p):
                # si es una lista entonces vemos si es asignacion 2  y hacemos el arbol

                if(elemento[0] == "asignacion" and elemento[1] <= 2):
                    
                    hayoperacion = True
                    numero_asignacion += 1

            elif(type(elemento) is String_p):

                if(hayoperacion):
                   
                    if(elemento == ";"):
                        hayoperacion = False
                        lista_operaciones.append(lista_temp)
                        lista_temp = []

                    else:
                        lista_temp.append(elemento)
                    

            contador += 1

        return lista_operaciones
        
      
    def resolver_operaciones(self,lista_con_signos):

        temp_operandos = []
        temp_operadores = []

        largo = len(lista_con_signos)
        index = 0

        while(index < largo):

            digito = lista_con_signos[index]
            if(self.es_numero(digito)):

                temp_operandos.append(self.convertir_numero(digito))
            else:
                temp_operadores.append(digito)
                if(digito == "}" or digito == "]" or digito == ")"):
                  
                    index_penultimo_operadores = len(temp_operadores) - 2
                    index_ultimo_operandos = len(temp_operandos) - 1

                    operador = temp_operadores[index_penultimo_operadores]

                    primer_numero = temp_operandos[index_ultimo_operandos-1]
                    segundo_numero = temp_operandos[index_ultimo_operandos]
                    

                    resultado = 0

                    if(operador == "+"):
                        resultado = primer_numero + segundo_numero
                    elif(operador == "-"):
                        resultado = primer_numero - segundo_numero
                    elif(operador == "/"):
                        resultado = primer_numero / segundo_numero
                    elif(operador == "*"):
                        resultado = primer_numero * segundo_numero
                    

                    temp_operandos.pop(index_ultimo_operandos)
                    temp_operandos.pop(index_ultimo_operandos-1)

                    # cuando se realiza una operacion, el resultado de esa operacion se guarda, puesto que 
                    # es una evidencia de que se hizo la operacion
                    temp_operandos.append(resultado)

                    
                    temp_operadores.pop(index_penultimo_operadores+1)
                    temp_operadores.pop(index_penultimo_operadores)
                    temp_operadores.pop(index_penultimo_operadores-1)


            
            index += 1

        return str(temp_operandos[0])
    

   

    


    def resolver_operaciones_nulas(self,lista):
        # hace estas operaciones x+0 = x, 1*x = x, x/1 = x

        largo = len(lista)
        i = 1

        while(i < largo):
            
            numero1 = lista[i-1]
            numero2 = lista[i+1]
            operador = lista[i]
            
            
            if(operador == "+" ):
                if(numero1 == "0" and numero2[0] == "$"):
                    # 0+x = x
                    lista.pop(i)
                    lista.pop(i-1)
                    # si llegara a entrar a alguna de las condicionales y elimina
                    # entonces que incie de nuevo
                    i=1

                elif(numero1[0] == "$" and numero2 == "0"):
                    # x+0 = x
                    lista.pop(i+1)
                    lista.pop(i)
                    i=1
                else:
                    i += 2
                    

            elif(operador == "*"):
                if(numero1 == "1" and numero2[0] == "$"):
                    # 1*x = x
                    lista.pop(i)
                    lista.pop(i-1)
                    i=1

                elif(numero1[0] == "$" and numero2 == "1"):
                    # x*1 = x
                    lista.pop(i+1)
                    lista.pop(i)
                    i=1

                else:
                    i += 2
                    
            elif(operador == "/"):
                if(numero1[0] == "$" and numero2 == "1"):
                    # x/1 = x
                    lista.pop(i+1)
                    lista.pop(i)
                    i=1

                elif(numero1 == "1" and numero2[0] == "$"):
                    # 1/x = x
                    lista.pop(i)
                    lista.pop(i-1)
                    i=1
                else:
                    i += 2
            else:
                i += 2
                  
            largo = len(lista)
           

        return lista

    def resolver_operaciones_de_potencia(self,lista):
        # resuelve operaciones como 2*x o x*2


        largo = len(lista)
        i = 1

        while(i < largo):
            
            numero1 = lista[i-1]
            numero2 = lista[i+1]
            operador = lista[i]
            
            if(operador == "*"):
                if(self.es_numero_entero(numero1) and numero2[0] == "$"):
                    # ejemplo 2*x = x + x
                    numero1 = int(numero1)
                    if(numero1 > 0):
                        lista = [numero2,"+"]*numero1
                        lista.pop(len(lista)-1)
                    

                elif(numero1[0] == "$" and self.es_numero_entero(numero2)):
                    # ejemplo x*2 = x + x 
                    numero2 = int(numero2)
                    if(numero2 > 0):
                        lista = [numero1,"+"]*numero2
                        lista.pop(len(lista)-1)
    
            i += 2
          
            largo = len(lista)
           

        return lista

    def precalcular_expresiones_constantes(self, lista_operaciones):
        # esta funcion busca las expresiones constantes y las resuelve
        cantidad = len(lista_operaciones)
      
        for i in range(0, cantidad):
            
            if(len(lista_operaciones[i]) > 3):
               
                # si tiene mas de estos 3 elementos  $variable, = , numero,  eso 
                # significa que es una operacion no una asiganacion
                lista = lista_operaciones[i]
                lista_relleno = lista[2:]
                
                if(self.son_todos_numeros(lista_relleno)):
                    # si son todos numeros lo optimizamos
                    lista_anidada = self.jerarquia_operadores(lista_relleno)
                
                    lista_con_signos = self.jerarquia_con_signos_de_agrupacion(lista_anidada)
                    resultado_operacion  = self.resolver_operaciones(lista_con_signos)
                
                    lista_operaciones[i] = [lista_operaciones[i][0],
                                         "=",
                                         resultado_operacion]
                    
    
                    
        return lista_operaciones
    

      

    def eliminacion_de_secuencias_nulas(self,lista_operaciones):

        cantidad = len(lista_operaciones)
        for i in range(0, cantidad):
         
            if(len(lista_operaciones[i]) > 3):
               
                # si tiene mas de estos 3 elementos $variable, = , numero,  eso 
                # significa que es una operacion no una asiganacion
                lista = lista_operaciones[i]
                lista_relleno = lista[2:]

                
                resultado_operacion  = self.resolver_operaciones_nulas(lista_relleno)
                   
                lista_operaciones[i] = [lista_operaciones[i][0],
                                         "="]
                for strings in resultado_operacion:
                    lista_operaciones[i].append(strings)
                    

                    
        return lista_operaciones


    def reduccion_de_potencias(self, lista_operaciones):
        
        cantidad = len(lista_operaciones)
        for i in range(0, cantidad):
         
            if(len(lista_operaciones[i]) == 5):
               
                # si tiene mas de estos 3 elementos $variable, = , numero,  eso 
                # significa que es una operacion no una asiganacion
                lista = lista_operaciones[i]
                lista_relleno = lista[2:]
                
                resultado_operacion  = self.resolver_operaciones_de_potencia(lista_relleno)
            
                lista_operaciones[i] = [lista_operaciones[i][0],
                                         "="]
                for strings in resultado_operacion:
                    lista_operaciones[i].append(strings)
      
                    
        return lista_operaciones
    
    def propagacion_de_copias(self,lista_operaciones):


        cantidad = len(lista_operaciones)
        i = 0
        while(i < cantidad):

            lista = lista_operaciones[i]
           
            if(len(lista) == 3 and lista[2][0] == "$"):
                # que es $f = $a
                variable_anterior = lista[0]
                variable_nueva = lista[2]
                j = i+1
                cantidad_operaciones = len(lista_operaciones)
                hay_propagacion = False

                if(j < cantidad_operaciones):
                    while(j<cantidad_operaciones):
                        largo = len(lista_operaciones[j])
                        for index in range(2,largo):

                            if(lista_operaciones[j][index] == variable_anterior):
                                hay_propagacion = True
                                lista_operaciones[j][index] = variable_nueva
                        j+=1
                    if(hay_propagacion):
                        lista_operaciones.pop(i)
                    i = 0
                else:
                    i+=1
            else:   

                i += 1

            cantidad = len(lista_operaciones)
                    
        return lista_operaciones
        
    def unir_listas(self,listas):
        resultado = ""
        for lista in listas:
            for elemento in lista:
                resultado += str(elemento) + " "
            resultado += ";\n"
        return resultado

    def analizar(self):
        # hace las cuatro optimizaciones y manda los resusltados
        lista_operaciones = self.buscar_operaciones_asignaciones()
       
        lista_optimizada1 = self.precalcular_expresiones_constantes(lista_operaciones)
        op1 = self.unir_listas(lista_optimizada1)
        lista_optimizada2 = self.eliminacion_de_secuencias_nulas(lista_optimizada1)
        op2 = self.unir_listas(lista_optimizada2)
        lista_optimizada3 = self.reduccion_de_potencias(lista_optimizada2)
        op3 = self.unir_listas(lista_optimizada3)
        lista_optimizada4 = self.propagacion_de_copias(lista_optimizada3)
        op4 = self.unir_listas(lista_optimizada4)
        
    
        return [op1,op2,op3,op4]




if __name__ == "__main__":
    objecto = Optimizacion()
    m = [1,"$a","=","12", "-", "9"]
    objecto.son_todos_numeros(m)
    
  
    

   
