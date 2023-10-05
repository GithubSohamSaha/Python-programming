#a is a list contaning some arbitary +ve and -ve numbers
a=[0,12,0,-10,20,-30,40,-50]
#initialization of the counters
positive=0
negative=0
zero=0
for i in a:
    if (i > 0):
        positive+=1
    elif (i < 0):
        negative+=1
    else:
        zero+=1
   
print("In the list,number of positive number is {0}, number of negative number is {1} and the number of zero is {2}".format(positive,negative,zero))