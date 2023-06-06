import sys 
from PyQt5.QtWidgets import QApplication,QDialog,QTableWidget
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes


class Control_ventana_sintactico(QDialog):
    
    def __init__(self,ventana_principal,resultado):
        self.resultado = resultado
        
        self.ventana_principal=ventana_principal
        
        QDialog.__init__(self)
        #super().__init__()
        #Carga la configuracion del archivo .ui en el objeto para su ejecucion
        uic.loadUi("ventanas/ventana_sintactico_retroceso.ui",self)
        
        #Comandos para centrar la ventana
        
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        
        left=int((resolucion_ancho/2)-(self.frameSize().width()/2))
        top=int((resolucion_alto/2)-(self.frameSize().height()/2))
        
        self.move(left,top)
        self.llenar_consola()

    def llenar_consola(self):
        
        self.consola_retroceso.setPlainText(self.resultado)
    


    def closeEvent(self, event):

        self.ventana_principal.show()
          