from modelos.empleado import Empleado

class EmpleadoControlador:

    def __init__(self):
        self.empleado = Empleado("","","","")
        self.empleado.iniciar_logs()

    def crear_empleado(self,nombre,identificacion,departamento):
        self.empleado.crear_empleado(nombre,identificacion,departamento)