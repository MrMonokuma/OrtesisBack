class Persona:
    def __init__(self,documento,sexo,nombre, email, contraseña, telefono, direccion, rol):
        self.documento=documento
        self.nombre=nombre
        self.email=email
        self.contraseña=contraseña
        self.telefono=telefono
        self.direccion=direccion
        self.sexo=sexo
        self.rol=rol
    def __hash__(self):
        return hash(self.email)
    
class Categoria:
    def __init__(self,nombre,imagen):
        self.idCategoria=0
        self.nombre=nombre
        self.imagen=imagen

class Producto:
    def __init__(self,idCategoria,nombre,unidad,precio,imagen):
        self.nombre=nombre
        self.unidad=unidad
        self.precio=precio
        self.imagen=imagen
        self.idCategoria=idCategoria
        self.idProducto=0

class Permiso:
    def __init__(self,nombrePermiso):
        self.idPermiso=0
        self.nombrePermiso=nombrePermiso

class Carrito:
    def __init__(self,idDomiciliario,idUsuario,direccionDestino,listaProductosACompra):
        self.codigoPedido = 0
        self.idDomiciliario=idDomiciliario
        self.idUsuario=idUsuario
        self.direccionDestino=direccionDestino
        self.listaProductosACompra=listaProductosACompra

class ProductoACompra:
    def __init__(self,producto,cantidad):
        self.producto=producto
        self.cantidad=cantidad