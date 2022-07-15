#The dateFilter class has a dateFilter method. This method will need to take a dictionary (data) and return a modified dictionary #that excludes values outside the user's choices
#Start date and end date will also be in the dictionary format. Example below

#dictionary example 
    #startDate = {
        # "year" : 2007
        # "month" : 11
        # "day" : 12
        # }
from datetime import datetime

class dateFilter:
    def dateFilter(data, startDate, endDate):
        #data is passed to the date filter method in a dictionary.
        startYear = startDate.get("year")
        startMonth = startDate.get("month")
        startDay = startDate.get("day")
        startDate = datetime.strptime(f"{startYear}-{startMonth}-{startDay} 00:00:00", "%Y-%m-%d %H:%M:%S")

        endYear = endDate.get("year")
        endMonth = endDate.get("month")
        endDay = endDate.get("day")
        endDate = datetime.strptime(f"{endYear}-{endMonth}-{endDay} 00:00:00", "%Y-%m-%d %H:%M:%S")

        for x in data.keys():
            if 'Meta' in x:
                continue
            else: 
                interval = x

        realData = data.get(interval)

        for y in list(realData.keys()):
            try:
                date = datetime.strptime(y, "%Y-%m-%d %H:%M:%S")
            except:
                date = datetime.strptime(f"{y} 00:00:00", "%Y-%m-%d %H:%M:%S")

            if(date < startDate or date > endDate):
                realData.pop(y)

        #print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        #print(realData)
        return realData

