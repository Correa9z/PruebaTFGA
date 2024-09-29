import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from controladores.empleado_controlador import EmpleadoControlador
from controladores.bd_controlador import BdControlador

class VistaEmpleado:

    ruta_input = ""

    def __init__(self,ruta_sistema):
        self.ruta_input = ruta_sistema / '../inputs/Empleados.txt'
        self.empleado_controlador = EmpleadoControlador()
        self.bd_controlador = BdControlador()        

    def leer_informacion(ruta):
        try:
            lista_empleados = pd.read_csv(ruta,delimiter=",",header=None)
            lista_empleados = lista_empleados.values.tolist()
            return lista_empleados
        except Exception as e:
            print(f"Error: {e}")


    def carga_empleados(self, numero_hilos = 200):
        lista_empleados = VistaEmpleado.leer_informacion(self.ruta_input)
        conexion, cursor = self.bd_controlador.iniciar_bd()
        with ThreadPoolExecutor(max_workers=numero_hilos) as executor:
            executor.map(lambda empleado: self.empleado_controlador.crear_empleado(conexion,cursor,empleado[0],empleado[1],empleado[2]), lista_empleados)
        self.bd_controlador.cerrar_bd(conexion,cursor)