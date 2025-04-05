import random
import numpy as np
from collections import Counter

def generate_athlete_params():
    return {
        f'У{i}': {
            'reaction_time': round(random.uniform(0.1, 0.3), 2),
            'acceleration': round(random.uniform(4.5, 5.0), 2),
            'max_speed': round(random.uniform(9.0, 10.0), 2),
            'fatigue_factor': round(random.uniform(0.68, 1.0), 3)
        }
        for i in range(1, 7)
    }

def get_place_distribution(history):
    dist = {}
    for runner, results in history.items():
        total = len(results)
        if total == 0:
            dist[runner] = {place: 1/6 for place in range(1, 7)}
        else:
            count = Counter(results)
            dist[runner] = {place: count.get(place, 0) / total for place in range(1, 7)}
    return dist

def calculate_strength(distribution):
    weights = {1: 1.0, 2: 0.8, 3: 0.6, 4: 0.4, 5: 0.2, 6: 0.0}
    strengths = {}
    for runner, probs in distribution.items():
        strengths[runner] = sum(weights[place] * probs.get(place, 0) for place in range(1, 7))
    return strengths

def simulate_race_with_physics(athlete_params):
    times = {}
    progress_data = {}
    for athlete, p in athlete_params.items():
        t, dt, distance, speed = 0.0, 1.0, 0.0, 0.0
        positions = []
        acc = p['acceleration'] + random.uniform(-0.2, 0.2)
        max_speed = p['max_speed'] + random.uniform(-0.3, 0.3)
        fatigue = p['fatigue_factor'] + random.uniform(-0.002, 0.002)
        react = p['reaction_time'] + random.uniform(-0.05, 0.05)

        while distance < 100:
            if t >= react:
                if speed < max_speed:
                    speed += acc * dt
                    speed = min(speed, max_speed)
                else:
                    speed *= fatigue
                distance += speed * dt
            positions.append(round(min(distance, 100), 2))
            t += dt
        progress_data[athlete] = positions
        times[athlete] = t
    sorted_runners = sorted(times.items(), key=lambda x: x[1])
    places = {runner: place for place, (runner, _) in enumerate(sorted_runners, start=1)}
    return places, progress_data

def simulate_races(history, athlete_params, num_races=10):
    for race in range(num_races):
        print(f"Забег {race + 1}")
        dist = get_place_distribution(history)
        strengths = calculate_strength(dist)
        places, progress = simulate_race_with_physics(athlete_params)
        print("Результаты:", places)
        # print("Прогресс дистанции:")
        # for runner, data in progress.items():
        #     print(f"  {runner}: {data}")
        for runner, place in places.items():
            history[runner].append(place)

if __name__ == "__main__":
    history = {f'У{i}': [] for i in range(1, 7)}
    athlete_params = generate_athlete_params()
    print(athlete_params)
    simulate_races(history, athlete_params, num_races=10)
