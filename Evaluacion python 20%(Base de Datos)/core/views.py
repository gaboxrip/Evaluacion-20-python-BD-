from db.connection import db_session
from core.controllers import *
from core.models import Estudiante, Profesor, Curso

def crear_estudiante_vista() -> None:
    print("=== Crear nuevo Estudiante ===")
    nombre = input("Nombre del estudiante: ").strip()

    with db_session() as session:
        try:
            estudiante = crear_estudiante(session, nombre)
            print(f"✅ Estudiante creado: {estudiante.nombre}")
        except ValueError as e:
            print(f"❌ Error: {e}")

def mostrar_los_estudiantes_vista() -> None:
    print("=== Lista de Estudiantes ===")
    with db_session() as session:
        estudiantes = mostrar_los_estudiantes(session)
        for e in estudiantes:
            print(f"{e.id}: {e.nombre}")

def mostrar_estudiante_por_id_vista() -> None:
    print("=== Buscar Estudiante por ID ===")
    eid = int(input("ID del estudiante: ").strip())
    with db_session() as session:
        estudiante = mostrar_estudiante_por_id(session, eid)
        if estudiante:
            print(f"{estudiante.id}: {estudiante.nombre}")
        else:
            print("❌ Estudiante no encontrado.")

def actualizar_estudiante_vista() -> None:
    print("=== Actualizar Estudiante ===")
    eid = int(input("ID del estudiante: ").strip())
    nuevo_nombre = input("Nuevo nombre: ").strip()

    with db_session() as session:
        try:
            estudiante = actualizar_estudiante(session, eid, nuevo_nombre)
            print(f"✅ Estudiante actualizado: {estudiante.nombre}")
        except ValueError as e:
            print(f"❌ Error: {e}")

def eliminar_estudiante_vista() -> None:
    print("=== Eliminar Estudiante ===")
    eid = int(input("ID del estudiante a eliminar: ").strip())

    with db_session() as session:
        try:
            eliminar_estudiante(session, eid)
            print("✅ Estudiante eliminado.")
        except ValueError as e:
            print(f"❌ Error: {e}")

def crear_profesor_vista() -> None:
    print("=== Crear nuevo Profesor ===")
    nombre = input("Nombre del profesor: ").strip()

    with db_session() as session:
        try:
            profesor = crear_profesor(session, nombre)
            print(f"✅ Profesor creado: {profesor.nombre}")
        except ValueError as e:
            print(f"❌ Error: {e}")

def mostrar_los_profesores_vista() -> None:
    print("=== Lista de Profesores ===")
    with db_session() as session:
        profesores = mostrar_los_profesores(session)
        for p in profesores:
            print(f"{p.id}: {p.nombre}")

def mostrar_profesor_por_id_vista() -> None:
    print("=== Buscar Profesor por ID ===")
    pid = int(input("ID del profesor: ").strip())
    with db_session() as session:
        profesor = mostrar_profesor_por_id(session, pid)
        if profesor:
            print(f"{profesor.id}: {profesor.nombre}")
        else:
            print("❌ Profesor no encontrado.")

def actualizar_profesor_vista() -> None:
    print("=== Actualizar Profesor ===")
    pid = int(input("ID del profesor: ").strip())
    nuevo_nombre = input("Nuevo nombre: ").strip()

    with db_session() as session:
        try:
            profesor = actualizar_profesor(session, pid, nuevo_nombre)
            print(f"✅ Profesor actualizado: {profesor.nombre}")
        except ValueError as e:
            print(f"❌ Error: {e}")

def eliminar_profesor_vista() -> None:
    print("=== Eliminar Profesor ===")
    pid = int(input("ID del profesor a eliminar: ").strip())

    with db_session() as session:
        try:
            eliminar_profesor(session, pid)
            print("✅ Profesor eliminado.")
        except ValueError as e:
            print(f"❌ Error: {e}")

def crear_curso_vista() -> None:
    print("=== Crear nuevo Curso ===")
    nombre = input("Nombre del curso: ").strip()

    with db_session() as session:
        profesores = mostrar_los_profesores(session)
        for p in profesores:
            print(f"{p.id}: {p.nombre}")
        profesor_id = int(input("ID del profesor asignado: ").strip())

        try:
            curso = crear_curso(session, nombre, profesor_id)
            print(f"✅ Curso creado: {curso.nombre}")
        except ValueError as e:
            print(f"❌ Error: {e}")

def mostrar_los_cursos_vista() -> None:
    print("=== Lista de Cursos ===")
    with db_session() as session:
        cursos = mostrar_los_cursos(session)
        for c in cursos:
            print(f"{c.id}: {c.nombre} (Profesor ID: {c.profesor_id})")

def mostrar_curso_por_id_vista() -> None:
    print("=== Buscar Curso por ID ===")
    cid = int(input("ID del curso: ").strip())
    with db_session() as session:
        curso = mostrar_curso_por_id(session, cid)
        if curso:
            print(f"{curso.id}: {curso.nombre} (Profesor ID: {curso.profesor_id})")
        else:
            print("❌ Curso no encontrado.")

def actualizar_curso_vista() -> None:
    print("=== Actualizar Curso ===")
    cid = int(input("ID del curso: ").strip())
    nuevo_nombre = input("Nuevo nombre del curso: ").strip()

    with db_session() as session:
        try:
            curso = actualizar_curso(session, cid, nuevo_nombre)
            print(f"✅ Curso actualizado: {curso.nombre}")
        except ValueError as e:
            print(f"❌ Error: {e}")

def eliminar_curso_vista() -> None:
    print("=== Eliminar Curso ===")
    cid = int(input("ID del curso a eliminar: ").strip())

    with db_session() as session:
        try:
            eliminar_curso(session, cid)
            print("✅ Curso eliminado.")
        except ValueError as e:
            print(f"❌ Error: {e}")

def inscribir_estudiante_vista() -> None:
    print("=== Inscribir Estudiante en Curso ===")

    with db_session() as session:
        estudiantes = mostrar_los_estudiantes(session)
        print("\nEstudiantes disponibles:")
        for e in estudiantes:
            print(f"{e.id}: {e.nombre}")

        eid = int(input("ID del estudiante: ").strip())

        cursos = mostrar_los_cursos(session)
        print("\nCursos disponibles:")
        for c in cursos:
            print(f"{c.id}: {c.nombre}")

        cid = int(input("ID del curso: ").strip())

        try:
            inscribir_estudiante_en_curso(session, eid, cid)
            print("✅ Estudiante inscrito con éxito.")
        except ValueError as e:
            print(f"❌ Error: {e}")

def ver_cursos_estudiante_vista() -> None:
    print("=== Ver cursos inscritos por estudiante ===")

    with db_session() as session:
        estudiantes = mostrar_los_estudiantes(session)
        for e in estudiantes:
            print(f"{e.id}: {e.nombre}")
        eid = int(input("ID del estudiante: ").strip())

        try:
            cursos = listar_cursos_de_estudiante(session, eid)
            print(f"\nCursos inscritos de {eid}:")
            for c in cursos:
                print(f"- {c.nombre}")
        except ValueError as e:
            print(f"❌ Error: {e}")