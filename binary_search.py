from typing import Sequence
import time

def binary_search(sequence, item):
    ''' This function return the index of item in the sequence 
    sequence has to be sorted '''
    begin_index=0
    end_index=len(sequence)-1

    while begin_index<=end_index:
        midpoint=begin_index +(end_index-begin_index)//2
        midpoint_value=sequence[midpoint]
        if midpoint_value== item:
            return midpoint

        elif item<midpoint_value:
            end_index=midpoint-1
        else:
            begin_index=midpoint+1
    return None 


Sequence_a=[1,2,3,4,5,6,7,8]
item= 2
print(binary_search(Sequence_a, item))

print('Today is :', time.time() )