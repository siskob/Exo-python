from datetime import datetime, timedelta

timedelta(days=20)
now = datetime.now()

now_in_15_days_minus_5_hours = now + timedelta(days=15, hours=-5)

print(now)
print(now_in_15_days_minus_5_hours)

