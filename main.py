import os
import re
from eval_module2 import *
from eval_module3 import *

blacklist = os.environ['file']
print(blacklist)

eval_file = os.environ['eval_file']
print(eval_file)

percentage_file = os.environ['output_percentages']

date = os.environ['date']
print(date)

with open(blacklist, 'r') as blacklist_file:
    data = blacklist_file.readlines()

content = [x.strip() for x in data]

ips = []
for line in content:
    ip = re.search(r"[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+", line)
    if ip is None:
        continue
    else:
        ips.append(ip.group())

averages = extract_stats_from_raw_data_file(eval_file, ips)
data_list = []
data_list.append(date)
data_list.extend(averages)
data_list.append(len(ips))
print(data_list)

header = ["date", "percent_bytes_stopped", "percent_packets_stopped", "percent_duration_stopped", "percent_events_stopped", "percent_of_IPs_stopped", "number_of_ips_in_BL"]
dictionary = {}
for x, entry in enumerate(data_list):
    dictionary[header[x]] = entry

write_dict_to_file(dictionary, percentage_file)



