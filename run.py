from datetime import datetime
import exceptions as e

DAYS_OF_WEEK = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
DAYS_IN_THE_MONTH = [-1,31,29,31,30,31,30,31,31,30,31,30,31]

def is_leap_year(year):
    """
    Function to check if a given year is leap year or not

    Parameters:
        year(INTEGER)

    Returns:
        True(Boolean): if year is leap year
        False(Boolean): if year is not leap year 
    """
    return year%4==0 and (year%100!=0 or year%400==0)


def get_weekdays_count(date_dict):
    """
    This function calculates the sum value of weekdays from the provided input dictionary.
    

    Parameters:
        date_dict(dict): Dictionary consisting of dates(STRING) as key and value(INT)

    Returns:
        count_dictionary(dict): Dictionary consiting of Weekdays as keys and sum value as key
    
    """
    
    #check if date dictionary is empty
    if not bool(date_dict):
        return "date dictionary cannot be empty"

    SUN = False
    MON = False

    #initialize count dictionary
    count_dictionary = {i:0 for i in range(0,7)}

    for k,v in date_dict.items():
        try:
            date_object = datetime.strptime(k,'%Y-%m-%d').date()
            if not (1970 <= date_object.year <= 2100):
                raise e.YearOutOfRangeError("Year should be in the range 1970 - 2100")
        except ValueError:
            return "date not supplied in YYYY-MM-DD format"

        day_of_the_week = date_object.weekday()

        if day_of_the_week == 0:
            MON = True
        elif day_of_the_week == 6:
            SUN = True


        count_dictionary[day_of_the_week]  += v


    if not (MON and SUN):
        return "Date dictionary must contain dates of Sunday and Monday"

    count_dictionary = substitute_for_occurence_of_zero(count_dictionary)

    #replace week indexes with week names 
    count_dictionary = {DAYS_OF_WEEK[i]:count_dictionary[i] for i in range(0,7)}

    return count_dictionary



def substitute_for_occurence_of_zero(count_dictionary):
    """
    Function to substitute for occurence of zero . Mean of prev day and next day is filled 
    if for particualr day of week count is 0

    Parameters:
        count_dictionary(dictionary): dictionary consisting of counts

    Returns:
        count_dictionart(dictionary): modified dictionary to fill the occurence of zero 

    """
    for k,v in count_dictionary.items():
        if v == 0:
            count_dictionary[k] = (count_dictionary[k-1]+count_dictionary[k+1])//2
    
    return count_dictionary

        
        
