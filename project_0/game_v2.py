import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    predict_number = np.random.randint(1, 101) # Случайное число сгенерированное программой
    count = 0
    min = 1 # Минимальное значение заданного числа
    max = 100 # Максимальное значение заданного числа
    while True:
        count += 1
        if predict_number > number:
            max = predict_number - 1
            predict_number = (max + min) // 2
        elif predict_number < number:
            min = predict_number + 1
            predict_number = (max + min) // 2
        else:
            #print(f'Заданное число найдено за {count} попыток. Это число равно {number}')
            break # Задача решена
    return(count)
# print(f'Количество попыток: {random_predict(number)}')
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воcпроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)