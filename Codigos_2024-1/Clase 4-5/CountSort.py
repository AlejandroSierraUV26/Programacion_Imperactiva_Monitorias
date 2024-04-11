# A = [2,8,1,4,8,2,1,3,7,4]
# CountSort



def CountSort(A):
    n = len(A)
    m = max(A)
    count = [0] * (m + 1)
    for i in range(n):
        count[A[i]] += 1
        print(count)
    i = 0
    print("--------------------Nu-huh")
    for a in range(m + 1):
        for c in range(count[a]):
            A[i] = a
            print(A)
            i += 1
    return A

A = [2,8,1,4,8,2,1,3,7,4]
print(CountSort(A))
