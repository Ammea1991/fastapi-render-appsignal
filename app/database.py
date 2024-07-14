# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://meahome_postgres_user:SXkSicAdQfG40H06i5bkwVb3pHWg37kp@dpg-cq9vj1lds78s739k1u10-a/meahome_postgres"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()