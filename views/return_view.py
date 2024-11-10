# return_console_view.py
from controllers.return_controller import get_prestamos_pendientes, registrar_retorno
from datetime import datetime

def display_menu():
    print("\n--- Retorno de Unidades ---")
    print("1. Ver Préstamos Pendientes")
    print("2. Registrar Retorno")
    print("3. Salir")

def list_prestamos_pendientes():
    print("\n--- Préstamos Pendientes ---")
    prestamos = get_prestamos_pendientes()
    if prestamos:
        print(f"{'Folio':<10}{'Clave Unidad':<15}{'Rodada':<10}{'Color':<10}{'Clave Cliente':<15}{'Nombre Cliente':<20}{'Fecha Préstamo':<15}{'Días de Préstamo':<15}")
        for prestamo in prestamos:
            folio, clave_unidad, rodada, color, clave_cliente, nombre_cliente, fecha_prestamo, dias_prestamo = prestamo
            print(f"{folio:<10}{clave_unidad:<15}{rodada:<10}{color:<10}{clave_cliente:<15}{nombre_cliente:<20}{fecha_prestamo:<15}{dias_prestamo:<15}")
    else:
        print("No hay préstamos pendientes.")

def registrar_retorno_console():
    list_prestamos_pendientes()
    folio_prestamo = input("Ingrese el folio del préstamo para registrar el retorno: ").strip()
    fecha_retorno = input("Ingrese la fecha de retorno (mm-dd-yyyy): ").strip()

    # Validar la fecha de retorno
    try:
        datetime.strptime(fecha_retorno, "%m-%d-%Y")
        registrar_retorno(folio_prestamo, fecha_retorno)
        print("Retorno registrado correctamente.")
    except ValueError:
        print("Error: Formato de fecha no válido. Use el formato mm-dd-yyyy.")

def main():
    while True:
        display_menu()
        choice = input("Seleccione una opción: ")
        if choice == "1":
            list_prestamos_pendientes()
        elif choice == "2":
            registrar_retorno_console()
        elif choice == "3":
            print("Saliendo del módulo de Retorno de Unidades...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
