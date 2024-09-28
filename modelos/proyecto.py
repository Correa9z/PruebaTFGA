from infra.conexion_bd import ConexionBd
from modelos.empleado import Empleado
import logging


class Proyecto:

    conexion = ConexionBd()
    

    def __init__(self,id,nombre,empleado_id):
        self.id = id
        self.nombre = nombre
        self.empleado_id = empleado_id 
    

    def crear_proyecto(self,nombre,nombre_empleado):
        try:
            Proyecto.iniciar_logs()
            resultado = Proyecto.buscar_proyecto_nombre(self,nombre)
            empleado = Empleado("","","","")
            empleado = empleado.buscar_empleado_nombre(nombre_empleado)

            cursor = self.conexion.conectar_bd()
            
            if(resultado == None):
                if(empleado != None):
                    query = "INSERT INTO proyectos (nombre,empleado_id) VALUES (%s,%s)"
                    cursor.execute(query,(nombre,empleado.id,))
                    self.conexion.conexion.commit()
                    logging.info(f"{nombre}-{nombre_empleado}: Registro almacenado correctamente")
                else:
                    logging.error(f"{nombre}-{nombre_empleado}: El empleado no existe en la BD")
            else:
                logging.error(f"{nombre}-{nombre_empleado}: El proyecto ya existe en al BD")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            self.conexion.cerrar_bd(cursor)

    
    def buscar_proyecto_nombre(self,nombre_proyecto):
        try:
            cursor = self.conexion.conectar_bd()
            query = "SELECT id, nombre, empleado_id FROM proyectos WHERE nombre = %s"
            cursor.execute(query,(nombre_proyecto,))
            resultado = cursor.fetchone()

            if resultado != None:
            
                return Proyecto(*resultado)
            else: 
                return None
            
        except Exception as e:
            print(f"Error: {e}")

        finally:
            self.conexion.cerrar_bd(cursor)


    

    def buscar_totalidad_proyectos(self):
        try:
            cursor = self.conexion.conectar_bd()
            query = "SELECT p.id, p.nombre, e.nombre, d.nombre FROM proyectos p INNER JOIN empleados e ON p.empleado_id = e.id INNER JOIN departamentos d ON e.departamento_id = d.id"
            cursor.execute(query,())
            resultado = cursor.fetchall()

            if resultado != None:
                print(resultado)
            else: 
                print("None")
            
        except Exception as e:
            print(f"Error: {e}")

        finally:
            self.conexion.cerrar_bd(cursor)

    
    


    def iniciar_logs():
        logging.basicConfig(
        filename='proyecto.log',             # Nombre del archivo de logs
        level=logging.DEBUG,            # Nivel de registro: DEBUG, INFO, WARNING, ERROR, CRITICAL
        format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del mensaje
        datefmt='%Y-%m-%d %H:%M:%S'     # Formato de la fecha
    )