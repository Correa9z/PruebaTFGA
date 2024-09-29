from threading import Lock
import logging
import os

class Departamento:

    logger = ""        

    def __init__(self,id,nombre):
        print("Se creo un departamento")
        self.id = id
        self.nombre = nombre 
        self.lock = Lock()
    

    def crear_departamento(self,conexion,cursor,nombre):
        with self.lock:
            try:
                
                resultado = Departamento.buscar_departamento_nombre(self,cursor,nombre)
                
                if (resultado == None) and (cursor != None):
                    query = "INSERT INTO departamentos (nombre) VALUES (%s)"
                    cursor.execute(query,(nombre,))
                    conexion.commit()
                    self.logger.info(f"{nombre}: Registro almacenado correctamente")
                else:
                    self.logger.error(f"{nombre}: El departamento ya existe en al BD")

            except Exception as e:
                print(f"Error: {e}")

    
    def buscar_departamento_nombre(self,cursor,nombre_departamento):
        try:
            query = "SELECT id, nombre FROM departamentos WHERE nombre = %s"
            cursor.execute(query,(nombre_departamento,))
            resultado = cursor.fetchone()
            
            if resultado != None:
                return Departamento(*resultado)
            else:
                return None

        except Exception as e:
            print(f"Error: {e}")



    def iniciar_logs(self,):
        logger = logging.getLogger('departamento')
        logger.setLevel(logging.DEBUG)
        
        if not logger.hasHandlers():
            file_handler = logging.FileHandler(os.path.join("app/logs/", 'departamento.log'))
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        self.logger = logger
        