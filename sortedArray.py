
def sort_ones_Array(a,size):
    count = 0
    count1 = 0
    count2 = 0

    for i in range(N):
        if a[i] == 0:
            count = count + 1
        elif a[i] == 1:
            count1 = count1 + 1
        else:
            count2 = count2 + 1
    for i in range(0,count):
        a[i] = 0
    for i in range(count,count1+count):
        a[i] = 1
    for i in range(count1+count,N):
        a[i] = 2

    for i in range(N):
        print(a[i], end=" ")


N = 5
arr = [0,2, 1, 2 ,0]
sort_ones_Array(arr,N)
