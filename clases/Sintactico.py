from difflib import SequenceMatcher
class Sintactico():
    
    def __init__(self):
        self.regla_1 ={}
        
    def crear_reglas(self,palabra):
        cantidad_elementos = len(palabra)
        for i in range(0,cantidad_elementos):
            if(palabra[i]=="Programa"):
                self.regla_1= {"n": i, "Programa":palabra[i], "complemento":["#"]}
                print("Entre a la condicion")
                
        print("Esto es lo que llega a crear reglas",palabra)
        print("Esto es lo que llega a crear reglas",self.regla_1)

if __name__ == "__main__":
    objecto = Sintactico()
    objecto.crear_reglas()