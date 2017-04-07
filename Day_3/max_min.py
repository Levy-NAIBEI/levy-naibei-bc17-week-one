def max_min(mylist):
    mylist.sort()
    minNum = mylist[0]
    maxNum = mylist[-1]

    return ("Maximum is {0} and Minimum is {1}".format(maxNum,minNum))

print(max_min([8,2,5,7]))



