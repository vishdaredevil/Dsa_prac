#Given a binary array arr[] consisting of only 0s and 1s, find the length of the longest contiguous sequence of either 1s or 0s in the array
# 0 1 0 1 1 1 1 
def fun(arr):
    cur_count=1
    maxcount=0
    for i in range(1,len(arr)):
        if (arr[i]==arr[i-1]):
            
            cur_count+=1
        else:
            maxcount=max(cur_count,maxcount)
            cur_count=1
    maxcount=max(cur_count,maxcount)
    return maxcount
lstarr=list(map(int,input().split()))
ans=fun(lstarr)
print (ans)


