from modelos.departamento import Departamento
import logging
from threading import Lock
import os


class Empleado:

    logger = ""
    departamento = Departamento("","")
    

    def __init__(self,id,nombre,identificacion,departamento_id):
        self.id = id
        self.nombre = nombre
        self.identificacion = identificacion
        self.departamento_id = departamento_id
        self.lock = Lock() 
    

    def crear_empleado(self,conexion,cursor,nombre,identificacion,departamento):
        with self.lock:
            try:
                resultado = Empleado.buscar_empleado_identificacion(self,cursor,identificacion)
                departamento_obj = self.departamento.buscar_departamento_nombre(cursor,departamento)
                
                if(resultado == None):
                    if(departamento_obj != None):
                        query = "INSERT INTO empleados (nombre,identificacion,departamento_id) VALUES (%s,%s,%s)"
                        cursor.execute(query,(nombre,identificacion,departamento_obj.id,))
                        conexion.commit()
                        self.logger.info(f"{nombre}-{identificacion}-{departamento}: Registro almacenado correctamente.")
                    else:
                        self.logger.error(f"{nombre}-{identificacion}-{departamento}: El departamento no existe en la BD")
                else:
                    self.logger.error(f"{nombre}-{identificacion}-{departamento}: El empleado ya existe en la BD")

            except Exception as e:
                print(f"Error: {e}")

    
    def buscar_empleado_identificacion(self,cursor,identificacion_empleado):
        try:
            query = "SELECT id, nombre, identificacion, departamento_id FROM empleados WHERE identificacion = %s"
            cursor.execute(query,(identificacion_empleado,))
            resultado = cursor.fetchone()

            if resultado != None:
                return Empleado(*resultado)
            else:
                return None
            
        except Exception as e:
            print(f"Error: {e}")


    def buscar_empleado_nombre(self,cursor,nombre_empleado):
        try:
            query = "SELECT id, nombre, identificacion, departamento_id FROM empleados WHERE nombre = %s"
            cursor.execute(query,(nombre_empleado,))
            resultado = cursor.fetchone()

            if resultado != None:
                return Empleado(*resultado)
            else:
                return None
            
        except Exception as e:
            print(f"Error: {e}")


    def iniciar_logs(self,):
        logger = logging.getLogger('empleado')
        logger.setLevel(logging.DEBUG)
        
        if not logger.hasHandlers():
            file_handler = logging.FileHandler(os.path.join("app/logs/", 'empleado.log'))
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        self.logger = logger