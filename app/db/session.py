# engine+SessionLocal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:1415@localhost:5432/users"

engine = create_engine(DATABASE_URL,pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine,autoflush = False,autocommit = False)