import time
import euler

euler.print_problem(19)
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
