#!/bin/bash
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
