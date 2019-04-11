#Ranran Shi
#DSC430
#Question1
#“I have not given or received any unauthorized assistance on this assignment.”

import statistics
import csv
import math

def read_data(var):
    data_index = 0
    data = []
    with open('avocado.csv', 'r') as csvfile:
        avocado = csv.reader(csvfile, delimiter=',')
        avocado = list(avocado)

    for i in range(len(avocado[0])):
        if avocado[0][i] == var:
            data_index = i
    
    for j in range(1, len(avocado)):
        data.append(float(avocado[j][data_index]))
    return data

def read_and_compute_mean_sm(var):
    data = read_data(var)
    return statistics.mean(data)

def read_and_compute_sd_sm(var):
    data = read_data(var)
    return statistics.stdev(data)

def read_and_compute_median_sm(var):
    data = read_data(var)
    return statistics.median(data)

def read_and_compute_mean_hg(var):
    data = read_data(var)
    size = len(data)
    sum = 0
    for d in data:
        sum += d
    return sum/size

def read_and_compute_sd_hg(var):
    data = read_data(var)
    mean = read_and_compute_mean_hg(var)
    variance = 0
    for d in data:
        variance += (d - mean)**2
    variance = variance / (len(data)-1)
    return math.sqrt(variance)

def read_and_compute_median_hg(var):
    data = read_data(var)
    data = sorted(data)
    size = len(data)
    if size % 2 == 0:
        median = (data[int(size/2)] + data[int(size/2) - 1])/2
    else:
        median = data[int(size/2)]
    return median

def read_and_compute_mean_mml(var):
    sum = 0
    count = 0
    with open('avocado.csv', 'r') as csvfile:
        avocado = csv.DictReader(csvfile, delimiter=',')
        for line in avocado:
            sum += float(line[var])
            count += 1
        return sum/count

def read_and_compute_sd_mml(var):
    sum = 0
    count = 0
    avg = 0
    with open('avocado.csv', 'r') as csvfile:
        avocado = csv.DictReader(csvfile, delimiter=',')
        for line in avocado:
            sum += float(line[var])
            count += 1
        avg = sum/count

    variance = 0
    with open('avocado.csv', 'r') as csvfile:
        avocado = csv.DictReader(csvfile, delimiter=',')
        for line in avocado:
            variance += (float(line[var]) - avg)**2
        variance = variance / (count-1)
        return math.sqrt(variance)

def countSmaller(var, n):
    count = 0
    with open('avocado.csv', 'r') as csvfile:
        avocado = csv.DictReader(csvfile, delimiter=',')
        for line in avocado:                # for each value n from a line of data
            if float(line[var]) < n:        # add to count if value smaller than n
                count += 1
        return count

def countLarger(var, n):
    count = 0
    with open('avocado.csv', 'r') as csvfile:
        avocado = csv.DictReader(csvfile, delimiter=',')
        for line in avocado:                # for each value n from a line of data
            if float(line[var]) > n:        # add to count if value greater than n
                count += 1
        return count

def read_and_compute_median_mml(var):
    n = 0
    largerVal = 0
    smallerVal = 0
    median = 0
    with open('avocado.csv', 'r') as csvfile:
        avocado = csv.DictReader(csvfile, delimiter=',')
        for line in avocado:
            n = float(line[var])            # for each value n from a line of data
            larger = countLarger(var, n)    # count how many values are larger than n
            smaller = countSmaller(var, n)  # count how many values are smaller than n
            diff = larger - smaller         # calculate difference between larger and smaller value
            if diff == 0:                   # if they are the same, this number is the median
                median = n                  # return the median
                return median
            elif diff == 1:                 # this can happen if there are even number of data
                smallerVal = n
            elif diff == -1:
                largerVal = n
        median = (largerVal + smallerVal)/2 # in this case median is the average of the middle two numbers
        return median
        
    

print(read_and_compute_mean_sm("Total Volume"))
print(read_and_compute_mean_hg("Total Volume"))
print(read_and_compute_mean_mml("Total Volume"))
print(read_and_compute_sd_hg("Total Bags"))
print(read_and_compute_sd_sm("Total Bags"))
print(read_and_compute_sd_mml("Total Bags"))
print(read_and_compute_median_sm("Total Bags"))
print(read_and_compute_median_hg("Total Bags"))
print(read_and_compute_median_mml("Total Bags"))    # this takes O(n^2) time to complete

