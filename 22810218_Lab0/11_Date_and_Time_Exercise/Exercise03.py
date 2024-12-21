# Subtract a week (7 days)  from a given date in Python
# Refer: TimeDelta in Python

# Given:
# given_date = datetime(2020, 2, 25)

# Expected output:
# 2020-02-18

import datetime

given_date = datetime.datetime(2020, 2, 25)
new_date = given_date - datetime.timedelta(days=7)
print(new_date)

# 2020-02-18