from modelos.empleado import Empleado

class EmpleadoControlador:

    empleado = Empleado("","","","")

    def crear_empleado(self,nombre,identificacion,departamento):
        self.empleado.crear_empleado(nombre,identificacion,departamento)

