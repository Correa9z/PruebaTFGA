from infra.conexion_bd import ConexionBd
import logging

class Departamento:

    conexion = ConexionBd()
        

    def __init__(self,id,nombre):
        self.id = id
        self.nombre = nombre 
    

    def crear_departamento(self,nombre):
        try:
            Departamento.iniciar_logs()
            resultado = Departamento.buscar_departamento_nombre(self,nombre)
            cursor = self.conexion.conectar_bd()

            if resultado == None:
                query = "INSERT INTO departamentos (nombre) VALUES (%s)"
                cursor.execute(query,(nombre,))
                self.conexion.conexion.commit()
                logging.info(f"{nombre}: Registro almacenado correctamente")
            else:
                logging.error(f"{nombre}: El departamento ya existe en al BD")

        except Exception as e:
            print(f"Error: {e}")

        finally:
            self.conexion.cerrar_bd(cursor)

    
    def buscar_departamento_nombre(self,nombre_departamento):
        try:
            cursor = self.conexion.conectar_bd()
            query = "SELECT id, nombre FROM departamentos WHERE nombre = %s"
            cursor.execute(query,(nombre_departamento,))
            resultado = cursor.fetchone()
            
            if resultado != None:
                return Departamento(*resultado)
            else:
                return None

        except Exception as e:
            print(f"Error: {e}")

        finally:
            self.conexion.cerrar_bd(cursor)


    def iniciar_logs():
        logging.basicConfig(
        filename='departamento.log',             # Nombre del archivo de logs
        level=logging.DEBUG,            # Nivel de registro: DEBUG, INFO, WARNING, ERROR, CRITICAL
        format='%(asctime)s - %(levelname)s - %(message)s',  # Formato del mensaje
        datefmt='%Y-%m-%d %H:%M:%S'     # Formato de la fecha
    )
        


