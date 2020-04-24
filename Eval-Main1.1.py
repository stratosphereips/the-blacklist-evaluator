from eval_module2 import extract_stats_from_raw_data_file as compare_files_and_create_stats
from eval_module2 import open_blacklist_and_list_IPs
from eval_module3 import read_csv_to_dictionary
from eval_module3 import write_dictionary_to_csv
from eval_module3 import write_list_to_file
from eval_module1 import get_siz_of_file
import os
from datetime import datetime


directory_where_the_blacklist_files_can_be_found = '/home/thomas/Test/Gradual/B20-E20/Out-Put-Files/Historical_Blacklists/All-Time-Prioritize-Consistent'

directory_where_the_data_files_can_be_found = '/home/thomas/Test/Data_For_testing/'

averages_file = '/home/thomas/Test/Gradual/B20-E20/Eval/averages.csv'

percentages_file = '/home/thomas/Test/Gradual/B20-E20/Eval/all_percentages.csv'


def loop_through_all_blacklists_and_datasets_and_generate_stats(blacklist_directory, data_directory, total_averages_file, percentage_list_file):
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
        stats_for_this_day = compare_files_and_create_stats(data_directory + '/' + sorted_data_dates[x+1] + '_splunk_raw.csv', open_blacklist_and_list_IPs(
            blacklist_directory + '/' + date + '_blacklist.csv'
        ))
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


loop_through_all_blacklists_and_datasets_and_generate_stats(directory_where_the_blacklist_files_can_be_found, directory_where_the_data_files_can_be_found, averages_file, percentages_file)
