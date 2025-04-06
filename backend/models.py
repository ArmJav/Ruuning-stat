import psycopg2
from fastapi import HTTPException
from sqlalchemy import create_engine, Column, Integer, DateTime, ARRAY, Float, inspect,String
from sqlalchemy.orm import sessionmaker,declarative_base
from datetime import datetime,timedelta
from time import sleep
import random
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
    
    id = Column(Integer, primary_key=True)  
    name = Column(String, nullable=False)
    reaction_time = Column(Float, nullable=False)
    acceleration = Column(Float, nullable=False)
    max_speed = Column(Float, nullable=False)
    min_speed = Column(Float, nullable=False)
    fatigue_factor = Column(Float, nullable=False)
    second_acceleration = Column(Float, nullable=False)

class RaceResult(Base):
    __tablename__ = 'race_results'
    
    race_id = Column(Integer, primary_key=True)
    place_ids = Column(ARRAY(Integer))  # Массив с данными о местах
    created_at_time = Column(DateTime, default=datetime.utcnow)

def get_race_history():
    Session = sessionmaker(bind=engine)
    session = Session()

    # Получение всех значений из столбца race_id
    race_ids = session.query(RaceResult.place_ids).all()

    race_ids_list = [race_id[0] for race_id in race_ids]

    return race_ids_list

def create_database(db_name, user, password, host='localhost'):
    cursor = None
    conn = None
    try:
        conn = psycopg2.connect(dbname='postgres', user=user, password=password, host=host)
        conn.autocommit = True 
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

def into_race(engine,races_data):
    Session = sessionmaker(bind=engine)
    session = Session()

    new_race = RaceResult(
        place_ids=races_data,
        created_at_time = datetime.now()
    )
    session.add(new_race)

    session.commit()
    print("Таблица Race заполнена данными.")

    
    min_race = session.query(RaceResult).order_by(RaceResult.race_id).first()  # Получаем запись с наименьшим race_id
    if min_race:
        session.delete(min_race)  # Удаляем запись
        session.commit()  # Сохраняем изменения
        print(f"Удален элемент с race_id: {min_race.race_id}")
    else:
        print("Нет записей для удаления.")

def get_fiz(engine):
    Session = sessionmaker(bind=engine)
    session = Session()

    # Получение всех данных из таблицы Performance, кроме id
    performances = session.query(Athlete).all()

    # Преобразование данных в список словарей
    performances_data = {
        performance.name: {
            "reaction_time": performance.reaction_time,
            "acceleration": performance.acceleration,
            "max_speed": performance.max_speed,
            "min_speed": performance.min_speed,
            "fatigue_factor": performance.fatigue_factor,
            "second_acceleration": performance.second_acceleration,
        }
        for performance in performances
    }
    if performances_data:
        return performances_data
    else:
        raise HTTPException(status_code=404,detail='Not Found')

# Функция для создания таблиц
def create_tables(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    print("Таблицы успешно созданы!")

def create_random_races():
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in range(25):  
        place_ids = random.sample(range(1, 7), 6)  
        created_at_time = datetime.utcnow() - timedelta(days=random.randint(0, 30)) 
        new_race = RaceResult(
            place_ids=place_ids,
            created_at_time=created_at_time
        )
        session.add(new_race)

    session.commit()
    print("Таблица races заполнена произвольными данными.")



# Словарь с данными о спортсменах
def athlet_created():
    Session = sessionmaker(bind=engine)
    session = Session()
    athletes_data = {
        f'pl1': {        'reaction_time': 0.2,
            'acceleration': 1.5,        'max_speed': 9.7,
            'min_speed': 6.7,        'fatigue_factor': 0.90,
            'second_acceleration': 1.0    },
        f'pl2': {        'reaction_time': 0.2,
            'acceleration': 1.4,        'max_speed': 9.8,
            'min_speed': 6.9,        'fatigue_factor': 0.93,
            'second_acceleration': 0.8    },
        f'pl3': {        'reaction_time': 0.3,
            'acceleration': 1.4,
            'max_speed': 9.3,        'min_speed': 6.6,
            'fatigue_factor': 0.9,        'second_acceleration': 0.9
        },    f'pl4': {
            'reaction_time': 0.3,        'acceleration': 1.2,
            'max_speed': 9.0,        'min_speed': 6.8,
            'fatigue_factor': 0.87,        'second_acceleration': 0.7
        },    f'pl5': {
            'reaction_time': 0.3,        'acceleration': 1.0,
            'max_speed': 8.7,        'min_speed': 6.7,
            'fatigue_factor': 0.85,        'second_acceleration': 0.6
        },
        f'pl6': {        'reaction_time': 0.3,
            'acceleration': 1.1,        'max_speed': 8.8,
            'min_speed': 6.9,        'fatigue_factor': 0.83,
            'second_acceleration': 0.6    },
    }

     # Заполнение таблицы данными о спортсменах
    for name, data in athletes_data.items():
        new_performance = Athlete(
            name=name,
            reaction_time=data["reaction_time"],
            acceleration=data["acceleration"],
            max_speed=data["max_speed"],
            min_speed=data["min_speed"],
            fatigue_factor=data["fatigue_factor"],
            second_acceleration=data["second_acceleration"]
        )
        session.add(new_performance)

    session.commit()

# # Основной код
# if __name__ == "__main__": 
#     env_path = Path('.') / '.env'
#     load_dotenv(dotenv_path=env_path)

#     if (DATABASE_URL := os.getenv("DATABASE_URL")) is None:
#         raise ValueError("DATABASE_URL не установлен")
#     create_engine(DATABASE_URL)
#     inspector = inspect(engine)
#     if 'athletes' not in inspector.get_table_names():
#         create_tables(DATABASE_URL)
#         create_random_races()
#         athlet_created()
#     else:
#         print('Таблицы уже созданы')


