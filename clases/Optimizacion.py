from clases.Lista_Personalizada import Lista_p
from clases.String_Personalizado import String_p

class Optimizacion():

    def precalcular_expresiones_constantes(self):
        pass

    def eliminacion_de_secuencias_nulas(self):
        pass

    def reduccion_de_potencias(self):
        pass
    
    def propagacion_de_copias(self):
        pass


if __name__ == "__main__":
    objecto = Optimizacion()
    texto = "START \n INT $m , $r ; \n $m = 10 ; \n $r = 11 + $m ; \n END"
    objecto.analizar(texto)
  
    

   
