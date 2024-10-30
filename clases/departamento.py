from empleados import id_empleado

class Departamento():
    def __init__(self,id_departamento, nombre, id_empleado):
        super().__init__(id_empleado)
        self. id_departamento= id_departamento
        self. nombre= nombre
        self. id_empleado= id_empleado