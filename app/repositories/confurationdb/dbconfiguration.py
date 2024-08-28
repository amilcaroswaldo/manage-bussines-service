from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./managedbbussines.db"

# Crear el motor de la base de datos
engine = create_async_engine(DATABASE_URL, echo=True)

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

async def get_db():
    """Genera una nueva sesión de base de datos."""
    async with SessionLocal() as db:
        yield db  # Esto es un generador asíncrono