# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, inspect,Float, CheckConstraint,TIMESTAMP
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, relationship
# import psycopg2

# # Создаем базовый класс для моделей
# Base = declarative_base()

# class Athlete(Base):
#     __tablename__ = 'athletes'
    
#     athlete_id = Column(Integer, primary_key=True)
#     name = Column(String(50), nullable=False)
#     color = Column(String(20), nullable=False)
#     reaction_time = Column(Float, CheckConstraint('reaction_time BETWEEN 0.1 AND 0.3'))
#     acceleration = Column(Float, CheckConstraint('acceleration > 0'))
#     max_speed = Column(Float, CheckConstraint('max_speed > 0'))
#     fatigue = Column(Float, CheckConstraint('fatigue BETWEEN 0 AND 0.1'))

#     # Связь с результатами гонок
#     race_results = relationship("RaceResult", back_populates="athlete")

# class RaceResult(Base):
#     __tablename__ = 'race_results'
    
#     result_id = Column(Integer, primary_key=True)
#     athlete_id = Column(Integer, ForeignKey('athletes.athlete_id', ondelete='CASCADE'))
#     position = Column(Integer, CheckConstraint('position BETWEEN 1 AND 6'))
#     created_at = Column(TIMESTAMP, nullable=True)

#     # Уникальные ограничения
#     # Связь с атлетами
#     athlete = relationship("Athlete", back_populates="race_results")



# # Функция для создания таблиц
# def create_tables(db_url):
#     try:
#         # Создаем движок для подключения к новой базе данных
#         engine = create_engine(db_url)
        
#         # Проверяем существование таблиц и создаем их
#         if not inspect(engine).has_table("your_model"):  # Замените на имя вашей модели
#             Base.metadata.create_all(engine)
#             print("Таблицы успешно созданы!")
#         else:
#             print("Таблицы уже существуют.")
#     except Exception as e:
#         print(f"Ошибка при создании таблиц: {e}")

import psycopg2
from sqlalchemy import create_engine, Column, Integer, String, Text, inspect,Float,CheckConstraint,TIMESTAMP,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.orm import declarative_base
from time import sleep
from dotenv import load_dotenv
from pathlib import Path
import os



# Создаем базовый класс для моделей
Base = declarative_base()
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

if (DATABASE_URL := os.getenv("DATABASE_URL")) is None:
    raise ValueError("DATABASE_URL не установлен")

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

class Athlete(Base):
    __tablename__ = 'athletes'
    
    athlete_id = Column(Integer, primary_key=True)
    reaction_time = Column(Float)#, CheckConstraint('reaction_time BETWEEN 0.1 AND 0.3'))
    acceleration = Column(Float)#, CheckConstraint('acceleration > 0'))
    max_speed = Column(Float)#, CheckConstraint('max_speed > 0'))
    min_speed = Column(Float)#, CheckConstraint('min_speed > 0'))
    fatigue_factor = Column(Float)
    second_acceleration = Column(Float)#, CheckConstraint('second_acceleration > 0'))
    # Связь с результатами гонок
    # race_results = relationship("RaceResult", back_populates="athlete")

class RaceResult(Base):
    __tablename__ = 'race_results'
    
    result_id = Column(Integer, primary_key=True)
    athlete_id = Column(Integer, ForeignKey('athletes.athlete_id', ondelete='CASCADE'))
    position = Column(Integer, CheckConstraint('position BETWEEN 1 AND 6'))
    created_at = Column(TIMESTAMP, nullable=True)

    # Уникальные ограничения
    # Связь с атлетами
    # athlete = relationship("Athlete", back_populates="race_results")


def create_database(db_name, user, password, host='localhost'):
    cursor = None
    conn = None
    try:
        # Подключаемся к PostgreSQL без указания базы данных
        conn = psycopg2.connect(dbname='postgres', user=user, password=password, host=host)
        conn.autocommit = True  # Включаем автокоммит для создания базы данных
        cursor = conn.cursor()
        
        # Создаем новую базу данных
        cursor.execute(f"CREATE DATABASE {db_name};")
        print(f"База данных '{db_name}' успешно создана.")
    except psycopg2.errors.DuplicateDatabase:
        print(f"База данных '{db_name}' уже существует.")
    except Exception as e:
        print(f"Ошибка при создании базы данных: {e}")
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

# Функция для создания таблиц
def create_tables(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    print("Таблицы успешно созданы!")


# def fill_athletes():
    
#     k = Athlete(reaction_time = 0.2,acceleration= 1.5,max_speed = 9.7, min_speed = 6.7,fatigue_factor= 0.90,second_acceleration= 1.0),



#     session.add(k)
#     session.commit()
#     print("Таблица 'athletes' успешно заполнена данными.")

# # Заполняем таблицу
# fill_athletes()

# # Закрываем сессию
# session.close()


# Основной код
if __name__ == "__main__": 
    create_database(DB_NAME, USER, PASSWORD)
    sleep(1)
    inspector = inspect(engine)
    if 'athletes' not in inspector.get_table_names():
        create_tables(DATABASE_URL)
    else:
        print('Таблицы уже созданы')


