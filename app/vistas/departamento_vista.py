import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from controladores.departamento_controlador import DepartamentoControlador


class VistaDepartamento:

    ruta_input = ""

    def __init__(self,ruta_sistema):
        self.ruta_input = ruta_sistema / '../inputs/Departamentos.txt'
        print(self.ruta_input)
        self.controlador = DepartamentoControlador()

    def leer_informacion(ruta):
        try:
            lista_departamentos = pd.read_csv(ruta,header=None)
            lista_departamentos = lista_departamentos.values.tolist()
            return lista_departamentos
        except Exception as e:
            print(f"Error: {e}")
    

    def carga_departamentos(self, numero_hilos=10):
        lista_departamentos = VistaDepartamento.leer_informacion(self.ruta_input)
        with ThreadPoolExecutor(max_workers=numero_hilos) as executor:
            executor.map(lambda departamento: self.controlador.crear_departamento(departamento[0]), lista_departamentos)