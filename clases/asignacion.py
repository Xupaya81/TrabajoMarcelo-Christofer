class asignacion ():
    def __init__(self, id_asignacion, id_departamento, id_empleado):
        self.id_asignacion = id_asignacion
        self.id_departamento = id_departamento
        self.id_empleado = id_empleado

    def __str__(self):
        """
        Devuelve una representación legible del objeto Asignacion.

        Returns:
            str: Cadena con la información de la asignación.
        """
        return f"ID de Asignación: {self.id_asignacion}, ID del Departamento: {self.id_departamento}, ID del Empleado: {self.id_empleado}"