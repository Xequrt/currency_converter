from online import get_currencies

# 1. Приветствие
# 2. Мануал – как пользоваться программой и какие валюты доступны
# 3. Ввести исходную валюту
# 4. Ввести в какую валюту перевести
# 5. Количество валюты
# 7. Вывод результата

online_response = get_currencies()['data']

def convert(amount, from_ticker, to_ticker, currencies):
    from_currency = currencies.get(from_ticker)
    to_currency = currencies.get(to_ticker)

    coefficient = to_currency / from_currency
    return round(amount * coefficient, 2)


def input_currency(input_message, currencies):
  try:
    ticker = input(f"{input_message}: ").strip().upper()
    if ticker not in currencies:
      raise ValueError(f'Данной валюты не существует: {ticker}')
    return ticker
  except ValueError:
    print(f'Неверный ввод: {ticker}, введите валюту из списка:'.format(ticker))
    print(''.join(f'{ticker} ' for ticker in currencies))
    return input_currency(input_message, currencies)
  
  


print("Привет, это программа Конвертер Валют!")

print("""
Для работы с программой требуется:
- выбрать исходную валюту 
- выбрать в какую валюту следует перевести
- ввести количество исходной валюты

Доступные валюты:
""")

for currency in online_response:
    print(f'- {currency}')
from_ticker = input_currency("Введите исходную валюту", online_response)
to_ticker = input_currency("Введите в какую валюту следует перевести", online_response)

amount_input = input("Введите количество валюты: ")
if amount_input.isdigit():
    amount = int(amount_input)
elif amount_input.replace('.', '', 1).isdigit():
  amount = float(amount_input)
else:
  print("Неверный ввод количества валюты")
  exit()

#if (isinstance(amount_input, int)):
#  amount = int(amount_input)
#elif (isinstance(amount_input, float)):
#  amount = float(amount_input)
#else:
#  print("Неверный ввод")
#  amount = 0

result = convert(amount, from_ticker, to_ticker, online_response)

print(f'Результат: {amount} {from_ticker} = {result} {to_ticker}')
