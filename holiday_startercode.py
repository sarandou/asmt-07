import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
class Holiday:
    "enter date"
      
    def __init__(self,name, date):
        #Your Code Here   
        self.name = name
        self.date = date
        #self.date = datetime.strptime(date, '%Y-%m-%d').date()     
    
    def __str__ (self):
        # String output
        # Holiday output when printed.
        return f'{self.name} ({self.date})'
    
          
           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------
class HolidayList:
    def __init__(self):
       self.innerHolidays = []

    def addHoliday(self,holidayObj):
        # Make sure holidayObj is an Holiday Object by checking the type
        # Use innerHolidays.append(holidayObj) to add holiday
        # print to the user that you added a holiday
        if type(holidayObj) != Holiday:
            return "Not an accurate holiday"
        if type(holidayObj) == Holiday:
            self.innerHolidays.append(holidayObj)
            print(f'Added to holiday list')
            #return self.innerHolidays


    def findHoliday(self, HolidayName, Date):
        findHoliday = Holiday(HolidayName, Date)
        for i in self.innerHolidays:
            if i == findHoliday:
                return i 
        return False

        # Find Holiday in innerHolidays
        # Return Holiday

    def removeHoliday(self, HolidayName, Date):
        # Find Holiday in innerHolidays by searching the name and date combination.
        # remove the Holiday from innerHolidays
        # inform user you deleted the holiday
        removeHoliday = self.findHoliday(Holiday)
        if removeHoliday == False:
            return False
        else:
            self.innerHolidays.remove(removeHoliday)


    def read_json(self,filelocation):
        # Read in things from json file location
        # Use addHoliday function to add holidays to inner list.
        with open("holidays.json", 'r') as f:
            holidays = json.load(f)
            #holidays_list = dict['holidays']
        for i in holidays['holidays']:
            #holidayObj = Holiday(i['name'],i['date'])
            holiday_name = i['name']
            date = i['date']
            date = date.split('-')
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
            self.addHoliday(Holiday(holiday_name,date))


    def save_to_json(self, filelocation):
        holidays_out = json.dumps(self.innerHolidays, indent = None)
        with open('holidays.json', 'r') as f:
            f.write(holidays_out)

        # Write out json file to selected file.
        
    def scrapeHolidays(self):
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. You can scrape multiple years by adding year to the timeanddate URL. For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in innerHolidays array
        # Add non-duplicates to innerHolidays
        # Handle any exceptions.
        for year in range(2020,2025):
            response = requests.get(f'https://www.timeanddate.com/holidays/us/{year}')
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('tbody')
            for row in table.find_all('tr', attrs={'class':'showrow'}):
                webDate = row.find('th').string
                holiday_name = row.find('a').text
                date = str(year) + webDate
                convertDate = datetime.strptime(date,'%Y %b %d').date()
                holiday = {}
                holiday = Holiday(holiday_name['name'], convertDate['date'])
                self.addHoliday(holiday)
   

    def format_date(input):
        datetime.strptime(input, '%b %d %Y').strftime('%Y-%m-%d')
        pass


    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        print(f'Total holidays: {len(self.innerHolidays)}')
    
    # def filter_holidays_by_week(year, week_number):
    #     # Use a Lambda function to filter by week number and save this as holidays, use the filter on innerHolidays
    #     # Week number is part of the the Datetime object
    #     # Cast filter results as list
    #     # return your holidays
    #     pass

    # def displayHolidaysInWeek(holidayList):
    #     # Use your filter_holidays_by_week to get list of holidays within a week as a parameter
    #     # Output formated holidays in the week. 
    #     # * Remember to use the holiday __str__ method.
    #     pass

    # def getWeather(weekNum):
    #     # Convert weekNum to range between two days
    #     # Use Try / Except to catch problems
    #     # Query API for weather in that week range
    #     # Format weather information and return weather string.
    #     pass

    def viewCurrentWeek():
        # Use the Datetime Module to look up current week and year
        # Use your filter_holidays_by_week function to get the list of holidays 
        # for the current week/year
        # Use your displayHolidaysInWeek function to display the holidays in the week
        # Ask user if they want to get the weather
        # If yes, use your getWeather function and display results
        pass

    def menu(self):
        print('Holidays')
        print('-----------')
        print('1. Add a holiday')
        print('2. Remove a holiday')
        print('3. Save holiday list')
        print('4. View holidays')
        print('5. Exit')
        user_input = int(input('Choose an option'))
        if user_input in range(1,6):
            return user_input
        else:
            print('Not an option')


def main():
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    # 2. Load JSON file via HolidayList read_json function
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    # 3. Create while loop for user to keep adding or working with the Calender
    # 4. Display User Menu (Print the menu)
    # 5. Take user input for their action based on Menu and check the user input for errors
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 
    holidays = HolidayList()
    holidays.read_json('holidays.json')


    holidays.scrapeHolidays()
    holidays.numHolidays()
    #holidays.menu()
    ended = False
    while not ended:
        user_input = holidays.menu()
        #holidays.user_input()
        if user_input == 1:
            i = {}
            print('Add a holiday')
            i['name'] = input('Enter a holiday')
            i['date'] = input('Enter a date as YYYY-MM-DD')
            i = Holiday(i['name'],i['date'])
            holidays.addHoliday(i)
        if user_input == 2:
            print('Remove a holiday')
            holiday_name = input('Enter holiday name you want to remove')
            date = input("Enter holiday's date as YYYY-MM-DD")
            date = date.split()
            date = datetime.date(int(date[0]), int(date[1]), int(date[2]))
            remove_confirm = input('Do you want to remove? y/n')
            if remove_confirm == 'y':
                holidayObj = Holiday(holiday_name, date)
                HolidayList.removeHoliday(holiday_name, date)
            else:
                print('Not removed')
        if user_input == 3:
            print('Save holiday list')
            save_confirm = input('Do you want to save? y/n')
            if save_confirm == 'y':
                holidays.save_to_json('holidays.json')
            else:
                print('Not saved')
        if user_input == 4:
            print('View holidays')
        if user_input == 5:
            print('Exit')
            exit_confirm = input('Do you want to exit? y/n')
            if exit_confirm == 'y':
                print('Exiting')
                ended = True
            else: 
                print('Back to menu')
        else: 
            main()





if __name__ == "__main__":
    main();


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.





