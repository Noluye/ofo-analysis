import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n').lower()
        if city in ['chicago', 'new york', 'washington']:
            break
        else:
            print('Your answer is not correct, please try again.\n')
    print('Looks like you want to hear about %s! If this is not true, restart the program now!\n\n' % city)
    
    # get user input for preferences of time filter
    while True:
        user_filter = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.\n').lower()
        if user_filter in ['month', 'day', 'both', 'none']:
            break
        else:
            print('Your answer is not correct, please try again.\n') 
    print('We will make sure to filter by %s!\n\n' % user_filter)

    # month can be assigned
    month = 'all'
    if user_filter == 'month' or user_filter == 'both':
        # get user input for month (all, january, february, ... , june)
        months = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
        while True:
            month_key = input('Which month? January, February, March, April, May, or June?\n').lower()
            if month_key in months:
                month = months[month_key]
                break
            else:
                print('Your answer is not correct, please try again.\n') 
        print('You will make sure to choose %s!\n\n' % month_key)
    # day can be assigned
    day = 'all'
    if user_filter == 'day' or user_filter == 'both':
        # get user input for day of week (all, monday, tuesday, ... sunday)
        days = {'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6}
        while True:
            day_key = input('Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday?\n').lower()
            if day_key in days:
                day = days[day_key]
                break
            else:
                print('Your answer is not correct, please try again.\n') 
        print('You will make sure to choose %s!\n\n' % day_key)
    print('-'*40)
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
    # Loads data for the specified city
    try:
        df = pd.read_csv(CITY_DATA[city]) 
    except Exception as e:
        print('The program encountered an error: ', e)
        exit()

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    # extract day from the Start Time column to create an day column
    df['day'] = df['Start Time'].dt.weekday
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # extract duration from the Start Time column and the End Time column to create an duration column
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['duration'] = df['End Time'].dt.date - df['Start Time'].dt.date
    
    # filter some rows based on user's filter
    if month == 'all' and day == 'all':
        return df
    elif month == 'all' and day != 'all':
        return df[df.day == day]
    elif month != 'all' and day == 'all':
        return df[df.month == month]
    else:
        return df[(df.month == month) & (df.day == day)]

def time_stats(df, month_is_all, day_is_all):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if month_is_all:
        # display the most common month
        popular_month = df['month'].mode()[0] # find the most popular month
        month = ['', 'January', 'February', 'March', 'April', 'May', 'June']
        print('Most popular month: %s\n' % month[popular_month])

    if day_is_all:
        # display the most common day of week
        popular_day = df['day'].mode()[0] # find the most popular week
        day = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        print('Most popular day of week: %s\n' % day[popular_day])
    
    # display the most common start hour
    popular_hour = df['hour'].mode()[0] # find the most popular hour
    print('\nMost popular hour: %d\n' % popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0] # find the most popular start station
    print('Most popular start station: %s\n' % popular_start_station)
    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0] # find the most popular end station
    print('Most popular end station: %s\n' % popular_end_station)
    # display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + ' --> ' + df['End Station']).mode()[0] # find the most popular start station
    print('Most popular trip: %s\n' % popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = 0
    for index, row in df.iterrows():
        total += row['duration'].total_seconds()
    print('\nTotal travel time: %f seconds\n' % total)

    # display mean travel time
    print('Count: %d\n' % len(list(df.index.values)))
    mean_val = total / len(list(df.index.values))
    print('Mean travel time: %f seconds\n' % mean_val)
   
    print("\nThis took %f seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nCalculating statistics...\n\n')
    print('What is the breakdown of users?\n')
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender
    print('\nCalculating statistics...\n\n')
    print('What is the breakdown of gender?\n')
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('No gender data to share.\n')

    # Display earliest, most recent, and most common year of birth
    print('\nCalculating statistics...\n\n')
    print('What is the oldest, youngest, and most popular year of birth, respectively?\n')
    if 'Birth Year' in df.columns:     
        print('Earliest year of birth: %d\n' % min(df['Birth Year'].dropna()))
        print('Recent year of birth: %d\n' % max(df['Birth Year'].dropna()))
        print('Most common year of birth: %d\n' % df['Birth Year'].dropna().mode()[0])
    else:
        print('No birth year data to share.\n')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month == 'all', day == 'all')
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
