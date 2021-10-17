from random import choice


def get_jokes(n, repeats=True):
    """Функция, возвращающая n шуток с повторами или без.

    Шутки сформированы из трех случайных слов,
    взятые из трёх заданных в функции списков
    (по одному из каждого).
    Если repeats=Fasle. Выполняется без повторения значений.
    Максимальное количество шуток n = 5.
    Иначе использованы все варианты
    """
    # print(help(get_jokes))

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    i = 0
    joke = []
    if not repeats:
        if n > min(len(nouns), len(adverbs), len(adjectives)):
            return 'Использованы все варианты'
        else:
            choice(nouns)
            choice(adverbs)
            choice(adjectives)
            while i < n:
                joke.append(f'{nouns[i]} {adverbs[i]} {adjectives[i]}')
                i += 1
    else:
        while i < n:
            joke.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
            i += 1
    return joke


print(get_jokes(5))  # True, возможны повторения
print(get_jokes(5, False))  # Без повторений
print(get_jokes(10))  # True, возможно неограниченное количество шутеек
print(get_jokes(6, False))  # Без повторений. Возможны 5 вариантов т.к. использованы все значения
