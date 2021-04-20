# Module for reading and writing dictionaries to csv files

import csv
import os


def write_dict_to_file(dictionary, location_of_csv):
    if os.stat(location_of_csv).st_size == 0:
        with open(location_of_csv, 'a') as file:
            header = ["date", "percent_bytes_stopped", "percent_packets_stopped", "percent_duration_stopped",
                      "percent_events_stopped", "percent_of_IPs_stopped", "number_of_ips_in_BL"]
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerow(dictionary)
    else:
        with open(location_of_csv, 'a') as file:
            header = ["date", "percent_bytes_stopped", "percent_packets_stopped", "percent_duration_stopped",
                      "percent_events_stopped", "percent_of_IPs_stopped", "number_of_ips_in_BL"]
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writerow(dictionary)





