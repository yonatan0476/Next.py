# 4.4


# 1
def gen_secs():
    for i in range(60):
        yield i


# 2
def gen_minutes():
    for i in range(60):
        yield i


# 3
def gen_hours():
    for i in range(24):
        yield i


# 4
def gen_time():
    for hour in gen_hours():
        for min in gen_minutes():
            for sec in gen_secs():
                yield "%02d:%02d:%02d" % (hour, min, sec)


# 5
def gen_years(start=2023):
    while True:
        yield start
        start += 1


# 6
def gen_months():
    for i in range(1, 13):
        yield i


# 7
def gen_days(month, leap_year=True):
    days_in_month_dict = {1: 31, 2: (28, 29), 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if month != 2:
        for i in range(1, days_in_month_dict[month] + 1):
            yield i
    else:
        if leap_year:
            for i in range(1, days_in_month_dict[month][1] + 1):
                yield i
        else:
            for i in range(1, days_in_month_dict[month][0] + 1):
                yield i


# 8
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def gen_date():
    for year in gen_years():
        leap_year = is_leap_year(year)
        for month in gen_months():
            for day in gen_days(month, leap_year):
                for exact_time in gen_time():
                    yield "%02d:%02d:%04d " % (day, month, year) + exact_time


# 9
date = gen_date()
i = 0
while True:
    next(date)
    i += 1
    if i == 1000000:
        print(next(date))
        i = 1
