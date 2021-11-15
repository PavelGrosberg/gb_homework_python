import re

regex = re.compile(r'([a-z0-9]+)(@)([a-z0-9]+\.[a-z]+)')


def email_parse(email):
    match_list = regex.findall(email)[0]
    # print(match_list)
    if match_list:
        user, dog, dom = match_list
    else:
        raise ValueError(f'wrong email: {email}')
    return user, dog, dom


print(email_parse('someone@geekbrains.ru'))
print(email_parse('someone@geekbrainsru'))
