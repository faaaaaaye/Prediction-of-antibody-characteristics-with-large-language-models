import csv
import random

# parameters
n = 25  # the number of lines extracted from heavy and light files
x = 10  # the number of rows to extract from heavy with different IDs
y = 10  # the number of rows to extract IDs from light


# Read CSV file
def read_csv(filename):
    with open(filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  
        data = [row for row in reader]
    return header, data

# Write to CSV file
def write_csv(filename, rows, delimiter='\t'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=delimiter)
        for row in rows:
            writer.writerow(row)

# read data
heavy_header, heavy_data = read_csv('heavy.csv')
light_header, light_data = read_csv('light.csv')

# Randomly extract n lines of data
heavy_sample = random.sample(heavy_data, n)
light_sample = random.sample(light_data, n)

# Change the name of the first column to ID.
heavy_sample = [['ID'] + heavy_header[1:]] + heavy_sample
light_sample = [['ID'] + light_header[1:]] + light_sample

# Collect extracted IDs
heavy_list = [row[0] for row in heavy_sample[1:]]
light_list = [row[0] for row in light_sample[1:]]

# Extract the second column of heavy_sample
heavy_rows = []
for row in heavy_sample[1:]: 
    heavy_rows.append([row[1]])  

# Write to heavy.txt
write_csv('heavy.txt', heavy_rows)

# Extract the second and third columns of light_sample
light_rows = []
for row in light_sample[1:]:  
    light_rows.append([row[1]])  

# Write to light.txt
write_csv('light.txt', light_rows)

# Ensure that IDs are different, extract x rows of data from heavy
remaining_heavy = [row for row in heavy_data if row[0] not in heavy_list]
heavy_unique_sample = random.sample(remaining_heavy, x)

# Ensure that the IDs are different, and extract the y row data from light.
remaining_light = [row for row in light_data if row[0] not in light_list]
light_unique_sample = random.sample(remaining_light, y)

# Write the data extracted in Task 2 to answer.txt
answer_rows = []
for row in heavy_unique_sample:
    answer_rows.append(row)
for row in light_unique_sample:
    answer_rows.append(row)
write_csv('answer.txt', answer_rows)

# Write the second column of answer.txt to user.txt
user_rows = []
for row in heavy_unique_sample:
    user_rows.append([row[1]])
for row in light_unique_sample:
    user_rows.append([row[1]])
write_csv('user.txt', user_rows)

print("Task completed. Data has been written to the appropriate file.")
