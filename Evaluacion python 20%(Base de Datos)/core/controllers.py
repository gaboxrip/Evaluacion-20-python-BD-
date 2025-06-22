from sqlalchemy.orm import Session
from core.models import Estudiante, Profesor, Curso

def crear_estudiante(session: Session, nombre: str) -> Estudiante:
    """Crea un nuevo estudiante."""
    existing = session.query(Estudiante).filter_by(nombre=nombre).first()
    if existing:
        raise ValueError("El estudiante ya existe.")

    new_estudiante = Estudiante(nombre=nombre)
    session.add(new_estudiante)
    session.commit()
    session.refresh(new_estudiante)
    return new_estudiante

def mostrar_los_estudiantes(session: Session) -> list[Estudiante]:
    return session.query(Estudiante).all()

def mostrar_estudiante_por_id(session: Session, estudiante_id: int) -> Estudiante:
    estudiante = session.get(Estudiante, estudiante_id)
    if estudiante is None:
        raise ValueError("No existe ningún estudiante con ese ID.")
    return estudiante

def actualizar_estudiante(session: Session, estudiante_id: int, nuevo_nombre: str) -> Estudiante:
    estudiante = mostrar_estudiante_por_id(session, estudiante_id)
    if not estudiante:
        raise ValueError("No existe ningún estudiante con ese ID.")

    estudiante.nombre = nuevo_nombre
    session.commit()
    session.refresh(estudiante)
    return estudiante

def eliminar_estudiante(session: Session, estudiante_id: int) -> None:
    estudiante = mostrar_estudiante_por_id(session, estudiante_id)
    if not estudiante:
        raise ValueError("No existe ningún estudiante con ese ID.")

    session.delete(estudiante)
    session.commit()

def crear_profesor(session: Session, nombre: str) -> Profesor:
    """Crea un nuevo profesor en la base de datos."""

    existing = session.query(Profesor).filter_by(nombre=nombre).first()
    if existing:
        raise ValueError("El profesor ya existe.")

    new_profesor = Profesor(nombre=nombre)
    session.add(new_profesor)
    session.commit()
    session.refresh(new_profesor)
    return new_profesor

def mostrar_los_profesores(session: Session) -> list[Profesor]:
    """Devuelve todos los profesores de la base de datos."""
    return session.query(Profesor).all()

def mostrar_profesor_por_id(session: Session, profesor_id: int) -> Profesor:
    """Devuelve un profesor por su ID."""
    profesor = session.get(Profesor, profesor_id)
    if profesor is None:
        raise ValueError("No existe ningún profesor con ese ID.")
    return profesor

def actualizar_profesor(session: Session, profesor_id: int, nuevo_nombre: str) -> Profesor:
    profesor = mostrar_profesor_por_id(session, profesor_id)
    if not profesor:
        raise ValueError("No existe ningún profesor con ese ID.")

    profesor.nombre = nuevo_nombre
    session.commit()
    session.refresh(profesor)
    return profesor

def eliminar_profesor(session: Session, profesor_id: int) -> None:
    profesor = mostrar_profesor_por_id(session, profesor_id)
    if not profesor:
        raise ValueError("No existe ningún profesor con ese ID.")

    session.delete(profesor)
    session.commit()

def crear_curso(session: Session, nombre: str, profesor_id: int) -> Curso:
    """Crea un nuevo curso vinculado a un profesor."""
    existing = session.query(Curso).filter_by(nombre=nombre).first()
    if existing:
        raise ValueError("El curso ya existe.")

    profesor = session.get(Profesor, profesor_id)
    if not profesor:
        raise ValueError("El profesor no existe.")

    new_curso = Curso(nombre=nombre, profesor_id=profesor_id)
    session.add(new_curso)
    session.commit()
    session.refresh(new_curso)
    return new_curso

def mostrar_los_cursos(session: Session) -> list[Curso]:
    return session.query(Curso).all()

def mostrar_curso_por_id(session: Session, curso_id: int) -> Curso:
    curso = session.get(Curso, curso_id)
    if curso is None:
        raise ValueError("No existe ningún curso con ese ID.")
    return curso

def actualizar_curso(session: Session, curso_id: int, nuevo_nombre: str) -> Curso:
    curso = mostrar_curso_por_id(session, curso_id)
    if not curso:
        raise ValueError("No existe ningún curso con ese ID.")

    curso.nombre = nuevo_nombre
    session.commit()
    session.refresh(curso)
    return curso

def eliminar_curso(session: Session, curso_id: int) -> None:
    curso = mostrar_curso_por_id(session, curso_id)
    if not curso:
        raise ValueError("No existe ningún curso con ese ID.")

    session.delete(curso)
    session.commit()

def inscribir_estudiante_en_curso(session: Session, estudiante_id: int, curso_id: int) -> None:
    """Asocia un estudiante a un curso (relación M:N)."""
    estudiante = session.get(Estudiante, estudiante_id)
    curso = session.get(Curso, curso_id)

    if not estudiante:
        raise ValueError("Estudiante no encontrado.")
    if not curso:
        raise ValueError("Curso no encontrado.")
    if curso in estudiante.cursos:
        raise ValueError("El estudiante ya está inscrito en ese curso.")

    estudiante.cursos.append(curso)
    session.commit()

def listar_cursos_de_estudiante(session: Session, estudiante_id: int) -> list[Curso]:
    """Devuelve todos los cursos a los que está inscrito un estudiante."""
    estudiante = session.get(Estudiante, estudiante_id)
    if not estudiante:
        raise ValueError("Estudiante no encontrado.")

    return estudiante.cursos