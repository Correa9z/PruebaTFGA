import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from controladores.empleado_controlador import EmpleadoControlador


class VistaEmpleado:

    ruta_input = ""

    def __init__(self,ruta_sistema):
        self.ruta_input = ruta_sistema / '../inputs/Empleados.txt'
        self.controlador = EmpleadoControlador()

    def leer_informacion(ruta):
        try:
            lista_empleados = pd.read_csv(ruta,delimiter=",",header=None)
            lista_empleados = lista_empleados.values.tolist()
            return lista_empleados
        except Exception as e:
            print(f"Error: {e}")

    def carga_empleados(self, numero_hilos = 10):
        lista_empleados = VistaEmpleado.leer_informacion(self.ruta_input)
        with ThreadPoolExecutor(max_workers=numero_hilos) as executor:
            executor.map(lambda empleado: self.controlador.crear_empleado(empleado[0],empleado[1],empleado[2]), lista_empleados)
