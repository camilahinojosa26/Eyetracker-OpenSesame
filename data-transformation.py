import csv
import os
import re
import shutil
import io
import pandas as pd
import os, csv, sys


input_dir = 'exp-results'
output_dir = 'et-and-os-results'
all_results_dir = 'all-results-by-subject'

# create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
if not os.path.exists(all_results_dir):
    os.makedirs(all_results_dir)

# iterate over files in input directory
for filename in os.listdir(input_dir):
    
    if filename.endswith('.tsv'):
        
        input_file = os.path.join(input_dir, filename)
        print(input_file)

        # set output file path for ET CSV file
        output_file_et_csv = os.path.join(output_dir, re.sub(r'(-et)?\.tsv$', r'-et.csv', filename))

        with open(input_file, 'r') as tsvfile, open(output_file_et_csv, 'w', newline='') as et_csvfile:
            tsvreader = csv.reader(tsvfile, delimiter='\t')
            et_csvwriter = csv.writer(et_csvfile, delimiter=',')
            for row in tsvreader:
                et_csvwriter.writerow(row)    

    if filename.endswith('.csv'): 
        input_file = os.path.join(input_dir, filename)
    
        output_file_csv = os.path.join(output_dir, re.sub(r'\.tsv$', r'.csv', filename))

        # copy CSV file to output directory
        shutil.copyfile(os.path.join(input_dir, re.sub(r'\.tsv$', r'.csv', filename)), output_file_csv)
        

              
for filename in os.listdir(output_dir):
    # check if file is an ET CSV file
    if filename.endswith('-et.csv'):
        # extract file prefix before -et.csv
        file_prefix = re.sub(r'-et\.csv$', '', filename)
        os_csv_file = os.path.join(input_dir, file_prefix + '.csv')
        et_csv_file = os.path.join(output_dir, file_prefix + '-et.csv')
        if os.path.exists(os_csv_file):
            all_data_csv_file = os.path.join(output_dir, f'all-data-{file_prefix}.csv')
            with open(os_csv_file, 'r') as os_csvfile, open(et_csv_file, 'r') as et_csvfile:
                os_csv_reader = csv.reader(os_csvfile)
                et_csv_reader = csv.reader(et_csvfile)
                with open(all_data_csv_file, 'w', newline='') as all_data_csvfile:
                    all_data_csv_writer = csv.writer(all_data_csvfile)
                    for os_row, et_row in zip(os_csv_reader, et_csv_reader):
                        output_row = os_row + et_row[1:]
                        all_data_csv_writer.writerow(output_row)
            #print(f'Matching pair: {os_csv_file} and {et_csv_file} merged into {all_data_csv_file}')
            # copy output file to input file
            # shutil.copy2(all_data_csv_file, os_csv_file)
            # print(f'{all_data_csv_file} copied to {os_csv_file}')
            
           
# move all all-data files to all-results-by-subject directory

for filename in os.listdir(output_dir):
    if filename.startswith('all-data'):
        src_path = os.path.join(output_dir, filename)
        dst_path = os.path.join(all_results_dir, filename)
        shutil.move(src_path, dst_path)
