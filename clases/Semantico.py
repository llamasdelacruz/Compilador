from clases.Lista_Personalizada import Lista_p
from clases.String_Personalizado import String_p
import graphviz
class Semantico():

    def __init__(self) -> None:

        self.tabla = {
            "tipo":[],
            "nombre":[],
            "valor":[]
        }

        self.pila = []

    
        
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
        
    def agregar_variable(self,tipo,nombre,valor):

        self.tabla["tipo"].append(tipo)
        self.tabla["nombre"].append(nombre)
        self.tabla["valor"].append(valor)


    def modificar_valor_variable(self,nombre,valor):
        indice = self.tabla["nombre"].index(nombre)
        self.tabla["valor"][indice] = valor

    def buscar_variable_existe(self,nombre):
        
        if(nombre in self.tabla["nombre"]):
            return True
        else:
            return False
        

    def buscar_tipo_variable(self,nombre):
        indice = self.tabla["nombre"].index(nombre)
        return self.tabla["tipo"][indice]
    

    def buscar_valor_variable(self,nombre):
        indice = self.tabla["nombre"].index(nombre)
        return self.tabla["valor"][indice]

        
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
                            self.agregar_variable(tipo,palabra,[numero_linea,"declarada"])
                        else:
                            errores += "Error en la linea "+str(numero_linea)+" en la variable "+palabra+", variable duplicada\n"
                
                    else:
                        if(self.buscar_variable_existe(palabra) and palabras_linea[i+1] == "="):
                            # aqui se ve que la variable que se  usa ya esta declarada y veremos si el relleno coinncidden


                            tipo_variable = self.buscar_tipo_variable(palabra)
                            pre_relleno = palabras_linea[i+2:]
                            
                            relleno = []
                            for j in pre_relleno:
                                relleno.append(j)
                                if(j == ";"):
                                    break
                               
                            #antes de procesar el relleno vemos si hay una variable que no esta declarada de ser asi
                            # no analizamos el tipo de los numeros y variables que hay en el relleno
                            bandera = True
                            for k in relleno:

                                if(k[0] == "$"):
                                    if(self.buscar_variable_existe(k) == False):
                                        bandera = False
                                        break
                    
                            if(bandera):
                                # si todas las variables del relleno existen entonces seguimos analizando

                                if(self.comprobar_relleno_del_mismo_tipo(tipo_variable,relleno) == False):
                                    errores += "Error en la linea "+str(numero_linea)+" operandos incompatibles \n"
                                else:
                                  
                                    if(len(relleno) == 2):
                                        # si solo es asignacion se agrega el valor 
                                        valor = ""
                                        if(tipo_variable == "INT"):
                                            valor = int(relleno[0])
                                        elif(tipo_variable == "FLOAT"):
                                            valor = float(relleno[0])
                                        elif(tipo_variable == "BOOLEAN"):
                                            valor = True
                                            if(relleno[0] == "FALSE"):
                                                valor = False
                                        else:
                                            valor = relleno[0]
                                        

                                        self.modificar_valor_variable(palabra,[numero_linea,valor])

                                    else:
                                        self.modificar_valor_variable(palabra,[numero_linea,"operacion"])

                        elif(self.buscar_variable_existe(palabra) == False):
                            # aqui se ve que la variable que se  usa ya esta declarada
                            errores += "Error en la linea "+str(numero_linea)+" variable " + str(palabra) + " identificador no definido \n"
               
                i+= 1
        
        return errores
    
    def buscar_operaciones(self):
        # este metodo busca las variables que contenga una operacion aritmentica y las guarda en una lista para 
        # despues procesarlas y hacer el arbol

        length = len(self.pila)
        contador = 0
        numero_arbol = 0
        lista_operaciones = []
        lista_temp = []
        hayoperacion = False

        while(contador < length):

            
            elemento = self.pila[contador]


            if(type(elemento) is Lista_p):
                # si es una lista entonces vemos si es asignacion 2  y hacemos el arbol

                if(elemento[0] == "asignacion" and elemento[1] == 2):
                    numero_arbol += 1
                    lista_temp.append("arbol"+str(numero_arbol))
                    lista_temp.append(elemento)
                    hayoperacion = True

                elif(hayoperacion):
                    lista_temp.append(elemento)

            elif(type(elemento) is String_p):

                if(hayoperacion):
                    lista_temp.append(elemento)
                    if(elemento == ";"):
                        hayoperacion = False
                        lista_operaciones.append(lista_temp)
                        lista_temp = []
                    
                    

                

            contador += 1


        return lista_operaciones

        

    def evaluar_operaciones_prioridad(self,lista_operaciones):
        # a cada nodo padre le da el valor de la operacion y a los hijos les da el valor de la variable
  
        for i in range(0, len(lista_operaciones)):

         
            variable_anterior = ""
            largo = len(lista_operaciones[i])-2
            temp = Lista_p([],"temp")

            # nombre de la variable a la que se le asigna el resultado de la operacion

            for j in range(largo,-1,-1):

             
                if(type(lista_operaciones[i][j]) is String_p):

                    if(lista_operaciones[i][j] == "+" or lista_operaciones[i][j] == "-" or 
                       lista_operaciones[i][j] == "*" or lista_operaciones[i][j] == "/" or 
                       lista_operaciones[i][j] == "=" or lista_operaciones[i][j][0] == "$"):  

                        variable_anterior = lista_operaciones[i][j] 
                             
                    else:
                        if(lista_operaciones[i][j].isdigit()):
                            variable_anterior = int(lista_operaciones[i][j])
                            
                        else:
                            variable_anterior = float(lista_operaciones[i][j])
                            

                    temp.append_start(variable_anterior)

                elif(type(lista_operaciones[i][j]) is Lista_p):

                    if(lista_operaciones[i][j][0] == "operacion"):
                        largo_temp = len(temp)
                        operacion = 0
                        for k in range(0,largo_temp):
                            if(type(temp[k]) is String_p):
                                if(temp[k][0] == "$"):
                                    temp[k] = self.buscar_valor_variable(temp[k])[1]
                        # si viene alguna variable obtenemos su valor para hacer las operaciones
                       
                        if(largo_temp == 3):
                            
                            if(temp[1] == "+"):
                                operacion = temp[0] + temp[2]
                            elif(temp[1] == "-"):
                                operacion = temp[0] - temp[2]
                            elif(temp[1] == "*"):   
                                operacion = temp[0] * temp[2]
                            elif(temp[1] == "/"):
                                operacion = temp[0] / temp[2]

                            temp[0] = operacion

                        elif(largo_temp == 5):

                            # este fragmento de codigo evalua sin prioridad de operadores

                            # for k in range(1,4,2):

                            #     operacion_temp = 0
                            #     print(temp,k)
                            #     if(temp[k] == "*"):
                            #         operacion_temp = temp[k-1] * temp[k+1]
                            #     elif(temp[k] == "/"):
                            #         operacion_temp = temp[k-1] / temp[k+1]
                            #     elif(temp[k] == "+"):
                            #         operacion_temp = temp[k-1] + temp[k+1]
                            #     elif(temp[k] == "-"):
                            #         operacion_temp = temp[k-1] - temp[k+1]

                            #     temp[k+1] = operacion_temp
                            
                            # temp[0] = temp[4]

                            if(temp[1] == "*" or  temp[1] == "/"):
                                inicio = 1
                                fin = 4
                                avance = 2
                            elif(temp[3] == "*" or  temp[3] == "/"):
                                inicio = 3
                                fin = 0
                                avance = -2

                            else:
                                inicio = 1
                                fin = 4
                                avance = 2
                         
                            for k in range(inicio,fin,avance):

                                operacion_temp = 0
                            
                                if(temp[k] == "*"):
                                    operacion_temp = temp[k-1] * temp[k+1]
                                elif(temp[k] == "/"):
                                    operacion_temp = temp[k-1] / temp[k+1]
                                elif(temp[k] == "+"):
                                    operacion_temp = temp[k-1] + temp[k+1]
                                elif(temp[k] == "-"):
                                    operacion_temp = temp[k-1] - temp[k+1]

                                if(inicio == 1):
                                    temp[k+1] = operacion_temp
                                else:
                                    temp[k-1] = operacion_temp
                                
                            if(inicio == 1):
                                # si inicia en el operador 1 avanza y termina en el 4 el resultado
                                # si inicia en e; 3 avanza y termina en el 0 el resultado
                                temp[0] = temp[4]


                        lista_operaciones[i][j].append(temp[0])
                        temp = Lista_p([],"temp")
                        temp.append_start(lista_operaciones[i][j][2])
                    
                    else:
                       
                        lista_operaciones[i][j].append(variable_anterior)

        print(lista_operaciones)
        return lista_operaciones
    
    
    def imprimir_pila(self):

        lista_operaciones = self.buscar_operaciones()
        lista_arboles = self.evaluar_operaciones_prioridad(lista_operaciones)

        length = len(lista_arboles)
        contador = 0

        dot = graphviz.Digraph()
        
        while(contador < length):

            arbol = lista_arboles[contador]
            length_arbol = len(arbol)

            for i in range(1,length_arbol):

                elemento = arbol[i]

                if(type(elemento) is Lista_p):
                    # si es una lista entonces vemos si es asignacion 2  y hacemos el arbol

                    if(elemento[0] == "asignacion"):

                        dot.node(elemento.get_name(),label='<<table border="0" cellborder="0" cellspacing="0"> <tr><td COLSPAN="2">asignacion</td></tr><tr><td COLSPAN="2">Valor</td><td>'+str(arbol[3])+'='+str(arbol[5][2])+';</td></tr></table>>')
                    else:
                        dot.node(elemento.get_name(),label='<<table border="0" cellborder="0" cellspacing="0"> <tr><td COLSPAN="2">'+elemento[0]+'</td></tr><tr><td COLSPAN="2">Valor</td><td>'+str(elemento[2])+'</td></tr></table>>' )
                        dot.edge(elemento.get_name_padre(), elemento.get_name())

                elif(type(elemento) is String_p):

                  
                    dot.node(elemento+str(i)+str(contador), elemento)
                    dot.edge(elemento.get_name_padre(),elemento+str(i)+str(contador))

                    if(elemento == ";"):
                            
                        dot.render('diagramas/'+str(arbol[0]), format='pdf')
                        dot = graphviz.Digraph()

                

            contador += 1







if __name__ == "__main__":
    objecto = Semantico()
    texto = "START \n INT $m , $r ; \n $m = 10 ; \n $r = 11 + $m ; \n END"
    objecto.analizar(texto)
  
    

   