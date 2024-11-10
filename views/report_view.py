


# report_console_view.py
from controllers.reports_controller import get_all_clients, get_all_units, get_retrasos, get_prestamos_por_retornar, get_prestamos_por_periodo
from datetime import datetime

def display_menu():
    print("\n--- Informes y Reportes ---")
    print("1. Clientes")
    print("2. Unidades")
    print("3. Retrasos")
    print("4. Préstamos por Retornar (Período)")
    print("5. Préstamos por Período")
    print("6. Salir")

def get_date(prompt):
    while True:
        date_str = input(f"{prompt} (mm-dd-yyyy): ")
        try:
            return datetime.strptime(date_str, "%m-%d-%Y")
        except ValueError:
            print("Fecha no válida. Inténtalo de nuevo.")

def generate_report(option):
    if option == "1":  # Clientes
        clients = get_all_clients()
        print(f"{'Clave':<10}{'Apellidos':<20}{'Nombres':<20}{'Teléfono':<15}")
        for client in clients:
            clave, apellidos, nombres, telefono = client
            print(f"{clave:<10}{apellidos:<20}{nombres:<20}{telefono:<15}")

    elif option == "2":  # Unidades
        units = get_all_units()
        print(f"{'Clave':<10}{'Rodada':<10}{'Color':<15}")
        for unit in units:
            clave, rodada, color = unit
            print(f"{clave:<10}{rodada:<10}{color:<15}")

    elif option == "3":  # Retrasos
        retrasos = get_retrasos()
        print(f"{'Unidad':<10}{'Rodada':<10}{'Color':<15}{'Cliente':<20}{'Fecha Préstamo':<15}{'Días Retraso':<15}")
        for retraso in retrasos:
            unidad, rodada, color, cliente, fecha_prestamo, dias_retraso = retraso
            print(f"{unidad:<10}{rodada:<10}{color:<15}{cliente:<20}{fecha_prestamo:<15}{dias_retraso:<15}")

    elif option == "4" or option == "5":  # Préstamos por Retornar o por Período
        fecha_inicio = get_date("Ingrese la fecha de inicio")
        fecha_fin = get_date("Ingrese la fecha de fin")

        if option == "4":
            prestamos = get_prestamos_por_retornar(fecha_inicio, fecha_fin)
            print(f"{'Unidad':<10}{'Rodada':<10}{'Fecha Préstamo':<15}{'Cliente':<20}{'Teléfono':<15}")
        else:
            prestamos = get_prestamos_por_periodo(fecha_inicio, fecha_fin)
            print(f"{'Unidad':<10}{'Rodada':<10}{'Fecha Préstamo':<15}{'Cliente':<20}{'Teléfono':<15}")

        for prestamo in prestamos:
            unidad, rodada, fecha_prestamo, cliente, telefono = prestamo
            print(f"{unidad:<10}{rodada:<10}{fecha_prestamo:<15}{cliente:<20}{telefono:<15}")

def main():
    while True:
        display_menu()
        choice = input("Seleccione una opción: ")
        if choice in ["1", "2", "3", "4", "5"]:
            generate_report(choice)
        elif choice == "6":
            print("Saliendo de Informes y Reportes...")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main()
