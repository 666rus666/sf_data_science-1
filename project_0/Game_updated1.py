import numpy as np

def random_predict(number:int=1) -> int:
    """Угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Кол-во попыток
    """
    count = 0

    while True:
        count += 10
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if predict_number < 50:
            count -= 1
            number == predict_number
            break # выход из цикла, если угадали
        elif predict_number > 50:
            count += 1
            number == predict_number
            break
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """1000 Попыток

    Args:
        random_predict (_type_): Функция нахождения

    Returns:
        int: Среднее кол-во попыток
    """ 
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(20)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict)