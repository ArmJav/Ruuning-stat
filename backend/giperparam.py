# import random
# import matplotlib.pyplot as plt

# from main import generate_random_statistics, get_probability_vector, get_strength


# def generate_athlete_params():
#     return {
#         f'pl{i}': {
#             'reaction_time': round(random.uniform(0.1, 0.3), 3),
#             'acceleration': round(random.uniform(1.0, 2.0), 3),
#             'max_speed': round(random.uniform(9.0, 10.0), 3),
#             'min_speed': round(random.uniform(6.0, 7.0), 3),
#             'fatigue_factor': round(random.uniform(0.85, 0.95), 3),
#             'second_acceleration': round(random.uniform(0.5, 1.0), 3)
#         }
#         for i in range(1, 7)
#     }

# def simulate_race_with_physics(athlete_params):
#     times = {}
#     progress_data = {}
#     progress_speed = {}
#     for athlete, p in athlete_params.items():
#         t, dt, distance, speed = 0.0, 1.0, 0.0, 0.0
#         is_max_speed_reached = 0
#         is_min_speed_reached = 0
#         positions = []
#         speeds = []
#         acc = p['acceleration'] + random.uniform(-0.2, 0.2)  # Прибавляем шум к ускорению
#         max_speed = p['max_speed'] + random.uniform(-0.5, 0.5)  # Прибавляем шум к максимальной скорости
#         fatigue = p['fatigue_factor'] + random.uniform(-0.01, 0.01)  # Прибавляем шум к коэффициенту потери скорости
#         react = p['reaction_time'] + random.uniform(-0.05, 0.05)  # Прибавляем шум к времени реакции
#         second_acc = p['second_acceleration'] + random.uniform(-0.3, 0.3)
#         min_speed = p['min_speed'] + random.uniform(-0.4, 0.4)

#         while distance < 100:
#             if t >= react:
#                 if speed < max_speed and not is_max_speed_reached:
#                     speed += (acc + random.uniform(-0.2, 0.05 * strength[athlete])) * dt
#                     speed = min(speed, max_speed)
#                     if speed == max_speed:
#                         is_max_speed_reached = 1
#                 elif is_max_speed_reached and not is_min_speed_reached:
#                     speed *= (fatigue + random.uniform(-0.01, 0.005 * strength[athlete]))
#                     speed = max(speed, min_speed)
#                     if speed == min_speed:
#                         is_min_speed_reached = 1
#                 elif is_min_speed_reached:
#                     speed += (second_acc + random.uniform(-0.2, 0.05 * strength[athlete])) * dt
#                     speed = min(speed, max_speed)
#                 distance += speed * dt
#             positions.append(round(min(distance, 100), 2))
#             speeds.append(speed)
#             t += dt
#         progress_data[athlete] = positions
#         progress_speed[athlete] = speeds
#         times[athlete] = t
#     sorted_runners = sorted(times.items(), key=lambda x: x[1])
#     places = {runner: place for place, (runner, _) in enumerate(sorted_runners, start=1)}
#     return places, progress_data

# def simulate_races(history, athlete_params, num_races=10):
#     for race in range(num_races):
#         places, progress = simulate_race_with_physics(athlete_params)
#         print("Результаты:", places)
#         for runner, place in places.items():
#             history[runner].append(place)

# if __name__ == "__main__":
#     history = {f'pl{i}': [] for i in range(1, 7)}
#     N = 15
#     history1 = generate_random_statistics(N)
#     prob = get_probability_vector(history1)
#     strength = get_strength(prob)
#     print(strength)

#     athlete_params = generate_athlete_params()
#     print(athlete_params)
#     simulate_races(history, athlete_params, num_races=10)
