#import order_environment_taskplan1
#import order_environment_taskplan2
#import order_environment_taskplan3
#import order_environment_taskplan4
#import order_environment_taskplan5
import glob
import random
files_toRead = glob.glob('../data/order-environment-taskplan*.txt')

file_train = open('../data/order-environment-taskplan-train.txt', 'w')
file_test = open('../data/order-environment-taskplan-test.txt','w')
file_whole = open('../data/order-environment-taskplan-whole.txt','w')
pairs = []
for file in files_toRead:
    file_toRead = open(file,'r')
    for line in file_toRead:
        pairs.append(line)
    file_toRead.close()

random.shuffle(pairs)
pairs_train = pairs[:45000]
pairs_test = pairs[45000:]
for pair in pairs:
    file_whole.writelines(pair)
for pair in pairs_train:
    file_train.writelines(pair)
for pair in pairs_test:
    file_test.writelines(pair)

file_whole.close()
file_train.close()
file_test.close()