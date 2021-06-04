# Это решение я свистнула из интернета, т.к. я до сих пор не имела дела с этой темой,
# то мне вообще непонятно было как это решать, а методичка к уроку 4, к сожалению, отвратительна.
# В этом готовом решении я увидела, что прилетает словарь, с которым очень удобно работать.
# Надеюсь, все-таки, что задачу я выполнила.

from requests import get


def currency_rates(param):
    param = param.upper()
    data = get('https://www.cbr-xml-daily.ru/daily_json.js').json()

    if not data['Valute'].get(param): # Если такого наименования валюты нет в ответе сервера, то вернется None
        result =  f'{data["Valute"].get(param)} {type(data["Valute"].get(param))} валюты {param} не существует'
    else:
        currency = data['Valute'][param]
        name_currency = currency['Name']
        currency = currency['Value']
        result = f'Курс валюты {param} ({name_currency}) равен {currency} руб. {type(currency)}'
    return print(result)


if __name__ == '__main__':
    currency_rates('CAd')
    currency_rates('usd')
    currency_rates('EUR')
    currency_rates('fgt')
    currency_rates('DKK')
