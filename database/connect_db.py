import cx_Oracle

class connect():

    def __init__(self):
        host = "localhost"
        user = "system"
        passw = "1234"
        tsname = "xe"

        try:
            self.conexion = cx_Oracle.connect(user, passw, host+"/"+tsname)
        except Exception as error:
            print("No se pudo conectar a la base de datos. Error: ")
        else:
            print("Conexion Establecida!!!")

    def sentenciaCompuesta(self, sentencia):
        cursor = self.conexion.cursor()
        cursor.execute(sentencia)
        datos = cursor.fetchall()
        cursor.close
        return datos

    def close(self):
        self.conexion.close()

    def commint(self):
        self.conexion.commit()
    
    def sentenciaSimple(self, sentencia):
        cursor = self.conexion.cursor()
        cursor.execute(sentencia)
        cursor.close() 

""" if __name__ == "__main__":
    conexion = connect()
    for fila in conexion.sentenciaCompuesta("select sysdate from dual"):
        print(fila)
    conexion.close() """