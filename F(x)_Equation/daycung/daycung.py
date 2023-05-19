import numpy as np
import matplotlib.pyplot as plt

#Thay đổi khoảng vẽ đồ thị tại đây
left = -5
right = 5

num_decimal = 15  # Số chữ số thập phân xuất hiện trong output


delta = 1e-6
MAXLOOP = 1e+6  # Số lần lặp tối đa cho đỡ vướng vào cái lặp vô hạn thôi
eta = 1e-2

#Phương trình f(x) = 0
def f(x):
    return np.log(x)-1


def df(x):
    return (f(x + delta) - f(x - delta)) / (2 * delta)

def d2f(x):
    return (df(x + delta) - df(x - delta)) / (2 * delta)

def dnf(x, deg):
    if deg == 1:
        return df(x)
    elif deg == 2:
        return d2f(x)


def show_fx():
    plt.xlabel("y")
    plt.ylabel("x")
    plt.title("y = f(x) ")
    x = np.linspace(left, right, 1000)
    plt.plot(x, f(x))
    plt.plot(0, 0, '+')
    plt.plot(0, )
    plt.grid()
    plt.show()

def menu():
    print("")
    print(" " * 20, "_" * 53)
    print(" " * 20, "|{0:51}|".format(" "))
    print(" " * 20, "|{0:^9}{1:^9}{0:^24}|".format(" ", "1. Sai số mục tiêu"))
    print(" " * 20, "|{0:^9}{1:^9}{0:^11}|".format(" ", "2. Sai số hai lần lặp liên tiếp"))
    print(" " * 20, "|{0:51}|".format(" "))
    print(" " * 20, "-" * 53)
    print("")
    print("")

def gradient_descent(a, b, sign, deg): #sign = 1(cực tiểu)/-1(cực đại)
    x_ct = a
    count = 1
    while (not (abs(dnf(x_ct, deg)) < delta)):
        x_ct = x_ct - sign*eta * dnf(x_ct, deg)
        count += 1
        if count > MAXLOOP:
            break
        elif x_ct > b:
            #print("Hàm đơn điệu trên (", a, " , ", b, ")")
            break
        elif x_ct < a:
            break
    return x_ct

def find_Extreme_of_theFuntion(left, right, deg):
    count = 2
    extreme = [left, right]
    while True:
        temp1 = gradient_descent(left, right, 1, deg)
        temp2 = gradient_descent(left, right, -1, deg)
        if (temp1 > right and temp2 < left) or (temp1 < left and temp2 > right):
            break
        if (temp1 > left) and (temp1 < right):
            extreme.append(temp1)
            left = extreme[count] + 0.05
            count += 1

        if (temp2 > left):
            if (temp2 < right):
                extreme.append(temp2)
                left = extreme[count] + 0.05
                count += 1
    if count > 2 and deg == 1:
        print("Hàm số tồn tại cực trị:",extreme[2:], "trên" , extreme[0], ",", extreme[1], "]")
    return extreme



def check_input(left, right):
    if f(left) * f(right) > 0:
        return False
    if left > right:
        left, right = right, left
    ext = find_Extreme_of_theFuntion(left, right, 1)
    ext2 = find_Extreme_of_theFuntion(left, right, 2)
    if len(ext) == 2 and len(ext2) == 2:
        return True
    elif len(ext) > 2:
        print("f'(x) đổi dấu tại ít nhất 1 điểm: ", ext[2])
        return  False
    elif len(ext2) > 2:
        print("f\"(x) đổi dấu tại ít nhất 1 điểm: ", ext2[2])
        return  False

def sai_so(x, x_old, M, m, ct_saisoi):
    if ct_saisoi == 1:
        return abs(f(x)) / m
    elif ct_saisoi == 2:
        return (M - m) * abs(x - x_old) / m

def daycung(left, right, num):
    m = min(abs(df(a)), abs(df(b)))
    M = max(abs(df(a)), abs(df(b)))
    if f(left) * d2f(left) > 0:  # Chọn right luôn là fourie
        left, right = right, left
    x = left   # xấp xỉ nghiệm đầu = cực trái
    x_old = right
    Delta = sai_so(x, x_old, M, m, num)
    count = 0    # đếm số lần lặp
    fout.write("\n" + "_" * 85)
    fout.write("\n|{0:^10}|{1:^25}|{2:^25}|{3:^20}|".format("Lần lặp", "Nghiệm x", "f(x)", "Sai số"))
    fout.write("\n" + "_" * 85)
    while (not Delta < eps) and count < MAXLOOP:
        x_old = x
        x = x - f(x) * (right - x) / (f(right) - f(x))
        Delta = sai_so(x, x_old, M, m, num)
        count += 1
        fout.write("\n|{0:^10}|{1:^25}|{2:^25}|{3:^20}|".format(count, round(x, num_decimal), round(f(x), num_decimal), round(Delta, num_decimal)))
    fout.write("\n" + "_" * 85)
    return [x, count]


if __name__ == "__main__":
    show_fx()
    print("Nhập khoảng tìm nghiệm: ")
    a = float(input("Nhập a: "))
    b = float(input("Nhập b: "))
    eps = float(input("Nhập sai số: "))
    print()
    check = check_input(a, b)
    if not check:
        print("Kiểm tra lại INPUT")
    else:
        menu()
        choose = int(input("Nhập lựa chọn: "))
        if choose == 1:
            fout = open("D:\\TLHT\\GTS-PPS\\codepython\\Tucode\GTS\\Numerical-Analysis-Code\\F(x)_Equation\\daycung\\output_tn.txt", mode='w', encoding='utf-8')
            x0 = daycung(a, b, 1)
            print("Nghiệm của phương trình: ", x0[0])
            print("Số lần lặp: ", x0[1])
            fout.write(f"\nNghiệm của phương trình: {x0[0]}")
            fout.close()
        elif choose == 2:
            fout = open("D:\\TLHT\\GTS-PPS\\codepython\\Tucode\GTS\\Numerical-Analysis-Code\\F(x)_Equation\\daycung\\output_hn.txt", mode='w', encoding='utf-8')
            x0 = daycung(a, b, 2)
            print("Nghiệm của phương trình: ", x0[0])
            print("Số lần lặp: ", x0[1])
            fout.write(f"\nNghiệm của phương trình: {x0[0]}")
            fout.close()
