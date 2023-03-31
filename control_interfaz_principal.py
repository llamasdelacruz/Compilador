
import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem,QFileDialog
from PyQt5 import uic
import ctypes
from clases.Lexico import Lexico
from ventanas.controlador_interfaz_tabla import Control_pantalla_tabla_token

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
        self.btn_limpiar.clicked.connect(self.limpiar)
        

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
        else:
            self.consola.setPlainText("")
            self.consola.setPlainText(errores)

        
    def limpiar(self):
        self.areaTexto.setPlainText("")
        self.consola.setPlainText("")

    def cargar_ventana_token(self,tokens):
        
        self.ex = Control_pantalla_tabla_token(self,tokens)
        self.ex.show()

if(__name__ == "__main__"):

    #Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    ventana = Control_interfaz_principal()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()
