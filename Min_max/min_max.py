
delta = 1e-7
eta = 1e-5

def f(x):
    return 2*x**5 - 12*x**4 + 3*x**2 - 15


def df(x):
    return (f(x + delta) - f(x - delta)) / (2 * delta)


def symmetry_df(x):
    return -df(x)



def gradient_descent(a, b):
    x_ct = a
    count = 1
    while (not (abs(df(x_ct)) < delta)):
        x_ct = x_ct - eta * df(x_ct)
        count += 1
        if count > 1e+7:
            break
        if x_ct > b:
            print("Hàm đơn điệu trên (", a, " , ", b, ")")
            return x_ct
        elif x_ct < a:
            # print("Hàm đang có xu hướng tăng -> tìm cực đại")
            return x_ct
    return x_ct


def gradient_descent_symmetry(a, b):
    x_cd = a
    count = 0
    while (not (abs(symmetry_df(x_cd)) < delta)):
        x_cd = x_cd - eta * symmetry_df(x_cd)
        count += 1
        if count > 1e+6:
            break
        if x_cd > b:
            print("Hàm đơn điệu trên (", a, ",", b, ")")
            return x_cd
        elif x_cd < a:
            # print("Hàm đang có xu hướng giảm -> tìm cực tiểu.")
            return x_cd
    return x_cd


def find_Extreme_of_theFuntion(a, b):
    global count1
    global count2
    while True:
        temp1 = gradient_descent(a, b)
        temp2 = gradient_descent_symmetry(a, b)
        if (temp1 > b and temp2 < a) or (temp1 < a and temp2 > b):
            break
        if (temp1 > a) and (temp1 < b):
            x_ct.append(temp1)
            a = x_ct[count1] + 0.05
            count1 += 1

        if (temp2 > a):
            if (temp2 < b):
                x_cd.append(temp2)
                a = x_cd[count2] + 0.05
                count2 += 1
    print("Cực tiểu: ", x_ct[2:])
    print("Cực đại: ", x_cd[2:])


if __name__ == '__main__':
    a = float(input("Nhap a: "))
    b = float(input("Nhap b: "))
    count1: int = 2
    count2: int = 2
    x_ct = [a, b]
    x_cd = [a, b]
    find_Extreme_of_theFuntion(a, b)
    # Tìm min của hàm số:
    x_min = a
    for i in x_ct:
        if f(i) < f(x_min):
            x_min = i
    # Tìm max của hàm số:
    x_max = a
    for i in x_cd:
        if f(i) > f(x_max):
            x_max = i
    print("Giá trị nhỏ nhất của hàm số trên đoạn: f(", round(x_min, 3), ") = ", f(x_min))
    print("Giá trị lớn nhất của hàm số trên đoạn: f(", round(x_max, 3), ") = ", f(x_max))