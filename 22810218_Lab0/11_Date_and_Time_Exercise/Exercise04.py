# Print a date in a the following format
# Day_name  Day_number  Month_name  Year
# Refer: Python DateTime Format Using Strftime()

# Given:
# given_date = datetime(2020, 2, 25)

# Expected output:
# Tuesday 25 February 2020

import datetime

given_date = datetime.datetime(2020, 2, 25)
print(given_date.strftime("%A %d %B %Y"))

# Tuesday 25 February 2020