from infra.conexion_bd import ConexionBd
from modelos.empleado import Empleado
from modelos.departamento import Departamento
import logging
from threading import Lock
import os


class Proyecto:

    logger = ""
    empleado = Empleado("","","","")
    departamento = Departamento("","")
    
    def __init__(self,id,nombre,empleado_id):
        self.id = id
        self.nombre = nombre
        self.empleado_id = empleado_id 
        self.lock = Lock()
    

    def crear_proyecto(self,conexion,cursor,nombre,nombre_empleado):
        with self.lock:
            try:
                resultado = Proyecto.buscar_proyecto_nombre(self,cursor,nombre)
                empleado = self.empleado.buscar_empleado_nombre(cursor,nombre_empleado)
                
                if(resultado == None):
                    if(empleado != None):
                        query = "INSERT INTO proyectos (nombre,empleado_id) VALUES (%s,%s)"
                        cursor.execute(query,(nombre,empleado.id,))
                        conexion.commit()
                        self.logger.info(f"{nombre}-{nombre_empleado}: Registro almacenado correctamente")
                    else:
                        self.logger.error(f"{nombre}-{nombre_empleado}: El empleado no existe en la BD")
                else:
                    self.logger.error(f"{nombre}-{nombre_empleado}: El proyecto ya existe en al BD")

            except Exception as e:
                print(f"Error: {e}")

    
    def buscar_proyecto_nombre(self,cursor,nombre_proyecto):
        try:
            query = "SELECT id, nombre, empleado_id FROM proyectos WHERE nombre = %s"
            cursor.execute(query,(nombre_proyecto,))
            resultado = cursor.fetchone()

            if resultado != None:
            
                return Proyecto(*resultado)
            else: 
                return None
            
        except Exception as e:
            print(f"Error: {e}")

    

    def buscar_totalidad_proyectos(self,cursor):
        try:
            query = "SELECT p.id, p.nombre, e.nombre, d.nombre FROM proyectos p INNER JOIN empleados e ON p.empleado_id = e.id INNER JOIN departamentos d ON e.departamento_id = d.id"
            cursor.execute(query,())
            resultado = cursor.fetchall()
            if resultado != None:
                return resultado
            else:
                return None
            
        except Exception as e:
            print(f"Error: {e}")


    def actualizar_nombre_proyectos(self,conexion,cursor,nombre_departamento,viejo_nombre,nuevo_nombre):
        with self.lock:
            try:
                query = "UPDATE proyectos SET nombre = %s WHERE nombre = %s AND empleado_id IN ( SELECT e.id FROM empleados e INNER JOIN departamentos d ON e.departamento_id = d.id WHERE d.nombre = %s)"
                cursor.execute(query,(nuevo_nombre,viejo_nombre,nombre_departamento,))
                conexion.commit()

            except Exception as e:
                print(f"Error: {e}")


    def iniciar_logs(self,):
        logger = logging.getLogger('proyecto')
        logger.setLevel(logging.DEBUG)
        
        if not logger.hasHandlers():
            file_handler = logging.FileHandler(os.path.join("app/logs/", 'proyecto.log'))
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        self.logger = logger