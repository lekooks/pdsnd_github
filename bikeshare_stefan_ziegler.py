#import packages
import time
import pandas as pd
import numpy as np
import random as rd
import json as js

# introduce dictionaries to handle and verify user input strings
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ('chicago', 'new york city', 'washington')
months = ('january', 'february', 'march', 'april', 'may', 'june')
days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

no_filter = ('all')
answers_yn= ('yes', 'no')                

# introduce error messages that can be used randomly to make the script appear more engaging
input_error_1 = "Sorry, I do not recognize your input. Did you mistype by any chance?\nPlease try again!\n"
input_error_2 = "Sorry, I don\'t understand what you\'re saying. Did you misspell it by any chance?\nPlease try again!\n"
input_error_3 = "Sorry, I\'m not reading you right. Am I looking at a typo by any chance?\nPlease try again!\n"

input_errors = [input_error_1, input_error_2, input_error_3]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hi there! Let\'s explore some US bikeshare data together!\nI\'m a friendly script to guide you through.')
    
    # get user input for city, handle errors
    while True:
      print("Which city would you like to explore? \nWe have data in store for Chicago, New York City and Washington.\n")
      city = input("Type the city to choose: ").lower()
      if city not in cities:
        print(input_errors[rd.randint(0, 2)])
      elif city in cities:
        print("Thanks! I'll filter results for city \"{}\"!".format(city))
        break

    # get user input for month, handle errors
    while True:
      print("Let's move on to choosing a month! \nPlease choose a month by typing January, February, March,... or type \"all\" to apply no filter\n")
      month = input("Type the month to choose: ").lower()
      if month == no_filter:
        print("Ok! I\'ll not apply a filter by month!")
        break  
      elif month in months:
        print("Thanks! I'll filter results for month \"{}\"!".format(month))
        break  
      elif month not in months:
        print(input_errors[rd.randint(0, 2)])
  
    # get user input for day of week, handle errors
    while True:
      print("Let's move on to choosing a day!\nYou can choose a day by typing Monday, Tuesday, Wednesday,... or type \"all\" to apply no filter\n")
      day = input("Type the day to choose: ").lower()
      if day == no_filter:
        print("Ok! I\'ll not apply a filter by day!")
        break  
      elif day in days:
        print("Thanks! I'll filter results for day \"{}\"!".format(day))
        break        
      elif day not in days:
        print(input_errors[rd.randint(0, 2)])
       
     # summarize user input
    print("-"*80 + "\n" + '-'*80 + "\nYour total filter settings include \"City: {}, Month: {}, Day: {}\"\n".format(city, month, day) + "-"*80 + "\n" + '-'*80)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #create dataframe and transpose start time to datetime format
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #create new separate colums for time measures and account for user input filters
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    #check of month was filtered and create a new data frame for filtered month if applicable  
    if month not in no_filter:
        month = months.index(month) +1
        df = df[ df['month'] == month ]
    #check of day was filtered and create a new data frame for filtered day if applicable
    if day not in no_filter:  
        df = df[ df['day_of_week'] == day.title() ]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nI\'m happy to calculate The Most Frequent Times of Travel for you...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['month'].value_counts().idxmax()
    print("The most popular month is:      {}".format(most_common_month))
    # display the most common day of week
    most_common_dow = df['day_of_week'].value_counts().idxmax()
    print("The most popular weekday is:    {}".format(most_common_dow))
    # display the most common start hour
    most_common_hour = df['hour'].value_counts().idxmax()
    print("The most popular Start Time is: {}".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print("\nI\'m happy to calculate The Most Popular Stations and Trip for you...\n")
    start_time = time.time()

    # display most commonly used start station
    most_common_start = df['Start Station'].mode().loc[0]
    print("The most popular station to start from is: {}".format(most_common_start))
    # display most commonly used end station
    most_common_end = df['End Station'].mode().loc[0]
    print("The most popular station to end on is:     {}".format(most_common_end))
    # display most frequent combination of start station and end station trip
    most_common_pair = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most popular pair of stations is:\n From: {}\n To:   {}".format(most_common_pair[0], most_common_pair[1]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def seconds_to_text(secs):
    """Introduces a way to print out Trip Duration results in a manner that is 
    easily grasped by the user
    
    The Dataframe introduces this data in seconds. The function will translate 
    and prit this to days, hours, minutes, seconds
    """
    days = secs//86400
    hours = (secs - days*86400)//3600
    minutes = (secs - days*86400 - hours*3600)//60
    seconds = round(secs - days*86400 - hours*3600 - minutes*60)
    result = ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
    ("{0} hour{1}, ".format(hours, "s" if hours!=1 else "") if hours else "") + \
    ("{0} minute{1}, ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
    ("{0} second{1}, ".format(seconds, "s" if seconds!=1 else "") if seconds else "")
    return result


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print("\nI\'m happy to calculate Trip Duration for you...\n")
    start_time = time.time()

    # display total travel time
    total_travel_time = seconds_to_text(df['Trip Duration'].sum())
    print("The total travel time is {}".format(total_travel_time))

    # display mean travel time
    mean_travel_time = seconds_to_text(df['Trip Duration'].mean())
    print("The mean travel time is {}".format(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def user_stats(df):
    """Displays statistics on bikeshare users"""

    print('\nI\'m happy to calculate User Stats for you...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("These User Types occur in the data:\n{}".format(user_type_counts))

    # Display counts of gender; 
    # Introduce a check if this data point exists in the data first
    if 'Gender' in df: 
      gender_counts = df['Gender'].value_counts()
      print("\nThese genders occur in the data:\n{}".format(gender_counts))
    else:
      print("\nSorry there are no data points for me to provide information on gender.")
    

    # Display earliest, most recent, and most common year of birth; 
    # introduce a check if this data point exists in the data first
    if 'Birth Year' in df:
      earl_dob = int(df['Birth Year'].min())
      mrec_dob = int(df['Birth Year'].max())
      mode_dob = int(df['Birth Year'].mode())
      print("\nThe oldest user was born in:   {}\nThe youngest user was born in: {}\nMost users are born in:        {}".format(earl_dob, mrec_dob, mode_dob))
    else:
      print("Sorry there are no data points for me to provide information on birth years\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*80)


def raw_data(df):
    """
    Prompts the user and asks if they would like to see 5 sets of raw data
    in a "yes" or "no" question. Repeats and outputs the data until users chooses "no"
    """
    row_length = df.shape[0]
  # go from 0 to the number of rows in steps of 5 to print 5 data sets
    for i in range(0, row_length, 5):

      user_input = input("\nI'm happy to show you some sets of raw data used to calculate these statistics.\nWould you like to see them? Let me know by typing \"yes\" or \"no\":\n\n>>>").lower()
      if user_input not in answers_yn:
        print(input_errors[rd.randint(0, 2)])
      if user_input == 'no':
        print("Got it! That was enough raw data examples.")
        break
      elif user_input == 'yes':  
      # get and convert raw data to json objects
        rows = df.iloc[i: i + 5].to_json(orient='records', lines=True).split('\n')
        for row in rows:
            # prettify data sets
            pretty_json = js.loads(row)
            data_set = js.dumps(pretty_json, indent=2)
            print(data_set)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nTo restart enter \"yes\". Otherwise hit any key and your friendly exploration script will close!\n\n>>>')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
  main()