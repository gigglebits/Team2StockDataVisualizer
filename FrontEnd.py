class FrontEnd:
    def frontEnd():
        #replace pass with front end code.
        #Ask for ticker, store as a string

        ticker = raw_input("Enter the ticker sybol of the company you would like to view:\n$")


        # ask if they would like a bar or line store as bool
        while(True):
            try:
                chartType = input("What chart type would you like?\n1. Bar\n2. Line\n")
                if chartType == 1:
                    chartType = False
                    break
                elif chartType == 2:
                    chartType = True
                    break
                else:
                    print("please enter either 1 or 2")
                    continue
            except:
                print("Please enter either 1 or 2")

        print(type(chartType))
        print(chartType)


        #ask what time series they would like store as int
        while(True):
            try:
                timeSeries = input("What time series would you like?\n1. Interday\n2. Daily\n3. Weekly\n4. Monthly\n")
                if timeSeries == 1:
                    break
                elif timeSeries == 2:
                    break
                elif timeSeries == 3:
                    break
                elif timeSeries == 4:
                    break
                else:
                    print("Please enter a number 1 through 4.")
            except:
               print("Please enter a number 1 though 4.")

        print(type(timeSeries))
        print(timeSeries)

        #ask for start date as dict
        currentTime = date.today()
        while(True):
            try:
                startYear = input("Please enter the year you would like for the data to start:\n")
                if startYear > currentTime.year:
                    print("Invalid year, please try again")
                elif (startYear < currentTime.year - 20):
                    print("Our records do not go back that far, please try again.")
                else:
                    break
            except:
                print("Invalid input, try again")

        print(type(startYear))
        print(startYear)

#date.startingDate.year = startYear
#print(startingDate)

        while(True):
            try:
                startMonth = input("Please select the Month you would like for the data to start:\n1. January\n2. February\n3. March\n4. April\n5. May\n6. June\n7. July\n8. August\n9. September\n10. October\n11. November\n12. December\n")
                if startMonth > 12:
                    print("Invalid input try again")
                elif ((startYear == currentTime.year- 20) and (startMonth < currentTime.month)):
                    print("Our records do not go back that far, please try again.")
                elif ((startYear == currentTime.year) and (startMonth > currentTime.month)):
                    print("Invalid month please try again")
                else:
                    break
            except:
                print("Invalid input, try again")

        print(type(startMonth))
        print(startMonth)

        while(True):
            try:
                startDay = input("Please enter the day you would like for the data to start:\n")
                if ((startMonth == 4 or 6 or 9 or 11) and (startDay > 30)):
                    print("there are only 30 days in this month, please try again")
                elif ((startMonth == 1 or 3 or 5 or 7 or 8 or 10 or 12) and (startDay > 31)):
                    print("There are only 31 days in this month, please try again")
                elif ((startYear == currentTime.year- 20) and (startMonth == currentTime.month) and (startDay)):

                elif (((startYear % 4 == 0 and startYear % 100 != 0) or (startYear % 400 == 0)) and (startMonth == 2) and (startDay > 29)):
                    print("You input a leap year, there are only 29 days in this month, please try again")
                elif (((startYear % 4 != 0 and startYear % 100 == 0) or (startYear % 400 != 0)) and (startMonth == 2) and (startDay > 28)):
                    print("There are only 28 days in this month, please try again")
                elif startDay > 1:
                    print("Invalid date, please try again")
                else:
                    break
            except:
                print("Invalid input, try again")

#ask for end date store as dict

#initiate a queryinput object with chosen data

#return queryInput object
