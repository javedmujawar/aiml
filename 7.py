import datetime

current_datetime = datetime.datetime.now()
print("current_datetime ", current_datetime)

current_date = datetime.date.today()
print("current_date ", current_date)

date_obj = datetime.date(2024,4,23)
print("date_obj ", date_obj)

formatted_date = current_date.strftime("%d-%b-%Y")
print('Formatred Date: ', formatted_date)

year = date_obj.year
month = date_obj.month
day = date_obj.day
print("year ", year)
print("month ", month)
print("day ", day)

weekday = date_obj.weekday
print("weekday", weekday)

date1 = datetime.date(2024,4,23)
date2 = datetime.date(2024,4,25)

date_diff = date2 - date1

print('date diff ', date_diff)

new_date =date1 +  datetime.timedelta(days=7)
print('New date:', new_date)

is_leep_year = datetime.date(2024,1,1).year % 4 == 0
print("is leep year? ", is_leep_year)
