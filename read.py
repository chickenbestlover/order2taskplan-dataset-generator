import re
file_toRead = open('../data/order-environment-taskplan1.txt.bak','r')

file_toWrite = open('../data/taskplan1.txt','w')
lines_filtered=[]
while True:
    line=file_toRead.readline()
    if not line: break
    line_splited= re.split('\t',line)
    lines_filtered.append(line_splited[0])

file_toWrite.write('[\n')
for line in lines_filtered:
    file_toWrite.write('"'+line+'",\n')
file_toWrite.write(']\n')
file_toRead.close()
file_toWrite.close()