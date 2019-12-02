def pyramidtwo(n):
    myList = []
    for i in range(1,n+1):
        myList.append("*"*i)
    print("\n".join(myList))

pyramidtwo(5)
