###################### This module will compare a blacklist to the next days data and generate stats ############################

import csv

def open_blacklist_and_list_IPs(a_blacklist_csv_file):
    list_of_IPs = []
    with open(a_blacklist_csv_file, 'r') as csvfile:
        for line in csv.reader(csvfile):
            list_of_IPs.extend(line)
    return list_of_IPs


def extract_stats_from_raw_data_file(path_to_data_file, list_of_blocked_IPs):
    # Data gathered for the attacks
    total_bytes_all = 0
    total_packets_all = 0
    total_duration_all = 0
    number_of_IPs_total = 0
    total_events = 0

    # Data gathered for the attacks that were blocked by the blacklist
    total_bytes_blocked = 0
    total_packets_blocked = 0
    total_durations_blocked = 0
    total_events_blocked = 0
    number_of_IPs_blocked = 0

    with open(path_to_data_file, "r") as the_file:
        for line in csv.reader(the_file):
            if (line[0] != 'SrcAddr') and (line[0] in list_of_blocked_IPs):
                total_durations_blocked += float(line[2])
                total_bytes_blocked += float(line[4])
                total_packets_blocked += float(line[6])
                total_events_blocked += float(line[1])
                number_of_IPs_blocked += 1

            if line[0] != 'SrcAddr':
                total_duration_all += float(line[2])
                total_bytes_all += float(line[4])
                total_packets_all += float(line[6])
                total_events += float(line[1])
                number_of_IPs_total += 1

    # Compute the stats
    percent_bytes_stopped = (total_bytes_blocked/total_bytes_all)*100
    percent_packets_stopped = (total_packets_blocked/total_packets_all)*100
    percent_events_stopped = (total_events_blocked/total_events)*100
    percent_duration_stopped = (total_durations_blocked/total_duration_all)*100
    percent_of_IPs_stopped = (number_of_IPs_blocked/number_of_IPs_total)*100

    return [percent_bytes_stopped, percent_packets_stopped, percent_duration_stopped, percent_events_stopped, percent_of_IPs_stopped]

#print(extract_stats_from_raw_data_file('/home/thomas/Tresors/Data/AIP-Testing/Raw_Splunk/December-January2019/2020-01-28_splunk_raw.csv', open_blacklist_and_list_IPs('/home/thomas/Tresors/Data/AIP-Testing/Blacklist_examples/December-January2019/New-Each-Day/2020-01-27_blacklist.csv')))
