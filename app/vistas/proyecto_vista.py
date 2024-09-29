import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from controladores.proyecto_controlador import ProyectoControlador


class VistaProyecto:

    ruta_input = ""
    ruta_input_actualizacion = ""
    ruta_totalidad_proyectos = ""

    def __init__(self,ruta_sistema):
        self.ruta_input = ruta_sistema / '../inputs/Proyectos.txt'
        self.ruta_input_actualizacion = ruta_sistema / '../inputs/ProyectosActualizacion.txt'
        self.ruta_totalidad_proyectos = ruta_sistema / '../resultados/ProyectosTotalidad.xlsx'
        self.controlador = ProyectoControlador()

    def leer_informacion(ruta):
        try:
            lista_proyectos = pd.read_csv(ruta,delimiter=",",header=None)
            lista_proyectos = lista_proyectos.values.tolist()
            return lista_proyectos
        except Exception as e:
            print(f"Error: {e}")

    def carga_proyectos(self, numero_hilos = 10):
        lista_proyectos = VistaProyecto.leer_informacion(self.ruta_input)
        with ThreadPoolExecutor(max_workers=numero_hilos) as executor:
            executor.map(lambda proyecto: self.controlador.crear_proyecto(proyecto[0],proyecto[1]), lista_proyectos)

    def buscar_totalidad_proyectos(self):
        resultados = self.controlador.buscar_totalidad_proyectos()
        dataframe = pd.DataFrame(resultados,columns=['Id Proyecto', 'Nombre Proyecto', 'Nombre Empleado', 'Departamento Nombre'])
        dataframe.to_excel(self.ruta_totalidad_proyectos,index=False)

    def carga_actualizacion_proyectos(self, numero_hilos = 10):
        lista_proyectos = VistaProyecto.leer_informacion(self.ruta_input_actualizacion)
        with ThreadPoolExecutor(max_workers=numero_hilos) as executor:
            executor.map(lambda proyecto: self.controlador.crear_proyecto(proyecto[0],proyecto[1]), lista_proyectos)