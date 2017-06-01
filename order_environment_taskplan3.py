import glob
import random
files_toRead = glob.glob('./taskplan3/*.txt')

file_toWrite = open('../data/order-environment-taskplan3.txt', 'w')
pairs = []
for file in files_toRead:
    file_toRead = open(file,'r')
    for line in file_toRead:
        if 'sprinklerwatering' in line:
            print line
            line = line.replace('sprinklerwatering', 'sprinkler watering')
        if 'snall' in line:
            print line
            line = line.replace('snall', 'small')

        #file_toWrite.write(line)
        pairs.append(line)
    file_toRead.close()

pairs_sampled = random.sample(pairs,10000)

for pair in pairs_sampled:
    file_toWrite.writelines(pair)
    pass
file_toWrite.close()

