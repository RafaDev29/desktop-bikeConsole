# analysis_console_view.py
from controllers.reports_controller import get_duracion_prestamos, get_ranking_clientes, get_preferencias_por_rodada, get_preferencias_por_color, get_preferencias_por_dia
import pandas as pd
import matplotlib.pyplot as plt

def display_menu():
    print("\n--- Análisis Descriptivo ---")
    print("1. Duración de los Préstamos")
    print("2. Ranking de Clientes")
    print("3. Preferencias por Rodada")
    print("4. Preferencias por Color")
    print("5. Preferencias por Día de la Semana")
    print("6. Exportar Datos a CSV")
    print("7. Exportar Datos a Excel")
    print("8. Salir")

def show_duracion_prestamos():
    stats = get_duracion_prestamos()
    if stats:
        print("\n--- Duración de los Préstamos ---")
        print(f"Media: {stats['media']:.2f}")
        print(f"Mediana: {stats['mediana']}")
        print(f"Moda: {stats['moda']}")
        print(f"Mínimo: {stats['minimo']}")
        print(f"Máximo: {stats['maximo']}")
        print(f"Desviación Estándar: {stats['desviacion']:.2f}")
        print(f"Cuartiles: {stats['cuartiles']}")
    else:
        print("No hay datos disponibles.")

def show_ranking_clientes():
    ranking = get_ranking_clientes()
    data = pd.DataFrame(ranking, columns=["Clave", "Nombre", "Teléfono", "Cantidad de Préstamos"])
    print(data)
    return data

def show_preferencias_rodada():
    preferencias = get_preferencias_por_rodada()
    data = pd.DataFrame(preferencias, columns=["Rodada", "Cantidad de Préstamos"])
    print(data)
    data.plot.pie(y="Cantidad de Préstamos", labels=data["Rodada"], autopct="%1.1f%%", legend=False)
    plt.title("Preferencias por Rodada")
    plt.show()
    return data

def show_preferencias_color():
    preferencias = get_preferencias_por_color()
    data = pd.DataFrame(preferencias, columns=["Color", "Cantidad de Préstamos"])
    print(data)
    data.plot.pie(y="Cantidad de Préstamos", labels=data["Color"], autopct="%1.1f%%", legend=False)
    plt.title("Preferencias por Color")
    plt.show()
    return data

def show_preferencias_dia():
    preferencias = get_preferencias_por_dia()
    data = pd.DataFrame(preferencias, columns=["Día de la Semana", "Cantidad de Préstamos"])
    print(data)
    data.plot.bar(x="Día de la Semana", y="Cantidad de Préstamos", legend=False)
    plt.title("Preferencias por Día de la Semana")
    plt.show()
    return data

def export_to_csv(data):
    if data is not None:
        data.to_csv("reporte.csv", index=False)
        print("Reporte exportado como reporte.csv.")
    else:
        print("No hay datos para exportar.")

def export_to_excel(data):
    if data is not None:
        data.to_excel("reporte.xlsx", index=False)
        print("Reporte exportado como reporte.xlsx.")
    else:
        print("No hay datos para exportar.")

def main():
    data = None
    while True:
        display_menu()
        choice = input("Seleccione una opción: ")
        if choice == "1":
            show_duracion_prestamos()
        elif choice == "2":
            data = show_ranking_clientes()
        elif choice == "3":
            data = show_preferencias_rodada()
        elif choice == "4":
            data = show_preferencias_color()
        elif choice == "5":
            data = show_preferencias_dia()
        elif choice == "6":
            export_to_csv(data)
        elif choice == "7":
            export_to_excel(data)
        elif choice == "8":
            print("Saliendo del análisis descriptivo...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()
