# loan_console_view.py
from controllers.loan_controller import add_prestamo, get_prestamos_activos
from controllers.client_controller import get_clientes
from controllers.unit_controller import get_unidades

def display_menu():
    print("\n--- Gestión de Préstamos ---")
    print("1. Registrar Préstamo")
    print("2. Listar Préstamos Activos")
    print("3. Salir")

def display_clientes():
    clientes = get_clientes()
    print("\nSeleccione un cliente:")
    for idx, cliente in enumerate(clientes, start=1):
        print(f"{idx}. {cliente[0]} - {cliente[1]} {cliente[2]}")
    choice = int(input("Ingrese el número del cliente: ")) - 1
    return clientes[choice][0]

def display_unidades():
    unidades = get_unidades()
    print("\nSeleccione una unidad:")
    for idx, unidad in enumerate(unidades, start=1):
        print(f"{idx}. {unidad[0]} - {unidad[1]} ({unidad[2]})")
    choice = int(input("Ingrese el número de la unidad: ")) - 1
    return unidades[choice][0]

def register_prestamo():
    try:
        clave_cliente = display_clientes()
        clave_unidad = display_unidades()
        dias_prestamo = int(input("Ingrese los días de préstamo: "))
        
        add_prestamo(clave_unidad, clave_cliente, dias_prestamo)
        print("Préstamo registrado correctamente.")
    except ValueError as e:
        print("Error:", e)

def list_prestamos_activos():
    print("\n--- Préstamos Activos -----------")
    prestamos = get_prestamos_activos()
    if prestamos:
        for prestamo in prestamos:
            print(prestamo)
    else:
        print("No hay préstamos activos. :(")

def main():
    while True:
        display_menu()
        choice = input("Seleccione una opción: ")
        if choice == "1":
            register_prestamo()
        elif choice == "2":
            list_prestamos_activos()
        elif choice == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente, porfavor. ")

if __name__ == "__main__":
    main()
