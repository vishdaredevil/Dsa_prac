#Three Great Candidates(Maximum product of a triplet (subsequence of size 3) in array)
def fun(arr):
    if len(arr) < 3:
        return 0
    else:
        arr.sort(reverse=True)
        return (arr[0]*arr[1]*arr[2])
arrlst=list(map(int,input().split()))
ans=fun(arrlst)
print(ans)
