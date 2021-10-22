def thesaurus(*val):
    dictionary = {}
    i = 0
    while i < len(val):
        key = val[i][0]
        dictionary.setdefault(key, val[i])
        i += 1
    dictionary = {key: [value] for key, value in dictionary.items()}
    i = 0
    while i < len(val):
        key = val[i][0]
        if [val[i]] not in dictionary.values():
            dictionary[key].append(val[i])
        i += 1
    return dictionary


print(thesaurus('Иван', 'Мария', 'Петр', 'Илья'))
print(thesaurus('Павел', 'Роман', 'Анна', 'Артём', 'Эмилия'))
