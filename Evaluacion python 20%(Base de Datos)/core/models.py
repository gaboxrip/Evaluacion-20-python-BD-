from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship

Base = declarative_base()

# Relación M:N entre Estudiante y Curso
estudiante_curso = Table(
    "estudiante_curso",
    Base.metadata,
    Column("estudiante_id", ForeignKey("estudiantes.id"), primary_key=True),
    Column("curso_id", ForeignKey("cursos.id"), primary_key=True)
)

class Profesor(Base):
    __tablename__ = "profesores"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    cursos: Mapped[list["Curso"]] = relationship("Curso", back_populates="profesor")

class Curso(Base):
    __tablename__ = "cursos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))
    
    profesor: Mapped["Profesor"] = relationship("Profesor", back_populates="cursos")
    estudiantes: Mapped[list["Estudiante"]] = relationship("Estudiante", secondary=estudiante_curso, back_populates="cursos")

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(nullable=False)
    cursos: Mapped[list["Curso"]] = relationship("Curso", secondary=estudiante_curso, back_populates="estudiantes")

