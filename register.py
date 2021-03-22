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
    documento=datos.getvalue('documento')
    nombre=datos.getvalue('nombre')
    direccion=datos.getvalue('direccion')
    email=datos.getvalue('email')
    sexo=datos.getvalue('sexo')
    contraseña =datos.getvalue('contra')
    rol="user"
    telefono=datos.getvalue('telefono')


    usuario=Persona(documento,sexo,nombre,email,contraseña,telefono,direccion,rol)
    dao=UsuariosDao()
    if(dao.consultar(email,contraseña) is None):
        if(dao.registrar(usuario)):
            print(json.dumps('{"tipo":"OK","mensaje":"Usuario creado"}'))
        else:
            print(json.dumps('{"tipo":"error","mensaje":"Error al crear usuario"}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Ya existe un usuario con esa identificación o con ese correo"}'))
