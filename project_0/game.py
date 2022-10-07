import numpy as np

def random_predict(number:int=1) -> int:
    """Quantity of trying to find number

    Args:
        number (int, optional): Finding number. Defaults to 1.

    Returns:
        int: Qantity of tries
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """1000 tries

    Args:
        random_predict (_type_): Function found

    Returns:
        int: Average tries
    """ 
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

score_game(random_predict)

git config --global user.email ema