#!/bin/bash
# Input location of results
echo ............................
echo Directory where you want results, no slash at end:
read output_folder_directory
echo ............................

# Check to see if the directory is real.
while [ ! -d $output_folder_directory ]
do
   echo Not a real directory, please input a real one:
   read output_folder_directory
   echo ............................
done

# Input a name that you want for these results
echo Pick a name that does not already exist for your results folder:
read name_of_results_folder
echo ............................

# Check to see if directory already exists.
while [ -d $output_folder_directory/$name_of_results_folder ]
do
   echo Directory alreay exists, please name it something else:
   read name_of_results_folder
   echo ............................
done

# Input location of the blacklists to be evaluated
echo Folder where the Blacklists are:
read blacklist_folder
echo ............................

# Check to see if the directory is real.
while [ ! -d $blacklist_folder ]
do
   echo Not a real directory, please input a real one:
   read blacklist_folder
   echo ............................
done

# Input the location of the traffic files that will be used for eval
echo Path to location folder for Vero Data:
echo Note: In order to evaluate all blacklists generated from input data, eval
echo data should contain one more days data file that input data:
read eval_data_folder

# Check to see if the directory is real.
while [ ! -d $eval_data_folder ]
do
   echo Not a real directory, please input a real one:
   read eval_data_folder
   echo ............................
done

output_folder=$output_folder_directory/$name_of_results_folder
mkdir $output_folder/
touch $output_folder/all_percentages.csv

for folder in $eval_data_folder/*
do
  folder_name=$(basename $folder)
  mkdir $output_folder/$folder_name
  current_location_output=$output_folder/$folder_name/all_percentages.csv
  for file in $blacklist_folder/*
  do
    pat='[0-9][0-9][0-9][0-9][-][0-9][0-9][-][0-9][0-9]'
    [[ $file =~ $pat ]]
    date="${BASH_REMATCH[0]}"
    tomorrow_unix=$(( $(date -d $date "+%s") + 86400 ))
    tomorrow=$(date -d @$tomorrow_unix +'%Y-%m-%d')
    eval_file=$folder/$tomorrow"_splunk_raw.csv"
    export file
    export eval_file
    export current_location_output
    export date
    python3 main.py
  done
done

