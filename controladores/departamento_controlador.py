from modelos.departamento import Departamento

class DepartamentoControlador:

    departamento = Departamento("","")

    def crear_departamento(self,nombre): 
        self.departamento.crear_departamento(nombre)
