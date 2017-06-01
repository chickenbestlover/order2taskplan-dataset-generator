import re
file_toRead = open("./VEIL500/Data/data.xml", 'r')
file_toWrite = open("../data/orders-taskplan.txt", 'w')
while True:
    line = file_toRead.readline()
    if not line: break
    #print line
    line = line.replace('<root>', '')
    line = line.replace('</root>', '')
    line = line.replace('<point>', '')
    line = line.replace('</point>', '')
    line = line.replace('|', '')
    line = line.replace('  ', ' ')
    line = line.replace('  ', ' ')
    line = line.replace('  ', ' ')
    line = line.replace('. .', '.')
    line = line.replace('.', '. ')
    line = line.replace('.  ', '. ')
    line = line.replace('\n', '')
    if '<text>' in line:
        line = line.replace('<text>', '')

        if 'energydrink' in line:
            print line
            line = line.replace('energydrink', 'energy drink')


        if '</text>' in line:
            line = line.replace('</text>', '')
            line_splited = re.split(' ',line)
            while line_splited[-1]==' ' or line_splited[-1]=='':
                del line_splited[-1]
            print line_splited
            file_toWrite.write(
                ' '.join(line_splited)+'\t')
            continue
        else:
            line_splited = re.split(' ',line)
            while line_splited[-1]==' ' or line_splited[-1]=='':
                del line_splited[-1]
            print line_splited
            file_toWrite.write(
                ' '.join(line_splited))
            continue
    if not '<text>' in line:
        if '</text>' in line:

            line = line.replace('</text>', '')
            line_splited = re.split(' ', line)
            if len(line_splited):
                print line_splited
                while line_splited[-1]==' ' or line_splited[-1]=='':
                    del line_splited[-1]
            print line_splited
            file_toWrite.write(
                ' '.join(line_splited) + '\t')
            continue

    if '<environment>' in line:
        line = line.replace('<environment>', '')
        line = line.replace('</environment>', '')
        line_splited = re.split(' ',line)
        #file_toWrite.write(' '.join(line_splited)+ '\t')
        continue
    if '<action>' in line:
        line = line.replace('<action>', '')
        line = line.replace('</action>', '')
        line = line.replace('\n', '')
        line_splited = re.split(' ',line)
        file_toWrite.write(
            ' '.join(line_splited)
            + ' ')
        continue
    if '<change_of_alignment/>' in line:
        line = line.replace('<change_of_alignment/>', '')
        continue
    if '</action_sequence>' in line:
        line = line.replace('</action_sequence/>', '')
        file_toWrite.write('\n')
        continue

file_toRead.close()
file_toWrite.close()