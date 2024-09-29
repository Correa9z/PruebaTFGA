from modelos.proyecto import Proyecto

class ProyectoControlador:

    def __init__(self):
        self.proyecto = Proyecto("","","")
        self.proyecto.iniciar_logs()

    def crear_proyecto(self,nombre,nombre_empleado):
        self.proyecto.crear_proyecto(nombre,nombre_empleado)

    def buscar_totalidad_proyectos(self):
        return self.proyecto.buscar_totalidad_proyectos()


