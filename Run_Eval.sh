#!/bin/bash
# Input location of results
echo ............................
echo Directory where you want results, no slash at end:
read output_folder_directory
echo ............................

# Input location of results
echo ............................
echo Input the file ending for current blacklist:
read blacklist_ending
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
echo Path to input data folder:
read input_data_folder
echo ............................

# Check to see if the directory is real.
while [ ! -d $input_data_folder ]
do
   echo Not a real directory, please input a real one:
   read input_data_folder
   echo ............................
done

# Input the location of the traffic files that will be used for eval
echo Path to evaluation data:
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
touch $output_folder/averages.csv
touch $output_folder/all_percentages.csv

output_averages=$output_folder/averages.csv
output_percentages=$output_folder/all_percentages.csv

export output_averages
export output_percentages
export input_data_folder
export eval_data_folder
export blacklist_ending

python3 Eval-Main.py
