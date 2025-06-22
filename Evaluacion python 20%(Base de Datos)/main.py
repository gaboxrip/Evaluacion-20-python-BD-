

import os
import time

from core.models import Base
from db.connection import engine
from core.views import *

OPT = {
    # Profesores
    "1": crear_profesor_vista,
    "2": mostrar_los_profesores_vista,
    "3": mostrar_profesor_por_id_vista,
    "4": actualizar_profesor_vista,
    "5": eliminar_profesor_vista,

    # Estudiantes
    "6": crear_estudiante_vista,
    "7": mostrar_los_estudiantes_vista,
    "8": mostrar_estudiante_por_id_vista,
    "9": actualizar_estudiante_vista,
    "10": eliminar_estudiante_vista,

    # Cursos
    "11": crear_curso_vista,
    "12": mostrar_los_cursos_vista,
    "13": mostrar_curso_por_id_vista,
    "14": actualizar_curso_vista,
    "15": eliminar_curso_vista,

    # Inscripciones
    "16": inscribir_estudiante_vista,
    "17": ver_cursos_estudiante_vista,
}


def wait_and_clear(s: int) -> None:
    time.sleep(s)
    os.system("cls" if os.name == "nt" else "clear")


def main():
    """Función principal."""
    while True:
        print("=== GESTIÓN ACADÉMICA ===\n")
        print("--- Profesores ---")
        print("1. Crear Profesor")
        print("2. Ver todos los Profesores")
        print("3. Ver Profesor por ID")
        print("4. Actualizar Profesor")
        print("5. Eliminar Profesor")

        print("\n--- Estudiantes ---")
        print("6. Crear Estudiante")
        print("7. Ver todos los Estudiantes")
        print("8. Ver Estudiante por ID")
        print("9. Actualizar Estudiante")
        print("10. Eliminar Estudiante")

        print("\n--- Cursos ---")
        print("11. Crear Curso")
        print("12. Ver todos los Cursos")
        print("13. Ver Curso por ID")
        print("14. Actualizar Curso")
        print("15. Eliminar Curso")

        print("\n--- Inscripciones ---")
        print("16. Inscribir Estudiante en Curso")
        print("17. Ver Cursos de un Estudiante")

        print("\n0. Salir")
        opt = input("\nSeleccione una opción: ").strip()

        if opt == "0":
            break
        elif opt in OPT:
            wait_and_clear(0)
            OPT[opt]()
            if int(opt) in range(2, 18):
                input("\nPresione una tecla para continuar...")
                wait_and_clear(0)
            else:
                wait_and_clear(1)
        else:
            print("❌ Opción inválida.")
            wait_and_clear(1)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    main()