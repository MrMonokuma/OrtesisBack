#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from DAO.usuarioDao import UsuariosDao
from DAO.AdminDao import AdminDao
from DAO.models import Usuario
import json
import cgi
import os

print('Content-Type: text/json')
print('')
datos= cgi.FieldStorage()
if os.environ['REQUEST_METHOD']=="POST":
    email=datos.getvalue('email')
    contraseña =datos.getvalue('contra')
    usuariosdao=UsuariosDao()
    admindao = AdminDao()
    usuario = usuariosdao.consultar(email,contraseña)
    admin = admindao.consultar(email,contraseña)
    
    if(usuario is not None):
        print(json.dumps('{"tipo":"OK","mensaje":"Bienvenido/a, '+usuario.nombre+'","usuario":'+json.dumps(usuario.__dict__)+'}'))
    elif (admin is not None):
        print(json.dumps('{"tipo":"OK","mensaje":"Bienvenido/a, '+admin.nombre+'","usuario":'+json.dumps(admin.__dict__)+'}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Usuario o contrasena inválidos"}'))