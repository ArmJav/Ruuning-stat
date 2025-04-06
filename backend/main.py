from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi_socketio import SocketManager
from models import into_race,engine, get_race_history
import asyncio

from functions import get_probability_vector, generate_random_statistics, \
    get_first_or_second_or_third, simulate_race_with_physics, get_athlete_params, simulate_races

app = FastAPI(description='API по сбору статистик о забегах', version='0.1.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

socket_manager = SocketManager(app=app)


main_stat = generate_random_statistics(25)

# @app.get('/get_race_hist',
#          summary='История забегов',
#          tags=['Таблицы'])
# async def get_racea_history():
#     return get_race_history()

# @app.get("/start_race",
#          summary='Старт забега',
#          tags=['Визуализация забега'])
# async def start_race():
#     athlete_params = get_athlete_params()
#     places, progress = simulate_race_with_physics(athlete_params)

#     places = {v:k for k,v in places.items()}

#     out = []
#     for i in range(1,7):
#         out.append(int(places[i][-1:]))
  
#     into_race(engine=engine,races_data=out)

#     return progress,places


@app.get('/get_probability',
         summary='Получение всех вероятностей',
         tags=['Таблицы'])
async def get_probability():
    return get_probability_vector()


@app.get('/pair_stat',
         summary='Вычисление парной статистики для любой пары учеников',
         tags=['Таблицы'])
async def get_probability_pair():
    prob = get_probability_vector()
    new = {}

    for i in range(0,6):
        adsa = []
        for j in range(0,6):
            if i != j:
                adsa.append(prob['pl'+str(i+1)][0]*prob['pl' +str(j+1)][1])
            else:
                adsa.append(0)
        new['pl' + str(i+1)] = adsa

    return new        
    
@app.get('/first_sec_thrid/',
         summary='Для расчета 1-ого или 2-ого или 3-его места по номеру игрока',
         tags=['Таблицы'])
async def get_first_or_second_or_third():
    prob = get_probability_vector()

    rez = {}

    for i in range(0,6):
        player = i +1
        rez['pl' + str(i+1)] = prob["pl" + str(player)][0] + prob["pl" + str(player)][1] + prob["pl" + str(player)][2]


    return rez

@app.get('/fir_sec',
         summary='Для расчета 1-ого или 2-ого места по номеру игрока',
         tags=['Таблицы'])
async def get_first_or_second():
    prob = get_probability_vector()
    rez = {}
    for i in range(0,6):
        player = i +1
        rez['pl' + str(i+1)] = prob["pl" + str(player)][0] + prob["pl" + str(player)][1]

    return rez

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
