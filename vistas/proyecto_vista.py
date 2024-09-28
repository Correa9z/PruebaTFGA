import pandas as pd
from controladores.proyecto_controlador import ProyectoControlador


class VistaProyecto:

    def __init__(self):
        self.controlador = ProyectoControlador()

    def carga_proyectos(self):
        info = pd.read_csv("",delimiter=",",header=None)
        VistaProyecto.crear_proyecto(self,info)

    def inicio_hilos(self):
        return False
    
    def finalizar_hilos(self):
        return False
    
    def crear_proyecto(self,nombre,nombre_empleado):
        self.controlador.crear_proyecto(nombre,nombre_empleado)

    def buscar_totalidad_proyectos(self):
        resultados = self.controlador.buscar_totalidad_proyectos()
        print(resultados)