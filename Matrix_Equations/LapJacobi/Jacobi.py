import numpy as np

def Cheotroihang(A, b):
    for i in range(A.shape[0]):
        max = abs(A[i, i])
        for j in range(A.shape[0]):
            if i == j:
                continue
            max -= abs(A[i, j])
        if max <= 0:
            return False
        
    return True

def Cheotroicot(A, b):
    for i in range(A.shape[0]):
        max = abs(A[i, i])
        for j in range(A.shape[0]):
            if i == j:
                continue
            max -= abs(A[j, i])
        if max <= 0:
            return False
        
    return True



def Jacobi_method(A, b, eps):
   
    if Cheotroihang(A, b):
        print("Ma trận thỏa mãn chéo trội hàng")
        for i in range(A.shape[0]):
            b[i] = b[i]/A[i, i]
            A[i, :] = A[i,:]/A[i, i]
        
        alpha = np.eye(A.shape[0]) - A
        q = np.linalg.norm(alpha.T, 1)
        print("q = ", q)
        print("alpha = " ,alpha)
        print("beta = ", b)
        print("\n\n")
        x0 = np.zeros(len(b))
        x = x0
        k = 0
        while(True):
            x = alpha@x.T + b
            print("Lần lặp thứ {0}: \n {1}".format(k+1, x))
            saiso = q*np.linalg.norm(x-x0, ord=1)/(1-q)
            if saiso < eps:
                print("Sai số: ", saiso)
                return x
            x0 = x 
            k = k+1
    elif Cheotroicot(A, b):
        print("Ma trận thỏa mãn chéo trội cột")
        T = np.zeros(A.shape)
        max_a = abs(A[0, 0])
        min_a = abs(A[0, 0])
        for i in range(A.shape[0]):
            T[i, i] = 1/A[i, i]
            if max_a < abs(A[i, i]):
                max_a = abs(A[i, i])
            if min_a > abs(A[i, i]):
                min_a = abs(A[i, i])
        Lambda = max_a/min_a
        alpha = np.eye(A.shape[0]) - T@A
        beta = T@b
        q = np.linalg.norm(alpha, 1)
        print("q = ", q)
        print("alpha = " ,alpha)
        print("beta = ", beta)
        print("\n\n")
        x0 = np.ones(len(b))
        x = x0
        k= 0
        while(True):
            x = alpha@x.T + beta
            print("Lần lặp thứ {0}: \n {1}".format(k+1, x))
            saiso = Lambda*q*np.linalg.norm(x-x0, ord=1)/(1-q)
            if saiso < eps:
                print("Sai số: ", saiso)
                return x
            print(x)
            x0 = x 
            k = k + 1
    
    else:
        print("Ma trận không thỏa mãn chéo trội")
        


if __name__ == "__main__":
#input matrix [A|b]
    path = "D:\\TLHT\\GTS-PPS\\codepython\\Tucode\\GTS\\Numerical-Analysis-Code\\Matrix_Equations\\LapJacobi\\matrix.txt"
    with open(path, "r") as file:
        # Read the matrix from the file, assuming that the values are space-separated
        matrix = np.loadtxt(file)

    A = matrix[:, :-1]
    A_b = np.array(matrix)
    b = matrix[:, -1]
    eps = 1e-10   #Sai số
    sochuso = 10  #Số chữ số sau dấu phẩy
    Sol = Jacobi_method(A, b, eps)
    print("Nghiệm gần đúng: ", Sol)
    print("Kiểm tra kết quả: Ax = ", A_b[:, :-1]@Sol)

