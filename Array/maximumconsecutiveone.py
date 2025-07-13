#Given a binary array arr[] consisting of only 0s and 1s, find the length of the longest contiguous sequence of either 1s or 0s in the array
def findMaxConsecutiveOnes(arr):
    max_count = 0
    current_count = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 1
            
    max_count = max(max_count, current_count)
    
    return max_count
arrlst = list(map(int, input().split()))
ans = findMaxConsecutiveOnes(arrlst)    
print(ans)