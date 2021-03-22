#!/usr/bin/python3
import mysql.connector
from mysql.connector import errorcode
from DAO.AdminDao import AdminDao
from DAO.models import Persona
import json
import cgi
import os

print('Content-Type: text/json')
print('')

if os.environ['REQUEST_METHOD']=="POST":
    datos= cgi.FieldStorage()
    nombre=datos.getvalue('n')
    email=datos.getvalue('email')
    telefono=datos.getvalue('telefono')
    contraseña =datos.getvalue('contra')
    documento=datos.getvalue('documento')
    sexo=datos.getvalue('sexo')
    direccion=datos.getvalue('direccion')
    rol=datos.getvalue('rol')

    administrador=Persona(documento,sexo,nombre,email,contraseña,telefono,direccion,rol)
    dao=AdminDao()
    if(dao.consultar(email,contraseña) is None):
        if(dao.registrar(administrador)):
            print(json.dumps('{"tipo":"OK","mensaje":"administrador creado"}'))
        else:
            print(json.dumps('{"tipo":"error","mensaje":"Error al crear administrador"}'))
    else:
        print(json.dumps('{"tipo":"error","mensaje":"Ya existe un administrador con esa identificación o con ese correo"}'))