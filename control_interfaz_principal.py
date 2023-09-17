
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QFileDialog
from PyQt5 import uic
import ctypes
from clases.Lexico import Lexico
from clases.Sintactico import Sintactico
from clases.Semantico import Semantico
from ventanas.controlador_interfaz_tabla import Control_pantalla_tabla_token
from ventanas.controlador_sintactico_retroceso import Control_ventana_sintactico
from ventanas.controlador_ventana_tabla_semantica import Control_pantalla_tabla_semantica

class Control_interfaz_principal(QMainWindow):

    def __init__(self):

        super().__init__()
        #cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("ventana_principal.ui", self)

        #centrar ventana
        resolucion = ctypes.windll.user32
        resolucion_ancho = resolucion.GetSystemMetrics(0)
        resolucion_alto = resolucion.GetSystemMetrics(1)

        left = int((resolucion_ancho/2) - (self.frameSize().width()/2))
        top = int((resolucion_alto/2) - (self.frameSize().height()/2))

        self.move(left,top)

        self.btn_cargarArchivo.clicked.connect(self.chooseFile)
        self.btn_lexico.clicked.connect(self.analizar_lexico)
        self.btn_sintactico.clicked.connect(self.analizar_sintactico)
        self.btn_semantico.clicked.connect(self.analizar_semantico)
        
        self.btn_limpiar.clicked.connect(self.limpiar) 
        self.areaTexto.textChanged.connect(self.cambio)

    def chooseFile(self):
        tipo = "archivo de datos (*.txt)"
        respuesta = QFileDialog.getOpenFileName(
            parent=self,
            caption="Seleccione archivo",
            directory=os.getcwd(),#la direccion de trabajo
            filter=tipo,
            initialFilter=tipo
        )
        if(respuesta[0] != ""):
            archivo = open(respuesta[0],'r')
            self.limpiar()
            self.areaTexto.appendPlainText(archivo.read())
      
    def analizar_lexico(self):
        #le pasa el texto
        texto = self.areaTexto.toPlainText()
        lexico_obj = Lexico()
        errores = lexico_obj.analizar(texto)

        if(errores == "" and len(lexico_obj.tabla_tokens) > 0):
            self.consola.setPlainText("")
            self.cargar_ventana_token(lexico_obj.tabla_tokens)
            self.btn_sintactico.setEnabled(True)
        else:
            self.consola.setPlainText("")
            self.consola.setPlainText(errores)
            self.btn_sintactico.setEnabled(False)

    def analizar_sintactico(self):
        texto = self.areaTexto.toPlainText()
        sintactico_obj = Sintactico()
        sintactico_obj.establecer_cadena(texto)
        seAprueba = sintactico_obj.analizar()
        self.cargar_ventana_sintactico(sintactico_obj.resultados)
        self.pila = sintactico_obj.parseo["pila"]
        self.btn_semantico.setEnabled(seAprueba)
        

    def analizar_semantico(self):
        
        semantico_obj = Semantico()
        errores = semantico_obj.analizar(self.areaTexto.toPlainText())
        if(errores == ""):
            self.cargar_ventana_semantico()
            semantico_obj.pila = self.pila
            #la imprimir_ pila 2 hace las sumas de izquierda a derecha sin prioridad
            #semantico_obj.imprimir_pila2()
            # la imprimir_ pila hace las operacion con prioridad de operadores
            semantico_obj.imprimir_pila()
        else:
            self.consola.setPlainText("")
            self.consola.setPlainText(errores)
            



    def cambio(self):
        self.btn_sintactico.setEnabled(False)
        self.btn_semantico.setEnabled(False)

    def limpiar(self):
        self.areaTexto.setPlainText("")
        self.consola.setPlainText("")

    def cargar_ventana_token(self,tokens):
        
        self.ex = Control_pantalla_tabla_token(self,tokens)
        self.ex.show()

    def cargar_ventana_sintactico(self,resultado):
        self.ex = Control_ventana_sintactico(self,resultado)
        self.ex.show()

    def cargar_ventana_semantico(self):
        self.ex = Control_pantalla_tabla_semantica(self)
        self.ex.show()

if(__name__ == "__main__"):

    #Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    ventana = Control_interfaz_principal()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()
