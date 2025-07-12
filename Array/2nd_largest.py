#SECOND LARGEST ELEMENT IN AN ARRAY
def fun(arr):
    if len(arr)<2:
        return None
    arr.sort(reverse=True)
    return (arr[1])
arrlst=list(map(int,input().split()))
ans=fun(arrlst)
print (ans)