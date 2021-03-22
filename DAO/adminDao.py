import mysql.connector
from mysql.connector import errorcode
from dao import dao
from models import Persona
class AdminDao(dao):
    """
    Clase de objeto de acceso a datos de los administradors
    """
    def registrar(self,administrador):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            args=[administrador.documento,administrador.tipoDocumento,administrador.nombre,administrador.direccion,administrador.email,administrador.telefono,administrador.contraseña]
            cursor.callproc("crearAdministrador",args)
            for permiso in administrador.permisos:
                sql = "insert into ADMINISTRADOR_has_PERMISO (ADMINISTRADOR_PERSONA_idPERSONA,PERMISO_idPERMISO)  values (%s,%s);"
                cursor.execute(sql,(administrador.documento,permiso))
            cnx.commit()
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

    def consultar(self,email,password):
        try:
            cnx = super().connectDB()
            cursor = cnx.cursor()
            sql = "select * from PERSONA where email='"+email+"' and contraseña=sha('"+password+"') and rol='admin';"
            cursor.execute(sql)
            administrador=None
            for row in cursor:
                documento=row[0]
                sexo=row[1]
                nombre=row[2]
                email=row[3]
                contraseña=row[4]
                telefono=row[5]
                direccion=row[6]
                rol=row[7]
                administrador=Persona(documento,sexo,nombre,email,contraseña,telefono,direccion,rol)
            cursor.close()
            cnx.close()
            return administrador
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            return None

    def actualizar(self,administrador):
        pass
    def consultarPorId(self,documento):
        pass