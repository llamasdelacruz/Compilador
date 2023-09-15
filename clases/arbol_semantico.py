import graphviz


arbol = [
        ["$a", "=", "2", "+", "4", ";"],
        ["$a", "=", "2", "*", "3", ";"],
]


def arboles():
    dot = graphviz.Digraph('round-table', comment='The Round Table')

    largo = len(arbol)

    for i in range(0, largo):

        # crea la raiz del arbol
        dot.node(str(i), "Asignacion")
        dot.node(str(i)+"nomVar", "nomVar")
        dot.node(str(i)+arbol[i][0], arbol[i][0])
        dot.node(str(i)+"igual", "=")

        largo_lista = len(arbol[i])
        primer_elemento_asignacion = arbol[i][2]

        if(largo_lista > 4):
            pass

        else:
            dot.node(str(i)+"nomVar"+primer_elemento_asignacion, "nomVar")
            dot.node(str(i)+"valor"+primer_elemento_asignacion,
                     primer_elemento_asignacion)

            dot.edge(str(i), str(i)+"nomVar"+primer_elemento_asignacion)
            dot.edge(str(i)+"nomVar"+primer_elemento_asignacion,
                     str(i)+"valor"+primer_elemento_asignacion)

        # creamos las conecciones
        dot.node(str(i)+"final", ";")
        dot.edge(str(i), str(i)+"nomVar")
        dot.edge(str(i), str(i)+"igual")

        dot.edge(str(i)+"nomVar", str(i)+arbol[i][0])
        dot.edge(str(i), str(i)+"final")

    dot.render('mi_grafo_personalizado', view=True)


arboles()
