import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from controladores.departamento_controlador import DepartamentoControlador
from controladores.bd_controlador import BdControlador


class VistaDepartamento:

    ruta_input = ""

    def __init__(self,ruta_sistema):
        self.ruta_input = ruta_sistema / '../inputs/Departamentos.txt'
        self.departamento_controlador = DepartamentoControlador()
        self.bd_controlador = BdControlador()  

    def leer_informacion(ruta):
        try:
            lista_departamentos = pd.read_csv(ruta,header=None)
            lista_departamentos = lista_departamentos.values.tolist()
            return lista_departamentos
        except Exception as e:
            print(f"Error: {e}")
    

    def carga_departamentos(self, numero_hilos=20):
        lista_departamentos = VistaDepartamento.leer_informacion(self.ruta_input)
        conexion, cursor = self.bd_controlador.iniciar_bd()
        with ThreadPoolExecutor(max_workers=numero_hilos) as executor:
            executor.map(lambda departamento: self.departamento_controlador.crear_departamento(conexion,cursor,departamento[0]), lista_departamentos)
        self.bd_controlador.cerrar_bd(conexion,cursor)