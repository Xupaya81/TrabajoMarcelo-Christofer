class Departamento():
    def __init__(self, id_departamento, nombre,):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.empleados =[]  # Inicializar la lista de empleados
        self. departamentos =[]
    def agregar_empleado(self, id_empleado):
        # Verificamos si el ID del empleado ya está en la lista
        if id_empleado not in self.empleados:
            self.empleados.append(id_empleado)
            print(f'Empleado con ID {id_empleado} agregado al departamento {self.nombre}.')
        else:
            print(f'El empleado con ID {id_empleado} ya está en el departamento {self.nombre}.')

    def mostrar_empleados(self):
        print(f'Empleados en el departamento {self.nombre}: {self.empleados}')


departamento_ventas = Departamento(1, "Ventas")
departamento_ventas.agregar_empleado(101)  # Agregar empleado con ID 101
departamento_ventas.agregar_empleado(102)  # Agregar empleado con ID 102
departamento_ventas.agregar_empleado(101)  # Intentar agregar el mismo empleado nuevamente
departamento_ventas.mostrar_empleados()  # Mostrar empleados en el departamento

        #falta agregar una funcion que agregre un empleado a un departamento, pensaba que podriamos hacerlo solo con su id para omitir tanto webeo