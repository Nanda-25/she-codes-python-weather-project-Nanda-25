import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp): #DONE
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"
# print(format_temperature(89))


def convert_date(iso_string): #DONE
    dt = datetime.fromisoformat(iso_string)
    week_day = dt.strftime("%A")
    day = dt.strftime("%d")
    month = dt.strftime("%B")
    year = dt.strftime("%Y")
    return f"{week_day} {day} {month} {year}"

    """Converts and ISO formatted date intso a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    pass


def convert_f_to_c(temp_in_farenheit): #DONE
    c_temp = (float (temp_in_farenheit) - 32) * 5 / 9
    c_temp = round (c_temp, 1)
    return c_temp

    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    pass

def calculate_mean(weather_data): #DONE
    sum = 0
    counter = 0
    mean = 0
    for value in weather_data:
        sum += float(value)
        counter += 1  
        mean = sum / counter
    return mean

    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    pass

def load_data_from_csv(csv_file):
    new_list = [] 

    with open(csv_file, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for line in reader:
            if len(line) != 0:
                new_list.append([line[0],int(line[1]),int(line[2])])
    # print(new_list) I do not need it.
    return new_list
# load_data_from_csv("tests/data/example_one.csv")

    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass

def find_min(weather_data):#DONE
    min_temp = 150
    position = 0

    if (weather_data) == []:
        return ()
    else:
        for item_index in range(len(weather_data)):# range is the number of interations - refer to item (index)
            temp = float(weather_data[item_index])
            if temp <= min_temp: #<= means that if it finds a duplicate min value, it will override.
                min_temp = temp
                position = item_index
            # print(min_temp)
        return min_temp, position

    """Calculates the minimum value in a list of numbers.
    
    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data): #DONE
    max_temp = 0 #is not comparing as ==. It is defining it. 
    position = 0

    if (weather_data) == []:
        return ()
    else:# range is the number of interations - refer to item (index)
        for item_index in range(len(weather_data)):
            temp = float(weather_data[item_index])
            if temp >= max_temp: #>= means that if it finds a duplicate min value, it will override.
                max_temp = temp
                position = item_index
        return max_temp, position
    
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    # summary = ""
    high_temp_list = []
    low_temp_list = []
    day_overview = len(weather_data)

    for line in weather_data:
        # low_temp = line[1]
        low_temp_list.append(convert_f_to_c(line[1])) # list in Celsius already created
        # high_temp = line[2]
        high_temp_list.append(convert_f_to_c(line[2])) # list in Celsius already created
    
    mean_high = calculate_mean(high_temp_list) 
    f_mean_high = format_temperature(round(mean_high,1))

    mean_min = calculate_mean(low_temp_list)
    f_mean_min = format_temperature(round(mean_min,1))

    low_temp_c = find_min(low_temp_list)
    low_temp_c_f = format_temperature(low_temp_c[0])
    date_min = convert_date(weather_data[low_temp_c[1]][0])

    high_temp_c = find_max(high_temp_list)
    high_temp_c_f = format_temperature(high_temp_c[0])
    date_max = convert_date(weather_data[high_temp_c[1]][0])

    summary=(f"{day_overview} Day Overview\n  The lowest temperature will be {low_temp_c_f}, and will occur on {date_min}.\n  The highest temperature will be {high_temp_c_f}, and will occur on {date_max}.\n  The average low this week is {f_mean_min}.\n  The average high this week is {f_mean_high}.\n")
    print(summary)
    return summary

# generate_summary(load_data_from_csv("tests/data/example_one.csv"))

    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data): 
    daily_summary = ""
    for item in weather_data:
        formatted_date = convert_date(item[0])
        min_temp_c = convert_f_to_c(item[1])
        formatted_min_temp = format_temperature(min_temp_c)
        max_temp_c = convert_f_to_c(item[2])
        formatted_max_temp = format_temperature(max_temp_c)
        daily_summary += f"---- {formatted_date} ----\n  Minimum Temperature: {formatted_min_temp}\n  Maximum Temperature: {formatted_max_temp}\n\n"
    print(daily_summary)
    return daily_summary


# generate_daily_summary(load_data_from_csv("tests/data/example_one.csv"))

    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
