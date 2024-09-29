from modelos.empleado import Empleado

class EmpleadoControlador:

    def __init__(self):
        self.empleado = Empleado("","","","")
        self.empleado.iniciar_logs()

    def crear_empleado(self,conexion,cursor,nombre,identificacion,departamento):
        self.empleado.crear_empleado(conexion,cursor,nombre,identificacion,departamento)
