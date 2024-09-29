from modelos.departamento import Departamento
from infra.conexion_bd import ConexionBd

class DepartamentoControlador:

    def __init__(self):
        self.departamento = Departamento("","")
        self.conexion_bd = ConexionBd()
        self.departamento.iniciar_logs()

    def crear_departamento(self,conexion,cursor,nombre): 
        self.departamento.crear_departamento(conexion,cursor,nombre)

    def iniciar_bd(self):
        conexion, cursor = self.conexion_bd.conectar_bd()
        return conexion, cursor

    def cerrar_bd(self,conexion,cursor):
        if (cursor != None):
            self.conexion_bd.cerrar_bd(conexion,cursor)