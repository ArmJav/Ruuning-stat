from random import shuffle
import random
from models import engine,get_fiz


# Генерируем n случайных забегов
def generate_random_statistics(n: int) -> list[list]:
    history = []
    places = [1, 2, 3, 4, 5, 6]
    for i in range(n):
        shuffle(places)
        history.append(places[:])
    return history


# Функция для расчета вероятности каждого места для каждого участника
def get_probability_vector() -> dict:
    history = generate_random_statistics()
    n = len(history)
    probs = {"pl1": [0, 0, 0, 0, 0, 0], "pl2": [0, 0, 0, 0, 0, 0], "pl3": [0, 0, 0, 0, 0, 0], "pl4": [0, 0, 0, 0, 0, 0],
             "pl5": [0, 0, 0, 0, 0, 0], "pl6": [0, 0, 0, 0, 0, 0]}
    for i in history:
        for j in range(6):
            probs["pl" + str(i[j])][j] += 1
    for i in range(6):
        probs["pl" + str(i + 1)] = [(j + 1)/(n+6) for j in probs["pl" + str(i + 1)]]
    return probs


# Функция для расчета 1-ого или 2-ого места по номеру игрока
def get_first_or_second(player: int, probs: dict) -> float:
    return probs["pl" + str(player)][0] + probs["pl" + str(player)][1]


# Функция для расчета 1-ого или 2-ого или 3-его места по номеру игрока
def get_first_or_second_or_third(player: int, probs: dict) -> float:
    return probs["pl" + str(player)][0] + probs["pl" + str(player)][1] + probs["pl" + str(player)][2]

# Мат ожидание места в следующем забеге (сила)
def get_strength(probs: dict) -> dict:
    res = dict()
    for i in range(1, 7):
        summ = 0
        for j in range(1, 7):
            summ += probs['pl' + str(i)][j - 1] * (7 - j)
        res['pl' + str(i)] = summ
    return res

# Генерируем случайные характеристики для участников
def get_athlete_params():
    return get_fiz(engine=engine)


# def calculate_strength(distribution):
#     weights = {1: 1.0, 2: 0.8, 3: 0.6, 4: 0.4, 5: 0.2, 6: 0.0}
#     strengths = {}
#     for runner, probs in distribution.items():
#         strengths[runner] = sum(weights[place] * probs.get(place, 0) for place in range(1, 7))
#     return strengths


def simulate_race_with_physics(athlete_params):
    strength = get_strength(get_probability_vector())
    times = {}
    progress_data = {}
    progress_speed = {}
    for athlete, p in athlete_params.items():
        t, dt, distance, speed = 0.0, 1.0, 0.0, 0.0
        is_max_speed_reached = 0

        is_min_speed_reached = 0
        positions = []
        speeds = []
        acc = p['acceleration'] + random.uniform(-0.2, 0.2)  # Прибавляем шум к ускорению
        max_speed = p['max_speed'] + random.uniform(-0.5, 0.5)  # Прибавляем шум к максимальной скорости
        fatigue = p['fatigue_factor'] + random.uniform(-0.01, 0.01)  # Прибавляем шум к коэффициенту потери скорости
        react = p['reaction_time'] + random.uniform(-0.05, 0.05)  # Прибавляем шум к времени реакции
        second_acc = p['second_acceleration'] + random.uniform(-0.3, 0.3)
        min_speed = p['min_speed'] + random.uniform(-0.4, 0.4)

        while distance < 100:
            if t >= react:
                if speed < max_speed and not is_max_speed_reached:
                    speed += (acc + random.uniform(-0.2, 0.05 * strength[athlete])) * dt
                    speed = min(speed, max_speed)
                    if speed == max_speed:
                        is_max_speed_reached = 1
                elif is_max_speed_reached and not is_min_speed_reached:
                    speed *= (fatigue + random.uniform(-0.01, 0.005 * strength[athlete]))
                    speed = max(speed, min_speed)
                    if speed == min_speed:
                        is_min_speed_reached = 1
                elif is_min_speed_reached:
                    speed += (second_acc + random.uniform(-0.2, 0.05 * strength[athlete])) * dt
                    speed = min(speed, max_speed)
                distance += speed * dt
            positions.append(round(min(distance, 100), 2))
            speeds.append(speed)
            t += dt

        progress_data[athlete] = positions
        progress_speed[athlete] = speeds
        times[athlete] = t

    # create_plot(progress_speed)
    sorted_runners = sorted(times.items(), key=lambda x: x[1])
    places = {runner: place for place, (runner, _) in enumerate(sorted_runners, start=1)}
    return places, progress_data


def simulate_races(history, athlete_params, num_races=10):
    for race in range(num_races):
        # print(f"Забег {race + 1}")
        places, progress = simulate_race_with_physics(athlete_params)
        # create_plot(progress)
        # print("Прогресс дистанции:")
        # for runner, data in progress.items():
        #     print(f"  {runner}: {data}")
        # print("Результаты:", places)
        print(progress)
        for runner, place in places.items():
            history[runner].append(place)
        return progress


if __name__ == "__main__":
    history = {f'pl{i}': [] for i in range(1, 7)}
    N = 15
    history1 = generate_random_statistics(N)
    prob = get_probability_vector(history1)
    strength = get_strength(prob)
    print(strength)

    athlete_params = get_athlete_params()
    print(athlete_params)
    simulate_races(history, athlete_params, num_races=10)



