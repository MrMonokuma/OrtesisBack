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
            sql="insert into Persona (idPersona, nombrePersona, direccionPersona, correoPersona, generoPersona, clavePersona, rol, telefono) values ('"+usuario.documento+"','"+usuario.nombre+"','"+usuario.direccion+"','"+usuario.correo+"','"+usuario.sexo+"','"+usuario.contraseña+"','"+usuario.rol+"','"+usuario.telefono+"');"
            cursor.execute(sql)
            #args=[usuario.documento,usuario.sexo,usuario.nombre,usuario.direccion,usuario.email,usuario.telefono,usuario.contraseña]
            #cursor.callproc("crearUsuario",args)
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
            sql = "select * from Persona where correoPersona='"+email+"' and clavePersona=sha('"+password+"');"
            cursor.execute(sql)
            usuario=None
            for row in cursor:
                documento=row[0]
                nombre=row[1]
                direccion=row[2]
                email=row[3]
                sexo=row[4]
                contraseña=row[5]
                rol=row[6]
                telefono=row[7]
                usuario=Persona(documento,nombre,direccion,email,sexo,contraseña,rol,telefono)
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