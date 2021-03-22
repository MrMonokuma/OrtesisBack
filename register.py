#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from DAO.usuarioDao import UsuariosDao
from DAO.models import Persona
import json
import cgi
import os

print('Content-Type: text/json')
print('')

if os.environ['REQUEST_METHOD']=="POST":
    datos= cgi.FieldStorage()
    nombre=datos.getvalue('nombre')
    documento=datos.getvalue('documento')
    email=datos.getvalue('email')
    telefono=datos.getvalue('telefono')
    contraseña =datos.getvalue('contra')
    sexo=datos.getvalue('sexo')
    direccion=datos.getvalue('direccion')
    rol="user"

    usuario=Persona(documento,sexo,nombre,email,contraseña,telefono,direccion,rol)
    dao=UsuariosDao()
    if(dao.consultar(email,contraseña) is None):
        if(dao.registrar(usuario)):
            print(json.dumps('{"tipo":"OK","mensaje":"Usuario creado"}'))
        else:
            print(json.dumps('{"tipo":"error","mensaje":"Error al crear usuario"}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Ya existe un usuario con esa identificación o con ese correo"}'))
