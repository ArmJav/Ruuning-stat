from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_socketio import SocketManager
import asyncio
import random
from main import get_strength,get_probability_vector,generate_random_statistics,get_pair_statistics,get_first_or_second_or_third

app = FastAPI(description='API по сбору статистик о забегах',version='0.1.0')

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Инициализация SocketManager
socket_manager = SocketManager(app=app)

# Начальные позиции и скорости спортсменов
athletes = {}
for i in range(6):
    athlete_name = f'Athlete_{i+1}'
    athletes[athlete_name] = {
        'name':f'y{i+1}',
        'position': 0,
        'acceleration': round(random.uniform(1.0, 1.5)), 
        'max_speed': round(random.uniform(9.5, 10), 3),
        'min_speed':round(random.uniform(6.5, 7.0)),
        'fatigue': round(random.uniform(0.85, 0.95)), 
        'reaction_time': round(random.uniform(0.1, 0.3), 3),
        'second_acceleration': round(random.uniform(0.5, 1.0), 3)
    }

async def update_athlete_positions() -> str:
    finished_guys = []
    
    t, dt, distance, speed = 0.0, 0.1, 0.0, 0.0
    main_dist = 100
    is_max_speed_reached = 0
    is_min_speed_reached = 0
    while True:        
        await asyncio.sleep(0.1) 
        
        all_finished = True  
        for athlete in athletes.values():
            
            acc = athlete['acceleration'] + random.uniform(-0.5, 0.5)  # Прибавляем шум к ускорению
            max_speed = athlete['max_speed'] + random.uniform(-1, 1)  # Прибавляем шум к максимальной скорости
            fatigue = athlete['fatigue'] + random.uniform(-0.05, 0.05)  # Прибавляем шум к коэффициенту потери скорости
            react = athlete['reaction_time'] + random.uniform(-0.01, 0.01)  # Прибавляем шум к времени реакции
            second_acc = athlete['second_acceleration'] + random.uniform(-0.5, 0.5)
            min_speed = athlete['min_speed'] + random.uniform(-1, 1)

            if athlete["position"] < main_dist:  
                if t <= react:
                    if athlete["position"] < main_dist:  
                        if speed < max_speed and not is_max_speed_reached:
                            speed += (acc) + random.uniform(-0.2, 0.2 * get_strength()) 
                            speed = min(speed, max_speed)
                            if speed == max_speed:
                                is_max_speed_reached = 1
                        elif is_max_speed_reached and not is_min_speed_reached:
                            speed *= (fatigue + random.uniform(-0.01, 0.01)) 
                            speed = max(speed, min_speed)
                            if speed == min_speed:
                                is_min_speed_reached = 1
                        elif is_min_speed_reached:
                            speed += (second_acc + random.uniform(-0.2, 0.2))
                            speed = min(speed, max_speed)
                        
                    # print(f'{athlete["name"]}: {speed}, м')
                    
                    athlete["position"] += speed
                
                    if athlete["position"] > main_dist:               
                        athlete["position"] = main_dist
                        finished_guys.append(athlete['name'])  
                        
                await socket_manager.emit('update_position', f'{athlete["name"]}: {round(athlete["position"],2)}, м')
                # print(f'{athlete["name"]}: {round(athlete["position"],2)}, м')

                all_finished = False  

       
        
        if all_finished:
            await socket_manager.emit('race_finished', {'message': 'Забег окончен!', 'results': athletes})
            all_finished = False
            
            for athlete in athletes.values():
                athlete['position'] = 0
            break

    return finished_guys

main_stat = generate_random_statistics(15)

@app.get("/start_race",
         summary='Старт забега',
         tags=['Визуализация забега'])
async def start_race(background_tasks: BackgroundTasks):
    background_tasks.add_task(update_athlete_positions)
    return {"message": "Race started!"}

@app.get('/get_probability',
         summary='Получение всех вероятностей',
         tags=['Таблицы'])
async def get_probability():
    return get_probability_vector(main_stat)

@app.get('/pair_stat',
         summary='Вычисление парной статистики для любой пары учеников',
         tags=['Таблицы'])
async def get_probability(player1: int, player2: int):
    return get_pair_statistics(player1=player1,player2=player2,probs=get_probability_vector(main_stat))

@app.get('/first_or_second_or_third',
         summary='Для расчета 1-ого или 2-ого или 3-его места по номеру игрока',
         tags=['Таблицы'])
async def get_first_or_second_or_thira(player:int):
    if player < 0 or player > 6:
        raise HTTPException(404,detail='Такого юзера нет')
    return round(get_first_or_second_or_third(player=player,probs= get_probability_vector(main_stat)),2)

@socket_manager.on('connect')
async def handle_connect(sid, environ):
    print(f"Client connected: {sid}")

@socket_manager.on('disconnect')
async def handle_disconnect(sid):
    print(f"Client disconnected: {sid}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)