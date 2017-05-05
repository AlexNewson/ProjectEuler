print('''
Problem No. 19
Title:      Counting Sundays

Problem:    You are given the following information, but you may prefer to
            do some research for yourself.

                1 Jan 1900 was a Monday.

                Thirty days has September,
                April, June and November.
                All the rest have thirty-one,
                Saving February alone,
                Which has twenty-eight, rain or shine.
                And on leap years, twenty-nine.

            A leap year occurs on any year evenly divisible by 4, but not on a
            century unless it is divisible by 400.

            How many Sundays fell on the first of the month during the
            twentieth century (1 Jan 1901 to 31 Dec 2000)?
''')

import time

start = time.time()

# ==================================================
n_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Normal Year
l_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Leap Year
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

done = False
year = 1901
day_count = 0
count = 0

while not done:
    if year % 4 == 0:
        # Leap Year
        for month in l_year:
            for date in range(1, month + 1):
                if day_count == 6:
                    day_count = 0
                else:
                    day_count += 1
                day_name = week[day_count]
                if day_name == "Sunday" and date == 1:
                    count += 1
    else:
        # Normal Year
        for month in n_year:
            for date in range(1, month + 1):
                if day_count == 6:
                    day_count = 0
                else:
                    day_count += 1
                day_name = week[day_count]
                if day_name == "Sunday" and date == 1:
                    count += 1
    # Check Year
    if year < 2000:
        year += 1
    else:
        done = True


print("The Answer is: %i" % count)
# ==================================================

end = time.time()
time = end - start

print("This took %s seconds" % time)
