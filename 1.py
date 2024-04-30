#    *
#   ***
#  *****
# *******
for i in range(1,5):
    for j in range(1,8):
        if i==1 and j<4 or i==1 and j>4 or i==2 and j<3 or i==2 and j>5 or i==3 and j<2 or i==3 and j>6 :
            print(' ',end='')
        else:
            print('*',end="")
    print('')
