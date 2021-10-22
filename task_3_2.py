def num_translate_adv(key):
    storage = {
        'one': 'один', 'One': 'Один',
        'two': 'два', 'Two': 'Два',
        'three': 'три', 'Three': 'Три',
        'four': 'четыре', 'Four': 'Четыре',
        'five': 'пять', 'Five': 'Пять',
        'six': 'шесть', 'Six': 'Шесть',
        'seven': 'семь', 'Seven': 'Семь',
        'eight': 'восемь', 'Eight': 'Восемь',
        'nine': 'девять', 'Nine': 'Девять',
        'ten': 'десять', 'Ten': 'Десять',
    }
    result = storage.get(key)
    return result


print(num_translate_adv('Ten'))
