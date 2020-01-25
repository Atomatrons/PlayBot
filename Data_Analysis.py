#!/usr/bin/env micropython

# List of spin turn error values
data = []

# open log file
logfile = open ('log.txt','r')
 
 # read file into 
for line in logfile:
    data.append(int(line))
print(data)

# compute some statistics
total_error = 0
max_value = -1
min_value = 1000
for item in data:
    total_error += item
    if item > max_value:
        max_value = item
    if item < min_value:
        min_value = item

print('total is {}'.format (total_error))
# number of data values
data_values = len(data)

# prints out statsistics
print ('number of samples is {}'.format(data_values))
print ('minimum value is {}'.format (min_value))
print ('maximum value is {}'.format (max_value))

# Computes Average
average = total_error/data_values
print (' average is {} degrees'.format (round(average, 2)))