import string
class Sintactico():
    
    def __init__(self):

        self.parseo = {
            "estado":[],
            "apuntador":[],
            "pila":[],
            "sentencia_actual":[]
        }
        
        self.gramatica = {

            "programa":["START","sentencias","END"],
            "sentencias":["declaraVar","comentario","mensajePantalla","asignacion","operacion","obtenerDatosPantalla",
                          ["declaraVar","sentencias"],["comentario","sentencias"],["mensajePantalla","sentencias"],
                           ["asignacion","sentencias"],["operacion","sentencias"],["obtenerDatosPantalla","sentencias"]
                           ],

            "declaraVar":[["tipoDato","$","nomVar",";"],
                          ["tipoDato","$","nomVar",",","$","nomVar",";"]
                          ],
            
            "tipoDato":["INT","FLOAT","BOOLEAN","STRING","CHAR"],

            "asignacion":[["$","nomVar","=","$","nomVar",";"],
                          ["$","nomVar","=","numeros",";"],
                          ["$","nomVar","=","operacion",";"],
                          ["$","nomVar","=","TRUE",";"],
                          ["$","nomVar","=","FALSE",";"]
                         ],

            "operacion":[["$","nomVar","operadores","$","nomVar",";"],
                         ["$","nomVar","operadores","numeros",";"],
                         ["numeros","operadores","numeros",";"],
                         ["numeros","operadores","$","nomVar",";"]
                         ],

            "operdores":["+","-","*","/"],

            "numeros":["numero",
                        ["numero","numeros"],
                        ["numero",".","numeros"]
                       ],

            "numero":["0","1","2","3","4","5","6","7","8","9"],

            "numVar":["letraMinus",
                      ["letraMinus","nomVar"]
                      ],

            "letraMinus":list(string.ascii_lowercase),

            "comentario":["#","mensaje"],

            "mensajePantalla":[["OUTPUT","'","mensaje","'",";"],
                               ["OUTPUT","'","mensaje","'",",","$","nomVar",";"]
                               ],

            "obtenerDatosPantalla":["INPUT","$","nomVar",";"],

            "mensaje":[]
            
        }
        
   

if __name__ == "__main__":
    objecto = Sintactico()
  
   