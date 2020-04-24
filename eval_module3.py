# Module for reading and writing dictionaries to csv files

import csv
import ast


def write_dictionary_to_csv(dictionary, location_of_csv):
    with open(location_of_csv, 'w') as file:
        csvfile = csv.writer(file)
        for key, val in dictionary.items():
            csvfile.writerow([key, val])


def read_csv_to_dictionary(location_of_csv):
    with open(location_of_csv, 'r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]: ast.literal_eval(rows[1]) for rows in reader}
        return mydict


def write_list_to_file(list, location_of_csv):
    with open(location_of_csv, 'w') as file:
        csvfile = csv.writer(file)
        for entry in list:
            csvfile.writerow(entry)





