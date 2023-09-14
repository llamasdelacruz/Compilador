import graphviz

def crear_arbol_compilador():
    # Crear un nuevo gráfico dirigido
    dot = graphviz.Digraph(comment='Ejemplo de arbol compilador ')
    contador_nodos=['$suma','=','$x','+','24','*','33','-','4','/','6','*','30']
    # Agregar nodos al gráfico
    dot.node('R','asignacion')
    dot.node('H','nomVar')
    dot.node('S','=')
    dot.node('O','operacion') 
    #Crear relaciones iniciales para empezr el arbol
    dot.edges(['RH','RS','RO']) 
    
    #Darle estilos a los nodos del arbol los cuales solo van hacer los padres    
    dot.node('R', shape='box', color='blue', style='filled', fillcolor='lightblue')
    dot.node('H', shape='box', color='blue', style='filled', fillcolor='lightblue')
    dot.node('R', shape='box', color='blue', style='filled', fillcolor='lightblue')
    dot.node('O', shape='box', color='blue', style='filled', fillcolor='lightblue')
    
    #----------------------------- Gereneración del arbol apartir del pasdre operacion --------------------------
    longitud_lista=len(contador_nodos)
    print("Esta es la longitud de la lsita",longitud_lista)
    
    c=0
    while c<len(contador_nodos): 
            if(len(contador_nodos)>10):
                dot.node('NO','nomvar')
                dot.node('OPE','operadores')
                dot.node('NUM','numeros')
                dot.node('OPE2','operadores')
                dot.node('OPERACION','operacion') 
                if(contador_nodos[0]):
                    dot.node('W',contador_nodos[0]) 
                    dot.node('NO', shape='box', color='blue', style='filled', fillcolor='lightblue')
                    dot.node('OPE', shape='box', color='blue', style='filled', fillcolor='lightblue')
                    dot.node('NUM', shape='box', color='blue', style='filled', fillcolor='lightblue')
                    dot.node('OPE2', shape='box', color='blue', style='filled', fillcolor='lightblue')
                    dot.node('OPERACION', shape='box', color='blue', style='filled', fillcolor='lightblue')
                c+=1
                if(c==2):
                    almaceno_valor=contador_nodos[c]
                    dot.node('numero',almaceno_valor)
                    print("Lo que almaceno de la posicion",almaceno_valor)
                    c+=1
                if(c==3):
                    almaceno_valor=contador_nodos[c]
                    dot.node('operador',almaceno_valor)
                    print("Lo que almaceno de la posicion",almaceno_valor)
                    c+=1
                if(c==4):
                    almaceno_valor=contador_nodos[c]
                    dot.node('numeros',almaceno_valor)
                    print("Lo que almaceno de la posicion",almaceno_valor)
                    c+=1
                if(c==5):
                    almaceno_valor=contador_nodos[c]
                    dot.node('operador2',almaceno_valor)
                    print("Lo que almaceno de la posicion",almaceno_valor)
                    c+=1
                if(c==6):
                    almaceno_valor=contador_nodos[c]
                    dot.node('numeros5',almaceno_valor)
                    if(almaceno_valor!="/" or almaceno_valor!="-" or almaceno_valor!="*" or almaceno_valor!="+"):
                        dot.node('numeros3','numeros')
                        dot.node('operadores3','operadores')
                        dot.node('numeros4','numeros')
                        dot.node('operadores4','operadores')
                        dot.node('operacion3','operacion')
                        print("Lo que almaceno de la posicion",almaceno_valor)
                        dot.node('numeros3', shape='box', color='blue', style='filled', fillcolor='lightblue')
                        dot.node('operadores3', shape='box', color='blue', style='filled', fillcolor='lightblue')
                        dot.node('numeros4', shape='box', color='blue', style='filled', fillcolor='lightblue')
                        dot.node('operadores4', shape='box', color='blue', style='filled', fillcolor='lightblue')
                        dot.node('operacion3', shape='box', color='blue', style='filled', fillcolor='lightblue')    
                    c+=1
                if(c==7):
                    almaceno_valor=contador_nodos[c]
                    dot.node('operadore5',almaceno_valor)
                    print("Lo que almaceno de la posicion",almaceno_valor)
                    c+=1
                if(c==8):
                    almaceno_valor=contador_nodos[c]
                    dot.node('NUMEROS6',almaceno_valor)
                    print("Lo que almaceno de la posicion",almaceno_valor)
                    c+=1
                if(c==9):
                    almaceno_valor=contador_nodos[c]
                    dot.node('OPERADOR6',almaceno_valor)
                    print("Lo que almaceno de la posicion",almaceno_valor)
                    c+=1
                if(c==10):
                    almaceno_valor=contador_nodos[c]
                    dot.node('numeros8',almaceno_valor)
                    if(almaceno_valor!="/" or almaceno_valor!="-" or almaceno_valor!="*" or almaceno_valor!="+"):
                        dot.node('numeros7','numeros')
                        dot.node('OPERADOR5','operadores')
                        dot.node('NUMEROS8','numeros')
                        print("Lo que almaceno de la posicion desde el 10",almaceno_valor)
                        dot.node('numeros7', shape='box', color='blue', style='filled', fillcolor='lightblue')
                        dot.node('OPERADOR5', shape='box', color='blue', style='filled', fillcolor='lightblue')
                        dot.node('NUMEROS8', shape='box', color='blue', style='filled', fillcolor='lightblue')    
                    c+=1
                if(c>11):
                        break
                else:
                    if(c==11):
                        almaceno_valor=contador_nodos[c]
                        dot.node('operadores10',almaceno_valor)
                        print("Lo que almaceno de la posicion",almaceno_valor)
                        c+=1
                    if(c==12):
                        almaceno_valor=contador_nodos[c]
                        dot.node('numeros10',almaceno_valor)
                        print("Lo que almaceno de la posicion",almaceno_valor)
                        c+=1
                    
    print("Este es le valor del contador al salir del ciclo",c)    
    if(c>11):           
        dot.edges(['HW',('O','NO'),('O','OPE'),('O','NUM'),('O','OPE2'),('O','OPERACION')])
        dot.edges([('NO','numero'),('OPE','operador'),('NUM','numeros'),('OPE2','operador2')])
        dot.edges([('OPERACION','numeros3'),('OPERACION','operadores3'),('OPERACION','numeros4'),('OPERACION','operadores4'),('OPERACION','operacion3')])        
        dot.edges([('numeros3','numeros5'),('operadores3','operadore5'),('numeros4','NUMEROS6'),('operadores4','OPERADOR6')])    
        dot.edges([('operacion3','numeros7'),('operacion3','OPERADOR5'),('operacion3','NUMEROS8')]) 
        dot.edges([('numeros7','numeros8'),('OPERADOR5','operadores10'),('NUMEROS8','numeros10')])
        # Guardar el gráfico como un archivo y visualizarlo
        dot.render('mi_grafo_personalizado', view=True)
    elif(c<=11):
        dot.edges(['HW',('O','NO'),('O','OPE'),('O','NUM'),('O','OPE2'),('O','OPERACION')])
        dot.edges([('NO','numero'),('OPE','operador'),('NUM','numeros'),('OPE2','operador2')])
        dot.edges([('OPERACION','numeros3'),('OPERACION','operadores3'),('OPERACION','numeros4'),('OPERACION','operadores4'),('OPERACION','operacion3')])        
        dot.edges([('numeros3','numeros5'),('operadores3','operadore5'),('numeros4','NUMEROS6'),('operadores4','OPERADOR6')])    
        dot.edges([('operacion3','numeros7'),('operacion3','OPERADOR5'),('operacion3','NUMEROS8')]) 
        # Guardar el gráfico como un archivo y visualizarlo
        dot.render('mi_grafo_personalizado', view=True)
        
# Llamar a la función para crear y visualizar el grafo personalizado
crear_arbol_compilador()
