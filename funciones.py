from mysql.connector import (connection)
from tabulate import tabulate

#Funciones agregar empleado
def agregarEmpleado(cnx):
    id_empleado = int(input("ID empleado: "))
    nombre = input("Nombre empleado: ")
    fecha_contrato = input("Fecha de contrato: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    salario = int(input("Ingrese salario: "))
    correo = input("Correo: ")
    telefono = int(input("Telefono: "))
    direccion = input("Dirección: ")
    id_tipo = int(input("ID tipo: "))
    rut = input("Rut empleado: ")
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO empleados (id_empleado, nombre, fecha_contrato, fecha_nacimiento, salario, correo, telefono, direccion, id_tipo, rut) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (id_empleado, nombre, fecha_contrato, fecha_nacimiento, salario, correo, telefono, direccion, id_tipo, rut)
    )   
    cnx.commit()
    print(f"Colaborador {nombre}, agregado.")

def verEmpleado(cnx):
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM empleados")
    empleado = cursor.fetchall()
    headers = ["ID","Nombre","Fecha Contrato","Fecha Nacimiento","Salario","Correo","Telefono","Direccion","RUT"]
    print(tabulate(empleado, headers=headers, tablefmt="pretty"))

def eliminarEmpleado(cnx):
    id_empleado = int(input("ID empleado: "))
    cursor = cnx.cursor()
    cursor.execute("DELETE FROM empleados WHERE = %s", (id_empleado))
    cnx.commit()
    print("Colaborador eliminado correctamente.")

def menu_empleado(cnx):
    while True:
        print("\nMenu empleados")
        print("1. Agregar empleado")
        print("2. Ver empleado")
        print("3. Eliminar empleado")
        print("4. Volver al menu principal")
        
        opcion = input("Seleccione su opción: ")
        
        if opcion == "1":
            agregarEmpleado(cnx)
        elif opcion == "2":
            verEmpleado(cnx)
        elif opcion == "3":
            eliminarEmpleado(cnx)
        elif opcion == "4":
            return
        else:
            print("Opcion no valida.")
        
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
        host='127.0.0.1', 
        database='marcelodb',
        port = 3306
        )
    cursor = cnx.cursor()
    cursor.execute(menu(cnx))
    cnx.close()

if __name__ == "__main__":
    main()