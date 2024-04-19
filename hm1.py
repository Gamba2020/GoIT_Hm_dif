from datetime import datetime
import re
def get_days_from_today():
    while True:
        date = input("Введіть дату у форматі 'РРРР-ММ-ДД': ")
        date = re.sub(r'[^a-zA-Z0-9]', '-', date)
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            today = datetime.today()
            difference = today - date
            return difference.days
        except ValueError:
            print("Неправильний формат дати. Спробуйте ще раз.")

print(get_days_from_today())
