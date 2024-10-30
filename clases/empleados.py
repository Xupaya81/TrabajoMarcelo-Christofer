from datetime import datetime
from tipo_usuario import Tipo_Usuario 
from rut_chile import rut_chile
import re

class Empleados():
 
 def __init__(self, id_empleado, Nombre_empleado, fecha_contrato, fecha_nacimiento, salario, correo, telefono, direccion, id_tipo_usuario, rut_empleado):      
  super().__init__(id_tipo_usuario)
  self. id_empleado = id_empleado
  self. Nombre_empleado = Nombre_empleado
  self. fecha_contrato = fecha_contrato
  self. fecha_nacimiento = fecha_nacimiento
  self. salario = salario 
  self. correo = correo
  self. telefono = telefono
  self. direccion = direccion
  self. rut_empleado = rut_empleado

  def validar_rut(self):
        return rut_chile.is_valid_rut(self.rut_empleado)
  
  def validar_correo(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, self.correo_usuario)):
            return True 
        else:
            return False
 