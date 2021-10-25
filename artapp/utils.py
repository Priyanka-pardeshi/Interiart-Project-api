import datetime
import re

# list of functions on which have to apply validation
def date_validation(date_data):
    # example of date format 2001M02
    # [\d]{4}M[\d]{2}
    # variable.group
    print("list of dates:",date_data)
    dates_return=[]
    for dates in date_data:
        print(dates)
        year=dates[0:4]
        month=dates[5:]
        #print("year:",year," month:",month)
        x = datetime.datetime(int(year),int(month), 13)
        print(x.strftime("%b %Y "))
        temp=x.strftime("%b %Y")
        dates_return.append(temp)
    return dates_return
