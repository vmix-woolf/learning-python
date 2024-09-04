A = range(10)
B = [0]*10
tmp = []
N = int(input('Input the elements\' quantity of array on how many it should be shifted left'))

for k in range(len(A)):
    tmp.append(A[k])
    B[k] = A[k+1]


print(B)