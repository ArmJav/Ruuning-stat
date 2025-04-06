from random import shuffle


# Генерируем n случайных забегов
def generate_random_statistics(n: int) -> list[list]:
    history = []
    places = [1, 2, 3, 4, 5, 6]
    for i in range(n):
        shuffle(places)
        history.append(places[:])
    return history


# Функция для расчета вероятности каждого места для каждого участника
def get_probability_vector(history: list[list]) -> dict:
    n = len(history)
    probs = {"pl1": [0, 0, 0, 0, 0, 0], "pl2": [0, 0, 0, 0, 0, 0], "pl3": [0, 0, 0, 0, 0, 0], "pl4": [0, 0, 0, 0, 0, 0],
             "pl5": [0, 0, 0, 0, 0, 0], "pl6": [0, 0, 0, 0, 0, 0]}
    for i in history:
        for j in range(6):
            probs["pl" + str(i[j])][j] += 1
    for i in range(6):
        probs["pl" + str(i + 1)] = [round(j/n,2) for j in probs["pl" + str(i + 1)]]
    return probs


# Функция для расчета 1-ого или 2-ого места по номеру игрока
def get_first_or_second(player: int, probs: dict) -> float:
    return probs["pl" + str(player)][0] + probs["pl" + str(player)][1]


# Функция для расчета 1-ого или 2-ого или 3-его места по номеру игрока
def get_first_or_second_or_third(player: int, probs: dict) -> float:
    return probs["pl" + str(player)][0] + probs["pl" + str(player)][1] + probs["pl" + str(player)][2]


# Функция для вычисления парной статистики для любой пары учеников
def get_pair_statistics(player1: int, player2: int, probs: dict) -> float:
    return round(probs["pl" + str(player1)][0] * probs["pl" + str(player2)][1]
            + probs["pl" + str(player1)][1] * probs["pl" + str(player2)][0],2)

# Мат ожидание места в следующем забеге (сила)
def get_strength(probs: dict) -> dict:
    res = dict()
    for i in range(1, 7):
        summ = 0
        for j in range(1, 7):
            summ += probs['pl' + str(i)][j - 1] * (7 - j)
        res['pl' + str(i)] = summ
    return res

