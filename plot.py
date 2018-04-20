import numpy as np
import matplotlib.pyplot as plt

datafile = open('test.txt', 'r')
print '\n rading data from test.txt'

#read the first line
columns = datafile.readlines()

#print '\n first column \n', columns
#columns = columns.split(' ')
#print '\n', columns

temp = []
print 'test new line \n'
for i in columns:
    #print '\n', i
    vars = [str(j) for j in i.split('\t')]

    #vars[0] = str(vars[0].replace("''", ""))
    #print  vars[0]
    vars[1] = int(vars[1].rstrip())
    #print type(vars[0])
    temp.append(vars)
print temp
print 'type of temp', type(temp)
Char = []
Num = []
for i in temp:
    Char.append(i[0])
    Num.append(i[1])
print type(Num)
print type(Char)
print Char[23:49]
print Char[48]

plt.bar(range(len(Num[23:49])), Num[23:49], align='center', color='y')
#print range(5)
plt.xticks(range(26),Char[23:49])
plt.xlabel('Character')
plt.ylabel('Number')
#plt.text(range(26),Char[23:49],Num[23:49])
plt.xlim(0,25)
plt.savefig('WordCount.png')
plt.show()
