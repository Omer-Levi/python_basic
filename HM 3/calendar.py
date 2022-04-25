"""
Student: Omer levi
ID: 203499090
Assignment no. 3
Program: calendar.py
"""


months = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
           "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}


def leap_year(year):  #function for finding a leap year
    return True if (not(year % 400)) or (not(year % 4)and (year%100)) else False


def calculate_month(year, month):  #A function that calculates the months
    days = 0

    for i in range(1900, year):
        if leap_year(i):
            days += 366
        else:
            days += 365
    for index, (key, value) in enumerate(months.items()):
        if key == month:
            break
        if key == "Feb" and leap_year(year):
            days += 29
            continue
        else:
            days += value
    res = (days % 7) + 2
    return res


if __name__ == "__main__":

    month = input('Enter the name of the month: ')
    year = input('Enter the name of the year: ')
    res = calculate_month(int(year), month)
    print(month + " " + year)
    print("Su  Mo  Tu  We  Th  Fr  Sa")
    mun_of_days = months[month]
    string = " "
    days_left = 7-res+1
    days_till = 7-days_left
    x = [i for i in range(1, mun_of_days+1)]
    x = [x[i: i + 7] for i in range(days_left, mun_of_days+1, 7)]
    first_week = ["  " for _ in range(days_till)]
    for i in range(1, days_left+1):
        first_week.append(i)
    x.insert(0,first_week)
    for i in x:
        print('  '.join(str(l) if len(str(l)) == 2 else (str(l)+ " ") for l in i ))