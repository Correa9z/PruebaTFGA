from modelos.proyecto import Proyecto

class ProyectoControlador:

    proyecto = Proyecto("","","")

    def crear_proyecto(self,nombre,nombre_empleado):
        self.proyecto.crear_proyecto(nombre,nombre_empleado)

    def buscar_totalidad_proyectos(self):
        return self.proyecto.buscar_totalidad_proyectos()


