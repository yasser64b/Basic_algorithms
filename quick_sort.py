def quick_sort(sequence):
    ''' this function sorts a list using in a quickest way'''
    length=len(sequence)
    if length <=1:
        return sequence
    else:
        pivot=sequence.pop()

    items_greater=[]
    items_lower=[]

    for item in sequence:
        if item>pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
        
    return quick_sort(items_lower)+[pivot]+quick_sort(items_greater)

print(quick_sort([1,2,5,63,58,32,5,3,8,25,5,3]))   

