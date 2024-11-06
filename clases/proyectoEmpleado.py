class ProyectoEmpleado:
    """
    Clase que representa la relación entre un proyecto y un empleado.

    Atributos:
        id_proyecto_empleado (int): ID de la relación proyecto-empleado.
        id_empleado (int): ID del empleado.
        id_proyecto (int): ID del proyecto.
    """
    def __init__(self, id_proyecto_empleado, id_empleado, id_proyecto):
        self.id_proyecto_empleado = id_proyecto_empleado
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto

    def __str__(self):
      return f"ID Proyecto Empleado: {self.id_proyecto_empleado}, ID Empleado: {self.id_empleado}, ID Proyecto: {self.id_proyecto}"