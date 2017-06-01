import re
file_toRead = open('./taskplan3/1.txt','r')

file_toWrite = open('./taskplan3/0.txt','w')
lines_filtered=[]
while True:
    line=file_toRead.readline()
    if not line: break
    line_splited= re.split(' `',line)
    lines_filtered.append(line_splited[0])
for line in lines_filtered:
    file_toWrite.writelines(line)

file_toRead.close()
file_toWrite.close()