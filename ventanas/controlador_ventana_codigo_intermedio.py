import sys 
from PyQt5.QtWidgets import QApplication,QDialog,QTableWidget
from PyQt5 import uic
from PyQt5 import QtWidgets
import ctypes


class Control_pantalla_codigo_intermedio(QDialog):
    
    def __init__(self,ventana_principal,resultados):
       
        self.ventana_principal=ventana_principal
        self.resultados = resultados
        QDialog.__init__(self)
        #super().__init__()
        #Carga la configuracion del archivo .ui en el objeto para su ejecucion
        uic.loadUi("ventanas/Ventana_codigo_intermedio.ui",self)
        
        #Comandos para centrar la ventana
        
        resolucion=ctypes.windll.user32
        resolucion_ancho=resolucion.GetSystemMetrics(0)
        resolucion_alto=resolucion.GetSystemMetrics(1)
        
        left=int((resolucion_ancho/2)-(self.frameSize().width()/2))
        top=int((resolucion_alto/2)-(self.frameSize().height()/2))
        
        self.move(left,top)
        self.colocar()
        
    def closeEvent(self, event):

        self.ventana_principal.show()

    def colocar(self):
        # print(self.resultados)
        #Colocar en resultados notacion polaca
        self.consola_polaca.setPlainText(self.resultados[0])
        #Colocar en resultados codigo p
        self.consola_codigop.setPlainText(self.resultados[1])

        filas_c = self.resultados[5]
        self.cuadruplos.setRowCount(filas_c)

        fila_c = 0
        #Colocar en la tabla de triplos
        filas_t = self.resultados[4]
        self.triplos.setRowCount(filas_t)

        fila_t = 0

        while(fila_t < filas_t):

            for i in self.resultados[2]:

                for j in i:

                    self.triplos.setItem(fila_t,0, QtWidgets.QTableWidgetItem(j[0]))
                    self.triplos.setItem(fila_t,1, QtWidgets.QTableWidgetItem(j[1]))
                    self.triplos.setItem(fila_t,2, QtWidgets.QTableWidgetItem(j[2]))
                    self.triplos.setItem(fila_t,3, QtWidgets.QTableWidgetItem(j[3]))
                    fila_t += 1

                fila_t += 1

        # cuadruplos
        while(fila_c < filas_c):

            for i in self.resultados[3]:

                for j in i:

                    self.cuadruplos.setItem(fila_c,0, QtWidgets.QTableWidgetItem(j[0]))
                    self.cuadruplos.setItem(fila_c,1, QtWidgets.QTableWidgetItem(j[1]))
                    self.cuadruplos.setItem(fila_c,2, QtWidgets.QTableWidgetItem(j[2]))
                    self.cuadruplos.setItem(fila_c,3, QtWidgets.QTableWidgetItem(j[3]))
                    fila_c += 1

                fila_c += 1
     
       



if(__name__ == "__main__"):

    #Instancia para iniciar la aplicacion
    app = QApplication(sys.argv)
    ventana = Control_pantalla_codigo_intermedio()
    ventana.show()
    #ejecutar la aplicacion
    app.exec_()