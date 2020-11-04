# Calculate the number of days to the PYCON 2021, using time aware datetime calculation
# Author : Kiran raj r

from datetime import datetime
from dateutil import tz
from dateutil.relativedelta import relativedelta
indian_tz = tz.gettz('Asia/Kolkata')

now = datetime.now(tz=tz.tzlocal())
now_ist = datetime.now(tz=indian_tz)

PYCON_date = datetime(year=2021, month=5, day=12, hour=8,
                      tzinfo=tz.gettz('America/New_York'))
countdown = relativedelta(PYCON_date, now)
str_countdown = str(countdown).split(",")
str_countdown[0] = str_countdown[0].split('(')[1]
new_countdown = []
for i in str_countdown:
    i = i.split('=+')
    msg = f"{i[0].upper().strip()} : {i[1]}"
    new_countdown.append(msg)
print(f"Days to the PYCON event 2021: {new_countdown}")


# print(indian_tz)        # tzfile('Asia/Calcutta')
# print(now.tzname())     # India Standard Time
# print(now, now_ist)
# # 2020-11-04 22:20:20.661700+05:30 2020-11-04 22:20:20.661700+05:30
