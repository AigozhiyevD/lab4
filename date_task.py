# Task 1

from datetime import datetime, timedelta

#current date
current_date = datetime.now()

#minus five days
new_date = current_date - timedelta(days=5)

# printing
print(current_date.strftime('%Y-%m-%d'))
print(new_date.strftime('%Y-%m-%d'))

# Task 2

current_date = datetime.now()
yesterday = current_date - timedelta(days=1)
tomorrow = current_date + timedelta(days=1)

print(yesterday.strftime('%Y-%m-%d'))
print(current_date.strftime('%Y-%m-%d'))
print(tomorrow.strftime('%Y-%m-%d'))

# Task 3

now = datetime.now()
cleaned_now = now.replace(microsecond=0)

print("Original datetime:", now)
print("Datetime without microseconds:", cleaned_now)

# Task 4

date1 = datetime(2025, 2, 22, 14, 30, 0)
date2 = datetime(2025, 2, 21, 12, 15, 0)

difference = abs((date1 - date2).total_seconds())

print(difference)