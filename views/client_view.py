# client_console_view.py
from controllers.client_controller import add_cliente, get_clientes

def display_menu():
    print("\n--- Gestión de Clientes ---")
    print("1. Agregar Cliente")
    print("2. Listar Clientes")
    print("3. Salir")

def add_cliente_console():
    apellidos = input("Ingrese los apellidos: ").strip()
    nombres = input("Ingrese los nombres: ").strip()
    telefono = input("Ingrese el teléfono: ").strip()

    if not apellidos or not nombres or not telefono:
        print("Error: Todos los campos son obligatorios.")
        return

    try:
        add_cliente(apellidos, nombres, telefono)
        print("Cliente agregado correctamente.")
    except ValueError as e:
        print("Error:", e)

def list_clientes():
    print("\n--- Lista de Clientes ---")
    clientes = get_clientes()
    if clientes:
        print(f"{'Clave':<10}{'Apellidos':<20}{'Nombres':<20}{'Teléfono':<15}")
        print("-" * 65)
        for cliente in clientes:
            clave, apellidos, nombres, telefono = cliente
            print(f"{clave:<10}{apellidos:<20}{nombres:<20}{telefono:<15}")
    else:
        print("No hay clientes registrados.")

def main():
    while True:
        display_menu()
        choice = input("Seleccione una opción: ")
        if choice == "1":
            add_cliente_console()
        elif choice == "2":
            list_clientes()
        elif choice == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()

