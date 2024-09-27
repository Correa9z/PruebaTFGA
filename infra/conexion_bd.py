import mysql.connector


class ConexionBd:

    conexion = ""
    cursor = ""

    def conectar_bd(self):
        try:
            self.conexion = mysql.connector.connect(host='localhost', port='3306',user='root',password='',database='pruebaT')

            self.cursor = self.conexion.cursor()

            return self.cursor

        except Exception as e:
            print("Error: ",e)
    
    def cerrar_bd(self,cursor):
        cursor.close()
        self.conexion.close()
