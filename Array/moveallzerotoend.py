# Given an array of integers arr[], the task is to move all the zeros to the end of the array while maintaining the relative order of all non-zero elements.
# arr=[1,2,0,4,3,0,5,0] 
# output= [1,2,4,3,5,0,0,0]
def fun(arr):
    emp=[]
    zerolst=[]
    count=0
    for i in range(len(arr)):
        if arr[i]==0:
            count=count+1
            zerolst.append(arr[i])
        else:
            emp.append(arr[i])
    emp.extend(zerolst)
    if count==0:
        return arr
    elif len(emp)==0:
        return arr
    else:
        return emp
    
arrlst=list(map(int,input().split()))
ans=fun(arrlst)
print(ans)