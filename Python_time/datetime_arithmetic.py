# Arithmetic using datetime, dateutil
# Author : Kiran raj r

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


now = datetime.now()
day_before = now - timedelta(days=+1)
next_day = timedelta(days=+1) + now

print(f"The yesterday this time will be: {day_before}")
print(f"The tomorrow this time will be: {next_day}")

now = datetime.now()
day_before = now - relativedelta(days=+1)
next_day = relativedelta(days=+1) + now

print(f"The yesterday this time will be: {day_before}")
print(f"The tomorrow this time will be: {next_day}")
print(f"{relativedelta(next_day, day_before)}")
print(f"{relativedelta(now, day_before)}")
print(f"{relativedelta(now, next_day)}")
