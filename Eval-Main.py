from eval_module1 import *
from eval_module2 import *
from eval_module3 import *
import os
from datetime import datetime

ending = os.environ['blacklist_ending']

input_blacklist_fi = os.environ['input_data_folder']

input_evaluation_files = os.environ['eval_data_folder']

averages_file = os.environ['output_averages']

percentages_file = os.environ['output_percentages']


def loop_through_all_blacklists_generate_stats(blacklist_directory, data_directory, total_averages_file, percentage_list_file, ending):
    list_of_blacklist_files = os.listdir(blacklist_directory)
    list_of_splunk_data_files = os.listdir(data_directory)
    number_of_processed_blacklists = 0
    list_of_blacklist_dates = []
    list_of_data_dates = []

    # These totals are needed in order calculate on average what percentage of data types are stopped
    total_byte_averages_for_table = 0
    total_packet_averages_for_table = 0
    total_duration_averages_for_table = 0
    total_event_averages_for_table = 0
    total_IPs_blocked_averages_for_table = 0

    # I want to save the actual average values in order to create a graphical comparison with traditional blacklist
    dictionary_of_data_averages_per_Day = {}

    for file in list_of_splunk_data_files:
        list_of_data_dates.append(file[:10])
    sorted_data_dates = sorted(list_of_data_dates, key=lambda date: datetime.strptime(date, '%Y-%m-%d'))

    for file in list_of_blacklist_files:
        list_of_blacklist_dates.append(file[:10])
    sorted_blacklist_dates = sorted(list_of_blacklist_dates, key=lambda date: datetime.strptime(date, '%Y-%m-%d'))
    print(sorted_blacklist_dates)

    for x,date in enumerate(sorted_blacklist_dates):
        print(date)
        number_of_processed_blacklists += 1
        stats_for_this_day = extract_stats_from_raw_data_file(data_directory + '/' + sorted_data_dates[x + 1] + '_splunk_raw.csv', open_blacklist_and_list_IPs(
            blacklist_directory + '/' + date + ending))
        # Add up the averages so I can get an overall average
        total_byte_averages_for_table += float(stats_for_this_day[0])
        total_packet_averages_for_table += float(stats_for_this_day[1])
        total_duration_averages_for_table += float(stats_for_this_day[2])
        total_event_averages_for_table += float(stats_for_this_day[3])
        total_IPs_blocked_averages_for_table += float(stats_for_this_day[4])

        # Create the entry for the big list of averages
        dictionary_of_data_averages_per_Day[date] = stats_for_this_day



    # Calculate the average percent of each data feature that was blocked by blacklists in data set
    print(number_of_processed_blacklists)
    dictionary_of_average_stats = {'average bytes blocked': total_byte_averages_for_table/number_of_processed_blacklists,
                                   'average packets blocked': total_packet_averages_for_table/number_of_processed_blacklists,
                                   'average duration blocked': total_duration_averages_for_table/number_of_processed_blacklists,
                                   'average events blocked': total_event_averages_for_table/number_of_processed_blacklists,
                                   'average IPs blocked': total_IPs_blocked_averages_for_table/number_of_processed_blacklists }

    # Arrange the data from all the days by day in decending order so that it will be easier to create graphs
    number = 1
    sorted_list = []
    for date in sorted_blacklist_dates:
        file_size = get_siz_of_file(blacklist_directory + '/' + date + '_blacklist.csv')
        list1 = []
        list1.append(number)
        list1.append(date)
        list1.extend(dictionary_of_data_averages_per_Day[date])
        list1.append(file_size)
        sorted_list.append(list1)
        number += 1


    # Write the results to files
    write_dictionary_to_csv(dictionary_of_average_stats, total_averages_file)
    #write_dictionary_to_csv(sorted_dictionary_by_date, percentage_list_file)
    write_list_to_file(sorted_list, percentage_list_file)


loop_through_all_blacklists_generate_stats(input_blacklist_files, input_evaluation_files, averages_file, percentages_file)
