import datetime

def define_weekday(day_number: int) -> str:
    days_of_the_week = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Dimanche'
    }
    
    return days_of_the_week[day_number]


specific_date = datetime.datetime(year=2024, month=4, day=5)
specific_date = datetime.datetime(month=2, day=6, year=2023)
specific_date = datetime.datetime(month=11, year=2022, day=6, hour=23, minute=30, second=14, microsecond=999888)
print(specific_date)
day_of_the_week = define_weekday(datetime.datetime(month=2, day=7, year=2023).weekday())
print(f'Today is: {day_of_the_week}')
