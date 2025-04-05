import numpy as np
from collections import Counter

# История забегов
# history = {
#     'У1': [1, 2, 1, 3, 2, 1],
#     'У2': [3, 4, 5, 2, 6, 4],
#     'У3': [6, 5, 6, 4, 5, 6],
#     'У4': [2, 1, 2, 1, 3, 2],
#     'У5': [4, 2, 4, 5, 2, 3],
#     'У6': [5, 6, 3, 6, 1, 5],
# }

history = {
    'У1': [1],
    'У2': [3],
    'У3': [6],
    'У4': [2],
    'У5': [4],
    'У6': [5],
}

# Функция для расчета вероятности каждого места для каждого участника
def get_place_distribution(history):
    dist = {}
    for runner, results in history.items():
        count = Counter(results)
        total = len(results)
        dist[runner] = {place: count.get(place, 0) / total for place in range(1, 7)}
    return dist

# Функция для расчета силы участника
def calculate_strength(distribution):
    weights = {1: 1.0, 2: 0.8, 3: 0.6, 4: 0.4, 5: 0.2, 6: 0.0}
    strengths = {}
    for runner, probs in distribution.items():
        strengths[runner] = sum(weights[place] * probs.get(place, 0) for place in range(1, 7))
    return strengths

# Генерация забега с учетом силы участников
def generate_weighted_race(strengths):
    runners = list(strengths.keys())
    scores = np.array([strengths[r] for r in runners])
    
    # Добавляем случайность (шум) для более разнообразных результатов
    noisy_scores = scores + np.random.normal(0, 0.25, size=scores.shape)

    # Сортируем участников по величине noisy_scores (чем выше сила, тем выше место)
    sorted_runners = [r for _, r in sorted(zip(-noisy_scores, runners))]

    return {runner: place for place, runner in enumerate(sorted_runners, start=1)}

# Симуляция 10 забегов
def simulate_races(num_races=10):
    global history

    for race in range(num_races):
        # print(f"Забег {race + 1}")
        
        # Получаем распределение мест для каждого участника
        dist = get_place_distribution(history)
        
        # Рассчитываем силу участников
        strengths = calculate_strength(dist)
        
        # Генерируем новый забег
        result = generate_weighted_race(strengths)
        print(result)
        
        # Обновляем историю результатов
        for runner, place in result.items():
            history[runner].append(place)
        
        print(f"Обновленная история:\n{history}\n")

# Симуляция 10 забегов
simulate_races(10)
