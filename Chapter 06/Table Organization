

def printTable(tableData):
    lineNum = len(tableData[0])
    rowNum = len(tableData)
    # Creat a list of max width list. and set default value to 0.
    colWidths = [0] * rowNum

    String_Length_List = []
    for i in range(0, rowNum):
        for j in range(0, lineNum):
            print tableData[i][j]
            String_Length_List.append(len(tableData[i][j]))
        print String_Length_List
        colWidths[i] = max(String_Length_List)  # Ex. set colWidths[0] = 8
        print 'This list max length is '+str(colWidths[i])+', i='+str(i)
        print '..............\n'
        String_Length_List = []  # reset to space. before next turn for loop.
    print 'The final colWidths list is,' + str(colWidths)

    # String_Length_List = [0]*rowNum
    # print String_Length_List
    # n = 0
    # for i,j,k,l in tableData:
    #     print i,j,k,l
    #     colWidths[n] = len(max(i,j,k,l,key=len))
    #     print colWidths[n]
    #     n +=1
    #     print '..............\n'
    # print 'The final colWidths list is,' + str(colWidths)

    list = []
    a = []
    print list
    for i in range(0, lineNum):
        for j in range(0, rowNum):
            data = tableData[j][i]
            print data
            a.append(data)
            print 'a list,#####', a
        list.append(a)
        print '..............\n'
        print list
        a = []
    print list
    print '..............\n'
    
    for m, n, k, in list:
        print   m.rjust(colWidths[0]),\
                n.ljust(colWidths[1]),\
                k.ljust(colWidths[2])

tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose'],
]


printTable(tableData)











