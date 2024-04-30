#it is the location on secondarystorage device that is used to store permanently
#1) open file
#2) read/write
#3) close
# to open file :- syntax = open(file,mode)  w = write,r = read,a = append,r+ = read and write,w+ = same as r+ only it can make file if file 
#                          is not existed there ,a+ = read and append
#append:- it is used cuz from w it will over write everytime but append will fix that 
f=open('open.txt','w')
f.write('bahubali ')
f.close()
f=open('open.txt','a')
f.write(input('write here:-'))
f.write(' ')
f.close()