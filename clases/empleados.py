from datetime import datetime
from tipoUsuario import TipoUsuario
from rut_chile import rut_chile
import re

class Empleados(TipoUsuario):  # Heredar de TipoUsuario

    def __init__(self, id_empleado, Nombre_empleado, fecha_contrato, fecha_nacimiento, salario, correo, telefono, direccion, id_tipo_usuario, rut_empleado):
        super().__init__(id_tipo_usuario)  #constructor de la clase padre
        self.id_empleado = id_empleado
        self.Nombre_empleado = Nombre_empleado
        self.fecha_contrato = fecha_contrato
        self.fecha_nacimiento = fecha_nacimiento
        self.salario = salario
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.rut_empleado = rut_empleado

    # este es el metodo para validar los rut
    def validar_rut(self):
        return rut_chile.is_valid_rut(self.rut_empleado)

    # metodo para validar el correo si creas mas clases que tengan q ver con este campo importa re y agrega esta funcion, es como para admitir caracteres especiales

    def validar_correo(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, self.correo)):  # Usar el atributo self.correo
            return True
        else:
            return False