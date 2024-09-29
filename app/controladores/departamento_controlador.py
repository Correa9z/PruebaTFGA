from modelos.departamento import Departamento
from infra.conexion_bd import ConexionBd

class DepartamentoControlador:

    def __init__(self):
        self.departamento = Departamento("","")
        self.departamento.iniciar_logs()

    def crear_departamento(self,conexion,cursor,nombre): 
        self.departamento.crear_departamento(conexion,cursor,nombre)
