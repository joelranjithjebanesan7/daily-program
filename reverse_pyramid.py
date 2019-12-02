def reverse_pyramid(n):
    for i in range(1,n):
        myList = []
        for j in range(1,i+2):
            m = 2*n
            space = " "*(m-1)
            rev_py = (space + "* ") * j
            m = m-2
            myList.append(rev_py)
    print ("\n".join(myList))

reverse_pyramid(5)
