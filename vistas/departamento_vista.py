import pandas as pd
from controladores.departamento_controlador import DepartamentoControlador


class VistaDepartamento:

    def __init__(self):
        self.controlador = DepartamentoControlador()

    def carga_departamentos(self):
        info = pd.read_csv("",delimiter=",",header=None)
        VistaDepartamento.crear_departamento(self,info)

    def inicio_hilos(self):
        return False
    
    def finalizar_hilos(self):
        return False
    
    def crear_departamento(self,nombre):
        self.controlador.crear_departamento(nombre)

