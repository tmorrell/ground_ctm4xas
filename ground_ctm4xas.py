# Extract ground state eigenvalues and put into table
# Takes File Name as Input
# Tom Morrell 2015

import sys

name=sys.argv[1]
infile = open(name,'r')
inline = infile.readline()

top=[]
data=[]

cur=0 #index of curent triad
eigs=0
index=0
maxv=0

while inline[1:46] !=  'CALCULATIONS for ACTOR:HAMILTONIAN     GROUND':
    inline=infile.readline()

#now at correct section
while inline[1:9] != 'H   H  A':
    split=inline.split()
    if len(split) > 0:
        if split[0] == 'CALCULATING':
            #If we have a triad label
            top.append([split[6],split[7],split[8]])
            index = len(top) #current triad
        if split[0]=='EIGVAL':
            if cur == index: 
                data[cur-1]=data[cur-1]+split[1:]
                eigs = eigs + len(split[1:])
                if eigs > maxv:
                    maxv=eigs
            else: #new value
                data.append(split[1:])
                eigs=len(split[1:])
                cur=index
    inline=infile.readline()

outstring=''
for j in top:
    outstring=outstring+str(j)+'\t'
outstring=outstring+'\n'
for i in range(maxv):#for each row
    for j in range(len(data)):
        if len(data[j])<=i:
            outstring = outstring+'\t'
        else:
            outstring=outstring+data[j][i]+'\t'
    outstring = outstring + '\n'

outfile=open(name.split('.')[0]+'.out','w')
outfile.write(outstring)


