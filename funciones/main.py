from mysql.connector import (connection, Error)
from tabulate import tabulate

def agregar_empleado(cnx):
    """
    Agrega un nuevo empleado a la base de datos.
    """

    nombre = input("Nombre empleado: ")
    fecha_contrato = input("Fecha de contrato (YYYY-MM-DD): ")
    fecha_nacimiento = input("Fecha de nacimiento (YYYY-MM-DD): ")
    salario = int(input("Ingrese salario: "))
    correo = input("Correo: ")
    telefono = int(input("Telefono: "))
    direccion = input("Dirección: ")
    id_tipo = int(input("ID tipo: "))
    rut = input("Rut empleado: ")

    try:
        cursor = cnx.cursor()
        cursor.execute(
            "INSERT INTO empleados (Nombre, FechaContrato, FechaNacimiento, Salario, Correo, Telefono, Direccion, IdTipo, Rut) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (nombre, fecha_contrato, fecha_nacimiento, salario, correo, telefono, direccion, id_tipo, rut))
        cnx.commit()
        print(f"Colaborador {nombre} agregado.")
    except Error as err:
        print(f"Error al agregar empleado: {err}")

def asignar_departamento_a_empleado(cnx):
    """
    Asigna un departamento a un empleado existente.
    """
    try:
        # Mostrar la lista de empleados
        cursor = cnx.cursor()
        cursor.execute("SELECT IdEmpleado, Nombre FROM Empleados")
        empleados = cursor.fetchall()

        print("\n--- Empleados ---")
        for empleado in empleados:
            print(f"{empleado[0]}. {empleado[1]}")

        id_empleado = int(input("Seleccione el ID del empleado: "))

        # Mostrar la lista de departamentos
        cursor.execute("SELECT IdDepartamento, Nombre FROM Departamento")
        departamentos = cursor.fetchall()

        print("\n--- Departamentos ---")
        for departamento in departamentos:
            print(f"{departamento[0]}. {departamento[1]}")

        id_departamento = int(input("Seleccione el ID del departamento: "))

        # Asignar el departamento al empleado (asumiendo que tienes una tabla para la relación)
        cursor.execute(
            "INSERT INTO Asignacion (IdDepartamento, IdEmpleado) VALUES (%s, %s)",
            (id_departamento, id_empleado))
        cnx.commit()
        print(f"Empleado {id_empleado} asignado al departamento {id_departamento}.")
    except Error as err:
        print(f"Error al asignar departamento: {err}")

def menu_empleado(cnx):
    """
    Muestra el menú de opciones para gestionar empleados.
    """
    while True:
        print("\n--- Menú administrador ---")
        print("___________________________________")
        print("1. Agregar empleado")
        print("2. Asignar departamento a empleado")  # Nueva opción
        print("3. Eliminar empleado")
        print("4. Buscar empleado")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_empleado(cnx)
        elif opcion == '2':
            asignar_departamento_a_empleado(cnx)  # Llamar a la nueva función
        elif opcion == '3':
            eliminar_empleado(cnx)
        elif opcion == '4':
            buscar_empleado(cnx)
        elif opcion == '5':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

def eliminar_empleado(cnx):
    """
    Elimina un empleado de la base de datos.
    """
    id_empleado = int(input("Ingrese el ID del empleado a eliminar: "))
    try:
        cursor = cnx.cursor()
        cursor.execute("DELETE FROM empleados WHERE IdEmpleado = %s", (id_empleado,))
        cnx.commit()
        print(f"Empleado con ID {id_empleado} eliminado correctamente.")
    except Error as err:
        print(f"Error al eliminar empleado: {err}")

def buscar_empleado(cnx):
    """
    Busca empleados por nombre en la base de datos.
    """
    nombre = input("Ingrese el nombre del empleado a buscar: ")
    try:
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM empleados WHERE Nombre LIKE %s", ('%' + nombre + '%',))
        empleados = cursor.fetchall()
        if empleados:
            for empleado in empleados:
                # Formatear la salida como desees, por ejemplo:
                print("\nInformación del empleado:")
                print(f"ID: {empleado[0]}")
                print(f"Nombre: {empleado[1]}")
                # ... (mostrar otros campos)
        else:
            print(f"No se encontraron empleados con el nombre '{nombre}'")
    except Error as err:
        print(f"Error al buscar empleados: {err}")


def menu(cnx):
    while True:
        print("\nMenú principal")
        print("1. Menú empleado")
        print("2. Salir")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            menu_empleado(cnx)
        elif opcion == "2":
            break
        else:
            print("Opcion no valida")

def main():
    cnx = connection.MySQLConnection(
        user='root',
        password='',
        host='localhost',
        database='gestion_empleados',
        port=3306
    )

    menu(cnx)  # Llamar a la función menu

    cnx.close()

if __name__ == "__main__":
    main()