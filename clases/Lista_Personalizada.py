
class Lista_p(list):

    def __init__(self,iterable,nombre,padre="undefined"):
        super().__init__(item for item in iterable)
        self.name_lista = nombre
        self.name_padre = padre

    def get_name(self):
        return self.name_lista
    
    def set_name(self,name):
        self.name_lista = name

    def get_name_padre(self):
        # retorna el nombre del contenedor padre de este elemento
        return self.name_padre
    
    def append_start(self,element):
        # agrega el elemento al principio de la lista 
        # self aqui hace referencia a la lista en si misma
        self.insert(0,element)

    def remove_start(self):
        # elimina el primer elemento de la lista
        element = "Undefined"
        if(len(self) > 0):
            element = self[0]
            self.remove(element)

        return element
            

