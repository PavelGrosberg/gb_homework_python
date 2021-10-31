import requests
import re
import datetime
import decimal

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url).text.split('"')


def currency_rates(ue=input().upper()):
    for char_code in response:
        if char_code.find(f'<CharCode>{ue}</CharCode>') != -1:
            value = re.split('<Value>|</Value>', char_code)[1].replace(',', '.')
            print(decimal.Decimal(value))
    return None


days, month, years = map(int, response[5].split('.'))
print(datetime.datetime(years, month, days))
currency_rates()
