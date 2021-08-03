import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"

def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_info = datetime.strptime(iso_string, "%Y-%m-%dT%H:%M:%S%z")
    date_string = date_info.strftime("%A %d %B %Y")
    return date_string


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    subtract32 = float(temp_in_farenheit) - 32
    temp_in_c = subtract32 * .5556
    return round(temp_in_c,1)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum = 0 
    for temp in weather_data:
        sum = sum + float(temp)
        mean = sum / len(weather_data)
    return mean



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    data =  []

    with open(csv_file, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)
        for index, line in enumerate(csv_reader):
            if line != [] and index != 0:
                data.append([line[0],int(line[1]),int(line[2])])
        return data

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    # if len(weather_data) == 0:
    #     return ()
    # counter = float(weather_data[0])
    # temp_position = 0
    # for index, weather in enumerate(weather_data):
    #     if float(weather) >= counter:
    #         counter = float(weather)
    #         temp_position = index
    # return counter,temp_position

    if len(weather_data) == 0:
        return()
    for weather in range(0,len(weather_data)):
        weather_data[weather] = float(weather_data[weather])

    temp_min = min(weather_data) # find min value
    position = weather_data.reverse() #reverse list
    position = len(weather_data) - weather_data.index(temp_min) -1 #identify position
    return temp_min, position


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if len(weather_data) == 0:
        return ()
    counter = float(weather_data[0])
    temp_position = 0
    for index, weather in enumerate(weather_data):
        if float(weather) >= counter:
            counter = float(weather)
            temp_position = index
    return counter, temp_position


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    count = 0
    min_temps = []
    max_temps = []
    date_time = []

    for index, item in enumerate(weather_data):
        if index != []:
            count += 1
            date_time.append(item[0])
            min_temps.append(item[1])
            max_temps.append(item[2])
             
    min_temp, index_date_min = find_min(min_temps)
    max_temp, index_date_max = find_max(max_temps)

    min_temps_c = convert_f_to_c(str(min_temp))
    max_temps_c = convert_f_to_c(str(max_temp))

    date_min = date_time[index_date_min]
    date_max = date_time[index_date_max]

    mean_min_c = convert_f_to_c(calculate_mean(min_temps))
    mean_max_c = convert_f_to_c(calculate_mean(max_temps))

    result = ""
    result += f"{count} Day Overview\n"
    result += f"  The lowest temperature will be {format_temperature(min_temps_c)}, and will occur on {convert_date(date_min)}.\n"
    result += f"  The highest temperature will be {format_temperature(max_temps_c)}, and will occur on {convert_date(date_max)}.\n"
    result += f"  The average low this week is {format_temperature(mean_min_c)}.\n"
    result += f"  The average high this week is {format_temperature(mean_max_c)}.\n"

    return result

# 5 Day Overview
#   The lowest temperature will be 9.4°C, and will occur on Friday 02 July 2021.
#   The highest temperature will be 20.0°C, and will occur on Saturday 03 July 2021.
#   The average low this week is 12.2°C.
#   The average high this week is 17.8°C.

# def generate_summary(weather_data):
#     """Outputs a summary for the given weather data.
#     Args:
#         weather_data: A list of lists, where each sublist represents a day of weather data.
#     Returns:
#         A string containing the summary information.
#     """
    # count = 0
    # min_temps = []
    # max_temps = []
    # date_list = []
    # for index,item in enumerate(weather_data):
    #     if item !=[]:
    #         # print(item)
    #         count +=1
    #         date_list.append(item[0])
    #         min_temps.append(item[1])
    #         max_temps.append(item[2])
    # min_temp,index_date_min = find_min(min_temps)
    # max_temp,index_date_max = find_max(max_temps)
    # min_temp_c = convert_f_to_c(str(min_temp))
    # max_temp_c = convert_f_to_c(str(max_temp))
    # date_min = date_list[index_date_min]
    # date_max = date_list[index_date_max]
    # mean_min_c = convert_f_to_c(calculate_mean(min_temps))
    # mean_max_c = convert_f_to_c(calculate_mean(max_temps))
    # output = ""
    # output += f"{count} Day Overview\n"
    # output += f"  The lowest temperature will be {format_temperature(min_temp_c)}, and will occur on {convert_date(date_min)}.\n"
    # output += f"  The highest temperature will be {format_temperature(max_temp_c)}, and will occur on {convert_date(date_max)}.\n"
    # output += f"  The average low this week is {format_temperature(mean_min_c)}.\n"
    # output += f"  The average high this week is {format_temperature(mean_max_c)}.\n"
    # return output

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    result = ""

    for item in weather_data:
        result += f"---- {convert_date(item[0])} ----\n"
        result += f"  Minimum Temperature: {format_temperature(convert_f_to_c(item[1]))}\n"
        result += f"  Maximum Temperature: {format_temperature(convert_f_to_c(item[2]))}\n\n"

    return result
#     ---- Friday 02 July 2021 ----
#   Minimum Temperature: 9.4°C
#   Maximum Temperature: 19.4°C
