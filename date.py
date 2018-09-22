'''
Created on Nov 22, 2017
@author: bobby
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
- hgeorgio
CS115 - Hw 11 - Date class
'''

DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
DAYS_OF_WEEK = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
        as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def copy2(self, d2):
        '''Returns a new object with the same month, day, year
        as Date d2.'''
        dnew = Date(d2.month, d2.day, d2.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day
            
    def tomorrow(self):
        ''' Changes self to the next date; returns nothing '''
        if self.day < DAYS_IN_MONTH[self.month]:
            self.day += 1
        elif self.day >= DAYS_IN_MONTH[self.month]:
            if self.month == 2 and self.isLeapYear() and self.day < 29:
                self.day += 1
            elif self.month == 12:
                self.year += 1
                self.month = 1
                self.day = 1
            else:
                self.month += 1
                self.day = 1
    
    def yesterday(self):
        ''' Changes self to the previous date; returns nothing '''
        if self.day == 1:
            if self.month == 3 and self.isLeapYear():
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month] + 1
            elif self.month == 1:
                self.year -= 1
                self.month = 12
                self.day = DAYS_IN_MONTH[12]
            else:
                self.month -= 1
                self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1
                
    def addNDays(self, N):
        ''' Adds N days from Date self and prints all dates between the start and end, including the start and end dates '''
        print(self)
        for _ in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        ''' Subtracts N days from Date self and prints all dates between the start and end, including the start and end dates '''
        print(self)
        for _ in range(N):
            self.yesterday()
            print(self)
            
    def isBefore(self, d2):
        ''' Returns boolean value representing if Date self is before Date d2 '''
        if d2.year > self.year: 
            return True
        elif d2.year < self.year:
            return False
        if d2.month > self.month: 
            return True
        elif d2.month < self.month:
            return False
        if d2.day > self.day:
            return True
        elif d2.day <= self.day:
            return False
        
    def isAfter(self, d2):
        ''' Returns boolean value representing if Date self is after Date d2 '''
        if d2.year < self.year: 
            return True
        elif d2.year > self.year:
            return False
        if d2.month < self.month: 
            return True
        elif d2.month > self.month:
            return False
        if d2.day < self.day:
            return True
        elif d2.day >= self.day:
            return False
        
    def diff(self, d2):
        ''' Returns difference in days between Dates self and d2 '''
        d2c = self.copy2(d2)
        dayscount = 0
        if self.isAfter(d2):
            while not self.equals(d2c):
                d2c.tomorrow()
                dayscount += 1
        elif self.isBefore(d2):
            while not self.equals(d2c):
                d2c.yesterday()
                dayscount -= 1
        return dayscount
    
    def dow(self):
        ''' Returns the day of week as a string of the Date self '''
        ref = Date(1, 1, 2017) # Sunday
        diffrem = self.diff(ref) % 7
        return DAYS_OF_WEEK[diffrem]
        
if __name__ == '__main__':
    d = Date(11, 9, 2011)
    d2 = Date(12, 16, 2011)
    print(d.isBefore(Date(1, 2, 2016)))
    print(d.isAfter(Date(5, 6, 2016)))
    print(d2.diff(d))
    print(d.diff(d2))
    print(d.dow())
    print(d2.dow())
