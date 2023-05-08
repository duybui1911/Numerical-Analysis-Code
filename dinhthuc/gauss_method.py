import numpy as np
import sys

data = np.genfromtxt('A.txt', delimiter=' ')
A = np.array(data)
print("A = ", A)

n = len(A[0])
i = 0
detA = 1
temp = np.zeros((1, n))

while i < n:
    check = -1
    for r in range(i, n):
        if np.abs(A[r, i]) == 1:
            check = 1
            break
    if check == -1:
        Any = np.abs(A[i, i])
        r = i
        for k in range(i+1, n):
            if np.abs(A[k, i]) > Any:
                Any = np.abs(A[k, i])
                r = k
        if Any == 0:
            print("Cột thứ ", i+1, " của ma trận A(", i,") đồng nhất 0")
            print("detA = 0")
            sys.exit()
    if r != i:
        temp[0] = A[i]
        A[i] = A[r]
        A[r] = temp[0]
        detA = -detA
        print()
        print("Đổi chỗ hàng thứ ", i + 1, " với hàng thứ ", r + 1)

    for j in range(i + 1, n):
        if j < n:
            p = A[j, i] / A[i, i]
            A[j] = A[j] - p * A[i]
    print()
    print("Lần lặp thứ: ",i+1)
    print(A)
    i += 1

for i in range(n):
    detA = detA * A[i, i]
print("Định thức của ma trận A là: ", detA)
