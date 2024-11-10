# unit_console_view.py
from controllers.unit_controller import add_unidad, get_unidades

def display_menu():
    print("\n--- Gestión de Unidades ---")
    print("1. Agregar Unidad")
    print("2. Listar Unidades")
    print("3. Salir")

def add_unidad_console():
    try:
        rodada = int(input("Ingrese la rodada (20, 26, 29): "))
        if rodada not in [20, 26, 29]:
            print("Error: Rodada no válida. Debe ser 20, 26 o 29.")
            return
        color = input("Ingrese el color: ").strip()

        if not color:
            print("Error: El campo 'Color' es obligatorio.")
            return

        add_unidad(rodada, color)
        print("Unidad agregada correctamente.")
    except ValueError as e:
        print("Error:", e)

def list_unidades():
    print("\n--- Lista de Unidades ---")
    unidades = get_unidades()
    if unidades:
        print(f"{'Clave':<10}{'Rodada':<10}{'Color':<15}")
        print("-" * 35)
        for unidad in unidades:
            clave, rodada, color = unidad
            print(f"{clave:<10}{rodada:<10}{color:<15}")
    else:
        print("No hay unidades en este momento registradas.")

def main():
    while True:
        display_menu()
        choice = input("Seleccione una opción: ")
        if choice == "1":
            add_unidad_console()
        elif choice == "2":
            list_unidades()
        elif choice == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
