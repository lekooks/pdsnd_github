### Date created
This project and Readme File were created Sunday 13.01.2019.

### Project Title
bikeshare_stefan_ziegler

### Description
This project was created for Udacity's Programming for Data Science Nanodegree programm.
It takes data from csv files which were given as prerequisites. The main file is the bikeshare_stefan_ziegler.py script.
When it is being run via a terminal it will conjour up a friendly script to guide through some data analysis.
The user will be prompted to enter some data which will function as filters for the analysis.
The scricpt will then return useful insights and statistics.

### Files used
bikeshare_stefan_ziegler.py
chicago.csv
new_york_city.csv
washington.csv

### Credits
#### Comments on Project original Submission
The most changes I made were to the displayed text and display to make the script nicely readable and "friendly"

#### Comments on Sourcing:
Most applied solutions to subproblems in the functions were directly taken from the udacity course.
The Pactice Solutions were espacially applied direcly.

#### Comments on Foreign Sources
##### General Input and Relearch
Generally https://stackoverflow.com/ was used as resource for errors. 

##### Adapted Concept I
For the trip duration section I was unhappy with the displayed results.
The raw data and thus the data frame hold the duration information in seconds.

The answer of user "Highstaker" to question:
https://stackoverflow.com/questions/4048651/python-function-to-convert-seconds-into-minutes-hours-and-days/4048773
was used to introduce a slightly adapted version of their secondsToText() function to my code
My version additionally will round up the ammout for the seconds

This is the Version that was found on the web and largely applied in my submission.

> def secondsToText(secs):
>     days = secs//86400
>     hours = (secs - days*86400)//3600
>     minutes = (secs - days*86400 - hours*3600)//60
>     seconds = secs - days*86400 - hours*3600 - minutes*60
>     result = ("{0} day{1}, ".format(days, "s" if days!=1 else "") if days else "") + \
>     ("{0} hour{1}, ".format(hours, "s" if hours!=1 else "") if hours else "") + \
>     ("{0} minute{1}, ".format(minutes, "s" if minutes!=1 else "") if minutes else "") + \
>     ("{0} second{1}, ".format(seconds, "s" if seconds!=1 else "") if seconds else "")
>     return result


##### Adapten Concept II
To introduce random friendly messages for user input errors I got help from this post:
https://stackoverflow.com/questions/3998908/how-do-i-perform-a-random-event-in-python-by-picking-a-random-variable

It needed to be adatped for propper string output 

> import random
> dog = 5
> cat = 3
> vars = [dog,cat]
> print random.sample(vars, 1)