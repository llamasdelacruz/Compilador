import graphviz

def crear_arbol_compilador():
    # Crear un nuevo gráfico dirigido
    dot = graphviz.Digraph(comment='Ejemplo de arbol compilador ')
    contador_nodos=['$suma','=','$x','+','24','*','33','-','4','/','6']
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
    if(contador_nodos[0]):
        dot.node('W',contador_nodos[0])
    dot.edges(['HW'])  
    for i in range(2,len(contador_nodos)):
        
        print("Desde a qui empieza la lista de operacion",contador_nodos[i])
        if(contador_nodos[i]):
            dot.node('N','nomvar')
            dot.edges(['ON'])
            break
        elif(contador_nodos[i]):
            dot.node()
        
    
        
            
            
    # Guardar el gráfico como un archivo y visualizarlo
    dot.render('mi_grafo_personalizado', view=True)

# Llamar a la función para crear y visualizar el grafo personalizado
crear_arbol_compilador()
