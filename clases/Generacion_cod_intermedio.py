#from clases.String_Personalizado import String_p
from String_Personalizado import String_p
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
        id = 0
        segunda_vuelta = False


        while(parada != 1):

        
            # si el index es menor a la parada, es porque aun hay elementos en la lista
            caracter = lista_numeros[index]
            if(segunda_vuelta):
                if(caracter == "+" or caracter == "-"):
                    # si el elemento es + o -, se encapsula
                    lista_temp = [id,lista_numeros[index-1], lista_numeros[index], lista_numeros[index+1]]
                    lista_numeros[index] = lista_temp
                    lista_numeros.pop(index+1)
                    lista_numeros.pop(index-1)

                    index -= 1
                    id += 1
                
            else:

                if(caracter == "*" or caracter == "/"):
                    # si el elemento es * o /, se encapsula
                    lista_temp = [id,lista_numeros[index-1], lista_numeros[index], lista_numeros[index+1]]
                    lista_numeros[index] = lista_temp
                    lista_numeros.pop(index+1)
                    lista_numeros.pop(index-1)

                    index -= 1
                    id += 1
           
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
                            abertura = String_p("{")
                            cierre = String_p("}")

                        elif(abertura == "{"):
                            abertura = String_p("[")
                            cierre = String_p("]")

                        elif(abertura == "["):
                            abertura = String_p("(")
                            cierre = String_p(")")


                        abertura.set_id(chunk[0])
                        cierre.set_id(chunk[0])

                        chunk.pop(0)
                        
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
        lista_anidada = self.jerarquia_operadores(cadena)
        lista_con_signos = self.jerarquia_con_signos_de_agrupacion(lista_anidada)
        print(lista_con_signos)
        pilas = []
        temp_operandos = []
        temp_operadores = []

        largo = len(lista_con_signos)
        index = 0

        resultado_pila = ""
        

        while(index < largo):

            digito = lista_con_signos[index]
            if(self.es_numero(digito)):
                temp_operandos.append(digito)
            else:
                temp_operadores.append(digito)
                if(digito == "}" or digito == "]" or digito == ")"):

                    index_penultimo = len(temp_operadores) - 2

                    pila_alreves = [temp_operandos[i] for i in range(len(temp_operandos)-1,-1,-1)]
                    
                    resultado_pila += " ".join(pila_alreves)
                    resultado_pila += temp_operadores[index_penultimo]

                    copia_pilas = [temp_operandos,temp_operadores,resultado_pila]
                    pilas.append(copia_pilas)

                    print(temp_operandos)
                    print(temp_operadores)
                    print(resultado_pila)

                    temp_operandos = []
                    temp_operadores.pop(index_penultimo+1)
                    temp_operadores.pop(index_penultimo)
                    temp_operadores.pop(index_penultimo-1)

                    
                    
            index += 1



   
if __name__ == "__main__":
    cadena = "50 * 2 / 5 * 3 + 5"
    m = Codigo_intermedio()
    #m.jerarquia_operadores(cadena)
    m.notacion_polaca(cadena)




