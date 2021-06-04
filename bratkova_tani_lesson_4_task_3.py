from requests import get
from datetime import date


def currency_rates(param):
    param = param.upper()
    data = get('https://www.cbr-xml-daily.ru/daily_json.js').json()

    if not data['Valute'].get(param): # Если такого наименования валюты нет в ответе сервера, то вернется None
        result =  f'{data["Valute"].get(param)} {type(data["Valute"].get(param))} валюты {param} не существует'
    else:
        currency = data['Valute'][param]
        name_currency = currency['Name']
        currency = currency['Value']

        # В Python 3.7 добавлен новый метод fromisoformat() для создания экземпляра даты из строки формата ISO.
        # Строка ввода должна быть в формате ГГГГ-ММ-ДД.
        date_answ = date.fromisoformat(data["Date"][:10]) # Дата с сервера прилетела в виде строки - преобразуем ее в тип дата

        result = f'На {date_answ} {type(date_answ)} курс валюты {param} ({name_currency}) равен {currency} руб. {type(currency)}'
    return print(result)


if __name__ == '__main__':
    currency_rates('CAd')
    currency_rates('usd')
    currency_rates('EUR')
    currency_rates('fgt')
    currency_rates('DKK')
