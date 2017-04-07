def missing_Number(myList):
    full_List = set(range(myList[0],myList[-1] + 1))
    return full_List - set(myList)

def main():
    myList = [10, 11, 13, 14, 15, 16, 17, 18, 20]
    print (missing_Number(myList))

if __name__ == "__main__":
    main()
