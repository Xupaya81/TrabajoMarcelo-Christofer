
empleados = []

def mostrarmenu():
    print("\nMenu de Asignación de Empleados")
    print("1. Agregar Empleado")
    print("2. Ver Empleados")
    print("3. Eliminar Empleado")
    print("4. Salir")

def agregarempleado():
    nombre = input("Ingrese el nombre del empleado: ")
    empleados.append(nombre)
    print(f"Empleado '{nombre}' agregado.")

def verempleados():
    if empleados:
        print("\nLista de Empleados:")
        for idx, empleado in enumerate(empleados, start=1):
            print(f"{idx}. {empleado}")
    else:
        print("No hay empleados en la lista.")

def eliminarempleado():
    ver_empleados()
    if empleados:
        try:
            idx = int(input("Ingrese el número del empleado a eliminar: ")) - 1
            if 0 <= idx < len(empleados):
                empleado_eliminado = empleados.pop(idx)
                print(f"Empleado '{empleado_eliminado}' eliminado.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            agregar_empleado()
        elif opcion == '2':
            ver_empleados()
        elif opcion == '3':
            eliminar_empleado()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, por favor intente nuevamente.")

if __name == "__main":
    main()
1222656126