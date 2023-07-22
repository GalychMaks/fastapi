from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import setting

SQLALCHEMY_DATABASE_URL = f'postgresql://{setting.DATABASE_USERNAME}:{setting.DATABASE_PASSWORD}@' \
                          f'{setting.DATABASE_HOSTNAME}:{setting.DATABASE_PORT}/{setting.DATABASE_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


"""
try:
    conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='qwerty0002234',
                            cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connection was successful")
except Exception as error:
    print("Connection to database failed")
    print(f"Error was {error}")
"""
