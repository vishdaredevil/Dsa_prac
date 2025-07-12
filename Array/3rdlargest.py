#THIRD LARGEST ELEMENT IN AN ARRAY
def fun(arr):
    if len(arr)<3:
        return None
    arr.sort(reverse=True)
    return (arr[2])
arrlst=list(map(int,input().split()))
ans=fun(arrlst)
print (ans)