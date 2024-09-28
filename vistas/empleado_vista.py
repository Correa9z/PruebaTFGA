import pandas as pd
from controladores.empleado_controlador import EmpleadoControlador


class VistaEmpleado:

    def __init__(self):
        self.controlador = EmpleadoControlador()

    def carga_empleados(self):
        info = pd.read_csv("",delimiter=",",header=None)
        VistaEmpleado.crear_empleado(self,info)

    def inicio_hilos(self):
        return False
    
    def finalizar_hilos(self):
        return False
    
    def crear_empleado(self,nombre,identificacion,departamento):
        self.controlador.crear_empleado(nombre,identificacion,departamento)