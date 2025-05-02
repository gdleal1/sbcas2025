# Generate a csv file with the output file created in calculate_complex.R script

import csv

txt_path = 'outputs/outputs_complex/output-white.txt'

# Read the text file
with open(txt_path, 'r') as file:
    lines = file.readlines()

complex_names = lines[6::2]
complex_values = lines[7::2]

list_names = []
list_values = []

# Create a list with the names of the complexity measures
for line_name in complex_names:
    names = line_name.split()
    for name in names:
        list_names.append(name)

# Create a list with the values of the complexity measures
for line_value in complex_values:
    values = line_value.split()
    list_aux =[]
    for value in values:
        if value == 'NA':
            value = 0
        float_value = float(value)
        list_aux.append(float_value)
    list_values.extend(list_aux)

complexity_measures = []

for i in range(len(list_names)):
    
    if '.sd' in list_names[i]:
        continue
    
    name_parts = list_names[i].split('.')
    complexity_measures.append((name_parts[1], list_values[i]))


csv_path = 'outputs/outputs_complex/output-white.csv'

with open(csv_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Complexity Measure', 'Value'])
    csvwriter.writerows(complexity_measures)



    

        