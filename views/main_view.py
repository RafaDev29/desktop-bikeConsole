# main_console_view.py
def display_main_menu():
    print("\n--- Sistema de Renta de Bicicletas ---")
    print("1. Gestión de Clientes")
    print("2. Gestión de Unidades")
    print("3. Gestión de Préstamos")
    print("4. Registro de Retorno")
    print("5. Informes y Reportes")
    print("6. Análisis Descriptivo")
    print("7. Salir")

def open_client_view():
    from client_console_view import main as client_main
    client_main()

def open_unit_view():
    from unit_console_view import main as unit_main
    unit_main()

def open_loan_view():
    from loan_console_view import main as loan_main
    loan_main()

def open_return_view():
    # Importa y ejecuta el código de la vista de retorno en consola
    from return_console_view import main as return_main
    return_main()

def open_report_view():
    # Importa y ejecuta el código de la vista de reportes en consola
    from report_console_view import main as report_main
    report_main()

def open_analysis_view():
    # Importa y ejecuta el código de la vista de análisis en consola
    from analysis_console_view import main as analysis_main
    analysis_main()

def main():
    while True:
        display_main_menu()
        choice = input("Seleccione una opción: ")
        if choice == "1":
            open_client_view()
        elif choice == "2":
            open_unit_view()
        elif choice == "3":
            open_loan_view()
        elif choice == "4":
            open_return_view()
        elif choice == "5":
            open_report_view()
        elif choice == "6":
            open_analysis_view()
        elif choice == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
