from modelos.proyecto import Proyecto

class ProyectoControlador:

    def __init__(self):
        self.proyecto = Proyecto("","","")
        self.proyecto.iniciar_logs()

    def crear_proyecto(self,conexion,cursor,nombre,nombre_empleado):
        self.proyecto.crear_proyecto(conexion,cursor,nombre,nombre_empleado)

    def buscar_totalidad_proyectos(self,cursor):
        return self.proyecto.buscar_totalidad_proyectos(cursor)
    
    def actualizar_proyectos(self,conexion,cursor,nombre_departamento,viejo_nombre,nuevo_nombre):
        self.proyecto.actualizar_nombre_proyectos(conexion,cursor,nombre_departamento,viejo_nombre,nuevo_nombre)

