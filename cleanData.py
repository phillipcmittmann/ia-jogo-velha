import pandas as pd
import csv

##################################################################################################

def replace_chars_in_csv(input_file, output_file):
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile, \
         open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            modified_row = []
            for cell in row:
                # Check if the cell contains the word "positive"
                if "positive" in cell:
                    modified_row.append(cell)  # Keep the original cell
                else:
                    # Replace 'x' with '1' and 'o' with '0'
                    modified_row.append(cell.replace('x', '1').replace('o', '0').replace('b', '2'))
            writer.writerow(modified_row)

input_csv = './tic-tac-toe.data'  # Change this to your input file name
output_csv = './tic-tac-toe-no-classes.data'  # Change this to your desired output file name
    
replace_chars_in_csv(input_csv, output_csv)

##################################################################################################
