def binary_Search(mylist,item):
    if len(mylist) == 0:
        return False
    else:
        midpoint = len(mylist)//2
        if mylist[midpoint]== item:
            return True
        else:
            if item < mylist[midpoint]:
                return binary_Search(mylist[:midpoint],item)
	    else:
                return binary_Search(mylist[midpoint+1:],item)
                
                 
mylist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_Search(mylist, 3))
print(binary_Search(mylist, 13))
