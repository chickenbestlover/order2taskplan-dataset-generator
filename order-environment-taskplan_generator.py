import order_environment_taskplan1
import order_environment_taskplan2
import order_environment_taskplan3
import order_environment_taskplan4
import order_environment_taskplan5
import glob
import random
files_toRead = glob.glob('../data/order-environment-taskplan*.txt')

file_toWrite = open('../data/order-environment-taskplan.txt', 'w')

pairs = []
for file in files_toRead:
    file_toRead = open(file,'r')
    for line in file_toRead:
        pairs.append(line)
    file_toRead.close()

random.shuffle(pairs)
for pair in pairs:
    file_toWrite.writelines(pair)

file_toWrite.close()
