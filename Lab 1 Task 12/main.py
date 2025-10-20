#Задача 12. Счет за телефон
# Ввод данных
minutes = int(input("Минуты: "))
sms = int(input("СМС: "))
mb = int(input("МБ: "))

# Базовый тариф
base_price = 24.99
base_minutes = 60
base_sms = 30
base_mb = 1024  # 1 ГБ = 1024 МБ

# Дополнительные расходы
extra_minutes = max(0, minutes - base_minutes) * 0.89
extra_sms = max(0, sms - base_sms) * 0.59
extra_mb = max(0, mb - base_mb) * 0.79

# Суммы
extra_total = extra_minutes + extra_sms + extra_mb
total_before_tax = base_price + extra_total
tax = total_before_tax * 0.02
total = total_before_tax + tax

# Вывод
print(f"\nБазовая стоимость: {base_price:.2f} руб.")

if extra_minutes > 0:
    print(f"Доп. минуты: {extra_minutes:.2f} руб.")
if extra_sms > 0:
    print(f"Доп. СМС: {extra_sms:.2f} руб.")
if extra_mb > 0:
    print(f"Доп. трафик: {extra_mb:.2f} руб.")

print(f"Налог 2%: {tax:.2f} руб.")
print(f"Итого к оплате: {total:.2f} руб.")