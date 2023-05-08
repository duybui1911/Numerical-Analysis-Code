import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.lib import scimath

#Thay đổi khoảng tìm nghiệm:
a = 4.823
b = 8.5
#Thay đổi khoảng vẽ đồ thị tại đây
left = 0
right = 8


num_decimal = 10   #Số chữ số thập phân hiển thị

#Nhập phương trình cần giải
def f(x):
    return 2*x**5 - 12*x**4 + 3*x**2 - 15

def show_fx():
    plt.xlabel("Giá trị x biến thiên")
    plt.ylabel("Giá trị y biến thiên")
    plt.title("Đồ thị hàm số của phương trình f(x) ")
    x = np.linspace(left, right, 1000)
    plt.plot(x, f(x))
    plt.plot(0, 0, '+')
    plt.plot(0, )
    plt.grid()
    plt.show()


def sign_f(x):
    if f(x) < 0:
        return -1
    elif f(x) > 0:
        return  1
    elif f(x) == 0:
        return 0

def checkInput(a, b):
    if sign_f(a)*sign_f(b) > 0:
        print("Giá trị hàm tại hai đầu mút cùng dấu --> Kiểm tra lại đầu vào")
        return 0
    elif sign_f(a) == 0:
        print("Hàm số có nghiệm là đầu mút a = ", a)
        return 0
    elif sign_f(b) == 0:
        print("Hàm số có nghiệm là đầu mút b = ", b)
        return 0
    return 1


def tien_nghiem(a, b):
    n = math.ceil(scimath.log2((b-a)/(eps)))
    print("Số lần lặp: ", n)
    #print("_"*110)
    #print("|{0:^9}|{1:^25}|{2:^30}|{3:^20}|{4:^20}|".format("Lần lặp", "Nghiệm x", "f(x)", "Đầu mút a", "Đầu mút b"))
    #print("-" * 110)
    fout.write("\n" + "_" * 110)
    fout.write("\n|{0:^9}|{1:^25}|{2:^30}|{3:^20}|{4:^20}|".format("Lần lặp", "Nghiệm x", "f(x)", "Đầu mút a", "Đầu mút b"))
    fout.write("\n" + "_" * 110)
    for i in range(n):
        x = (a + b) / 2
        if f(x) == 0:
            #print("|{0:^9}|{1:^25}|{2:^30}|{3:^20}|{4:^20}|".format(i + 1, round(x, num_decimal), round(f(x), num_decimal), round(a, num_decimal), round(b, num_decimal)))
            print("Phương trình đạt nghiệm đúng sau ", n, "lần lặp")
            fout.write("\n|{0:^9}|{1:^25}|{2:^30}|{3:^20}|{4:^20}|".format(i+1, round(x, num_decimal), round(f(x), num_decimal), round(a, num_decimal), round(b, num_decimal)))
            break
        elif f(a) * f(x) < 0:
            b = x
            #print("|{0:^9}|{1:^25}|{2:^30}|{3:^20}|{4:^20}|".format(i + 1, round(x, num_decimal), round(f(x), num_decimal), round(a, num_decimal), round(b, num_decimal)))
            fout.write("\n|{0:^9}|{1:^25}|{2:^30}|{3:^20}|{4:^20}|".format(i + 1, round(x, num_decimal), round(f(x), num_decimal), round(a, num_decimal), round(b, num_decimal)))
        elif f(x) * f(b) < 0:
            a = x
            #print("|{0:^9}|{1:^25}|{2:^30}|{3:^20}|{4:^20}|".format(i + 1, round(x, num_decimal), round(f(x), num_decimal), round(a, num_decimal), round(b, num_decimal)))
            fout.write("\n|{0:^9}|{1:^25}|{2:^30}|{3:^20}|{4:^20}|".format(i + 1, round(x, num_decimal), round(f(x), num_decimal), round(a, num_decimal), round(b, num_decimal)))
    fout.write("\n" + "_" * 110)
    return x


if __name__ == "__main__":
    show_fx()
    x0: float
    print("Nhập khoảng tìm nghiệm: ")
    eps = float(input("Nhập sai số: "))
    print()
    if checkInput(a, b) == 1:
        try:
            fout = open("output_tn.txt", mode='w', encoding='utf-8')
            if not (f(a) * f(b) > 0):
                x0 = tien_nghiem(a, b)
                print("Nghiệm gần đúng của phương trình là: ")
                print(x0)
                fout.write("\nNghiệm gần đúng của phương trình là: " + str(x0))
            else:
                print("Khoảng (", a, ",", b, ") không là khoảng phân ly nghiệm")
        finally:
            fout.close()