import sys 
from PyQt5.QtWidgets import QApplication,QDialog,QTableWidget
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes


class Control_pantalla_codigo_intermedio(QDialog):
    
    def __init__(self):
       
        
        
        
        QDialog.__init__(self)
        #super().__init__()
        #Carga la configuracion del archivo .ui en el objeto para su ejecucion
        uic.loadUi("ventanas/Ventana_codigo_intermedio.ui")
        
        #Comandos para centrar la ventana
        
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        
        left=int((resolucion_ancho/2)-(self.frameSize().width()/2))
        top=int((resolucion_alto/2)-(self.frameSize().height()/2))
        
        self.move(left,top)
        
    def closeEvent(self, event):

        self.ventana_principal.show()



if(__name__ == "__main__"):

    #Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    ventana = Control_pantalla_codigo_intermedio()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()