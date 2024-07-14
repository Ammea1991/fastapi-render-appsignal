from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
SQLALCHEMY_DATABASE_URL = "postgresql://meahome_postgres_user:SXkSicAdQfG40H06i5bkwVb3pHWg37kp@dpg-cq9vj1lds78s739k1u10-a.oregon-postgres.render.com/meahome_postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
