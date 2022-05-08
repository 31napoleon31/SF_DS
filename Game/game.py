import numpy as np

def optimal_predict(mini: int=1, maxi: int=101, number: int=None) -> int:
    '''Игра компьютер угадает число меньше чем за 20 попыток'''

    if number is None:
        number = np.random.randint(mini, maxi)

    count = 0

    while True:
        count+=1
        midi = (mini+maxi) // 2
    
        if midi > number:
          maxi = midi
    
        elif midi < number:
          mini = midi

        else:
            print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break 
    return count


def score_game(optimal_predict) -> int:
    """ За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        optimal_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    
    count_ls = []
    
    #np.random.seed(1)   
    ''' Если раскомментируем предыдущую строку, то можем зафиксировать сид для воспроизводимости.
        Это облегчит отлов ошибок и позволит сравнить работу программы
        даже при использовании разных рабочих мест'''
                            
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список онлайн переводчик чисел
    for i in random_array:
        count_ls.append(optimal_predict(number=i))

    score = round(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки в {len(count_ls)} проходах!")
    return score


    # RUN
if __name__ == "__main__":

    score_game(optimal_predict)
