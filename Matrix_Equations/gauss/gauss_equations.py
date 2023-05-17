import numpy as np


def gauss_elimination(A: np.matrix):
    n = A.shape[0]
    p = -1
    for i in range(0, n - 1):
        for p in range(i, n + 1):
            if p == n:
                print("no unique solution exists")
                return
            if A[p, i] != 0:
                break
        if p != i:
            A[[p, i]] = A[[i, p]]
        for j in range(i + 1, n):
            A[j] = A[j] - (A[j, i] / A[i, i]) * A[i]
    print("Kết thúc quá trình đưa ma trận về dạng bậc thang: ")
    print("Ma trận [A|b] sau biến đổi: \n", A)
    if A[n - 1, n - 1] == 0:
        print("no unique solution exists")
        return
    x = np.zeros(n)
    x[n - 1] = A[n - 1, n] / A[n - 1, n - 1]
    for i in range(n - 1, -1, -1):
        sig = 0
        for j in range(i + 1, n):
            sig += A[i, j] * x[j]
        x[i] = (A[i, n] - sig) / A[i, i]
    return x


if __name__ == "__main__":
    #input matrix [A|b]
    path = "D:\\TLHT\\GTS-PPS\\codepython\\Tucode\\GTS\\Numerical-Analysis-Code\\Matrix_Equations\\gauss\\matrix.txt"
    with open(path, "r") as file:
        # Read the matrix from the file, assuming that the values are space-separated
        A = np.loadtxt(file)
    print("Ma trận [A|b] ban đầu: \n", A)
    x = gauss_elimination(A)
    print("---------------------------")
    print("Nghiệm của hệ: x = ", x)
    print("---------------------------")
    #print("Kiểm tra nghiệm A*x = ", A[:, :-1]@x.T)


