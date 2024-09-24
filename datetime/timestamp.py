from datetime import datetime

# Поточний час
now = datetime.now()
print(type(now))
# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(type(timestamp))
print(timestamp)  # Виведе timestamp поточного часу

# Припустимо, є timestamp
timestamp = 1617183600

# Конвертація timestamp назад у datetime
dt_object = datetime.fromtimestamp(timestamp)
print(dt_object)  # Виведе відповідний datetime