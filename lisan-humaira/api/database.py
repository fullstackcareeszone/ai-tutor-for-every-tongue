from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
#D:\lisan-tutor\api\database.py
DB_USER = "root"
DB_PASSWORD = "11%4022%4033%4044%4055%4066%4077"
DB_HOST = "localhost"
DB_NAME = "lisan_db"  # ✅ choose your preferred name

# Step 1: Connect to MySQL without specifying a database
temp_engine = create_engine(f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306")

# Step 2: Create the database if it doesn't exist
with temp_engine.connect() as conn:
    conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"))
    conn.commit()

# Step 3: Now connect to the newly created database
DB_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}"
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
