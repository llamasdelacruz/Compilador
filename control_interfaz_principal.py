
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from PyQt5 import uic
import ctypes


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

if(__name__ == "__main__"):

    #Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    ventana = Control_interfaz_principal()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()
