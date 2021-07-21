def bubbleSort(list_a):
    ''' this function sorts a list using bubble algorithm'''
    indexing_length=len(list_a)-1
    sorted= False
    while not sorted: 
        sorted= True
        for i in range (0, indexing_length):
            if list_a[i]> list_a[i+1]:
                sorted=False
                list_a[i], list_a[i+1] = list_a[i+1] , list_a[i] 
    return list_a


bubbleSort([7,3,1,6,98,3,6,5,96,9,1,0,-2,-1])