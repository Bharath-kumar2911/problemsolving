

def rotate(ar,d,N):

    p = 1
    while(p<=d):
        last = ar[0]
        for i in range(N-1):
            ar[i] = ar[i+1]

        ar[N-1] = last
        p = p+1
def printArray(ar,size):
    for i in range(size):
        print(ar[i],end = " ")







arr = [1,2,3,6,7,8,9]
N = len(arr)
d = 2


rotate(arr,d,N)
printArray(arr, N)



