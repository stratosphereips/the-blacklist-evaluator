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

data_list = [date, averages, len(ips)]

write_list_to_file(data_list, percentage_file)



