def selection_sort(list_a):
    ''' Sort a list using selection method , complexity is n*log(n)'''
    indexing_length=range(0,len(list_a)-1)
    # loop over all list (N)
    for i in indexing_length:
        min_value=i
        # loop over part of the list (~Log(N))   
        for j in range(i+1, len(list_a)):
            if list_a[j]<list_a[min_value]:
                min_value=j

        #Shift min value to the left
        if min_value !=i: 
            list_a[min_value], list_a[i]= list_a[i],list_a[min_value] # must change simultaniously
            # this can give you wrong answer
            #              list_a[min_value]= list_a[i] 
            #              list_a[i]=list_a[min_value]
    return list_a 



selection_sort([0,-1,9,8,7,4,5,6,3,2,1,-1])