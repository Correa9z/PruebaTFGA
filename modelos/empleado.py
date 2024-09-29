from infra.conexion_bd import ConexionBd
from modelos.departamento import Departamento
import logging
from threading import Lock


class Empleado:

    conexion = ConexionBd()
    

    def __init__(self,id,nombre,identificacion,departamento_id):
        self.id = id
        self.nombre = nombre
        self.identificacion = identificacion
        self.departamento_id = departamento_id
        self.lock = Lock() 
        Empleado.iniciar_logs()
    

    def crear_empleado(self,nombre,identificacion,departamento):
        with self.lock:
            try:
                resultado = Empleado.buscar_empleado_identificacion(self,identificacion)
                departamento_obj = Departamento("","")
                departamento_obj = departamento_obj.buscar_departamento_nombre(departamento)

                cursor = self.conexion.conectar_bd()
                
                if(resultado == None):
                    if(departamento_obj != None):
                        query = "INSERT INTO empleados (nombre,identificacion,departamento_id) VALUES (%s,%s,%s)"
                        cursor.execute(query,(nombre,identificacion,departamento_obj.id,))
                        self.conexion.conexion.commit()
                        logging.info(f"{nombre}-{identificacion}-{departamento}: Registro almacenado correctamente.")
                    else:
                        logging.error(f"{nombre}-{identificacion}-{departamento}: El departamento no existe en la BD")
                else:
                    logging.error(f"{nombre}-{identificacion}-{departamento}: El empleado ya existe en la BD")

            except Exception as e:
                print(f"Error: {e}")

            finally:
                self.conexion.cerrar_bd(cursor)

    
    def buscar_empleado_identificacion(self,identificacion_empleado):
        try:
            cursor = self.conexion.conectar_bd()
            query = "SELECT id, nombre, identificacion, departamento_id FROM empleados WHERE identificacion = %s"
            cursor.execute(query,(identificacion_empleado,))
            resultado = cursor.fetchone()

            if resultado != None:
                return Empleado(*resultado)
            else:
                return None
            
        except Exception as e:
            print(f"Error: {e}")

        finally:
            self.conexion.cerrar_bd(cursor)


    def buscar_empleado_nombre(self,nombre_empleado):
        try:
            print(nombre_empleado)
            cursor = self.conexion.conectar_bd()
            query = "SELECT id, nombre, identificacion, departamento_id FROM empleados WHERE nombre = %s"
            cursor.execute(query,(nombre_empleado,))
            resultado = cursor.fetchone()

            if resultado != None:
                return Empleado(*resultado)
            else:
                return None
            
        except Exception as e:
            print(f"Error: {e}")

        finally:
            self.conexion.cerrar_bd(cursor)


    def iniciar_logs():
        logging.basicConfig(
        filename='empleado.log',             # Nombre del archivo de logs
        level=logging.DEBUG,            # Nivel de registro: DEBUG, INFO, WARNING, ERROR, CRITICAL
        format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del mensaje
        datefmt='%Y-%m-%d %H:%M:%S'     # Formato de la fecha
    )