from datetime import datetime as dt

first_strdate='10.05.2024'
second_strdate='26-June-2019'
third_strdate='5 Jan, 21'

first_date=dt.strptime(first_strdate, '%d.%m.%Y')
second_date=dt.strptime(second_strdate, '%d-%B-%Y')
third_date=dt.strptime(third_strdate, '%d %b, %y')

print(first_strdate, '->', first_date)
print(second_strdate, '->', second_date)
print(third_strdate, '->', third_date)

time = dt.now()

day_of_the_month = time.strftime("%d")
day_of_the_week = time.strftime(("%A"))
month = time.strftime("%B")
year = time.strftime("%Y")

format_of_time = time.strftime("%H:%M")
print('Today is', day_of_the_week+'.', 'It is', day_of_the_month, 'day of the', month, year)
print('Current time', format_of_time)

a_time = dt.now()
print(a_time.strftime('%a'))
A_time = dt.now()
print(A_time.strftime('%A'))

b_time = dt.now()
temp_date='11 Nov 2022'
today = dt.strptime(temp_date,'%d %b %Y')

print(today,'\n', b_time.strftime('%b'))

temp_date='11 November 2022'
today = dt.strptime(temp_date,'%d %B %Y')

print(today)

# Поточна дата та час
now = dt.now()

# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")