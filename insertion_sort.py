def insertion_sort(list_a):
    ''' this function sorts a list using insertion algorithm _ complexity: n*log(n)'''
    indexing_length=range(1,len(list_a))
    for i in indexing_length:
        value_to_sort=list_a[i]
        while list_a[i-1]>value_to_sort and i>0:
            list_a[i], list_a[i-1]=list_a[i-1],list_a[i]
            i-=1
    return list_a

print(insertion_sort([1,5,3,4,5,6,7,8,90,3,0,1,-1]))


