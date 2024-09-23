from datetime import datetime as dt, timedelta as td

delta = td(
    days=50, seconds=27, microseconds=10, milliseconds=29000, \
    minutes=5, hours=8, weeks=2
)
print(delta)

seventh_day_2019 = dt(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = dt(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0

birthday = dt(year=1966, month=4, day=5, hour=12)
total_life_delta = dt.now() - birthday
print(f'Total life seconds: {total_life_delta.total_seconds()}')