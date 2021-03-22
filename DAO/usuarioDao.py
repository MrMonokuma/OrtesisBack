import mysql.connector
from mysql.connector import errorcode
from dao import dao
from models import Persona
class UsuariosDao(dao):
    """
    Clase de objeto de acceso a datos de los usuarios
    """
    def registrar(self,usuario):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            args=[usuario.documento,usuario.sexo,usuario.nombre,usuario.direccion,usuario.email,usuario.telefono,usuario.contraseña]
            cursor.callproc("crearUsuario",args)
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            return False

    def consultar(self,email,password):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from PERSONA where email='"+email+"' and contraseña=sha('"+password+"');"
            cursor.execute(sql)
            usuario=None
            for row in cursor:
                documento=row[0]
                sexo=row[1]
                nombre=row[2]
                email=row[3]
                contraseña=row[4]
                telefono=row[5]
                direccion=row[6]
                rol=row[7]
                usuario=Persona(documento,sexo,nombre,email,contraseña,telefono,direccion,rol)
            cursor.close()
            cnx.close()
            return usuario
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

    def actualizar(self,usuario):
        pass
    def consultarPorId(self,documento):
        pass