def TimeToEquality(array):
    max_val=float('-inf')
    time_to_equal=0
    for iterator in range(len(array)):
        if max_val<iterator:
            max_val=iterator
            
    for iterator in range(len(array)):
        time_to_equal+=max_val-iterator
    return time_to_equal
array=list(map(int,input().split()))
print(TimeToEquality(array))    
        