#I have not given or received any unauthorized assistance on this assignment.
#RanranShi
#01/31/2019

# list out all of the alphabets
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# read namesboys file into a list of strings
with open("namesBoys.txt") as f:
    boys = f.readlines()
boys = [i.strip() for i in boys]

# read namesgirls file into a list of strings
with open("namesGirls.txt") as f:
    girls = f.readlines()
girls = [i.strip() for i in girls]

# initialize the count array to 26 0s
countBoys = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for boy in boys:
    # check which alphabet the string ends with
    for i in range(0, 26):
        if(boy.endswith(alphabets[i])):
            # increment the corresponding count
            countBoys[i] += 1

# initialize the count array to 26 0s
countGirls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for girl in girls:
    # check which alphabet the string ends with
    for i in range(0, 26):
        if(girl.endswith(alphabets[i])):
            # increment the corresponding count
            countGirls[i] += 1

print("Letter\tBoys\tGirls\n")
# print out the result for each alphabet
for i in range(0, 26):
    print(alphabets[i] + '\t' + str(countBoys[i]) + '\t' + str(countGirls[i]) + '\n')

#comment: 
#the most popluar names for girls is A has 380 names, and most popular for boys is 340 with end N.
