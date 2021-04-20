
file='/home/the-shadow/Thesis/2021-03-01-abuse_ch-ip-blocklist.csv'
eval_file='/home/the-shadow/Thesis/2021-03-02_splunk_raw.csv'
output_percentages='/home/the-shadow/Thesis/averages.csv'
date='2021-03-02'

export file
export eval_file
export output_percentages
export date
python3 main.py