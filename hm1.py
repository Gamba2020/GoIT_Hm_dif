from datetime import datetime
import re
def get_days_from_today(date):
    date = re.sub(r'[^a-zA-Z0-9]', '-', date)
    try:
        date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        difference = today - date
        return difference.days
    except ValueError:
        print("Неправильний формат дати. Спробуйте ще раз.")

print(get_days_from_today("2024-05-04"))
