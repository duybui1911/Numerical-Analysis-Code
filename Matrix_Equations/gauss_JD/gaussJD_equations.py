import numpy as np 

path = 'D:\\TLHT\\GTS-PPS\\codepython\\Tucode\\GTS\\Numerical-Analysis-Code\\Matrix_Equations\\gauss_JD\\'


class Gauss_Jordan_Algorithms:
    np.set_printoptions(suppress=True, linewidth=np.inf, precision=10)


    matrix = np.genfromtxt(path + 'GJ_input.txt', delimiter=' ')
    A = matrix[:, :-1] #Lưu lại ma trận ban đầu để lát kiểm tra tính đúng của nghiệm
    index_row = []  # Khởi tạo mảng lưu các hàng của phần tử giải (theo thứ tự)
    index_column = []  # Khởi tạo mảng lưu các cột của phần tử giải (theo thứ tự)
    result = np.zeros(
        (len(matrix[0]) - 1, len(matrix[0])))  # Khởi tạo ma trận lưu kết quả với các giá trị ban đầu bằng 0

    def solutions_checker(self):
        """Trong trường hợp nghiệm duy nhất, hàm được sử dụng để kiểm tra lại nghiệm
        bằng cách nhân lại ma trận kết quả với hệ số ban đầu"""
        A = np.loadtxt("input.txt", delimiter=' ')[:, :-1]  # ma trận hệ số trong phương trình AX=B
        print()
        print("- - - - - Kiểm tra nghiệm - - - - -")
        print(np.matmul(A, np.delete(self.result, np.s_[1:], axis=1)))  # In ra ma trận A * ma trận X

    def find_pivot_element(self):
        """Hàm được dùng để tìm phần tử giải"""
        # global index_row, index_column
        index_temp = []
        pivot_element = 0
        for row in range(0, len(self.matrix)):
            if row in self.index_row:
                continue  # Bỏ qua vì hàng này đã có phần tử giải
            max_row = np.amax(abs(self.matrix[row, 0:(len(self.matrix[0]) - 1)]))  # Tìm phần tử lớn nhất trong hàng row
            if (1 in self.matrix[row, 0:(len(self.matrix[0]) - 1)]) or (
                    -1 in self.matrix[row,
                          0:(len(self.matrix[0]) - 1)]):  # Nếu có 1 hoặc -1 trong hàng row => chọn làm phần tử giải
                pivot_element = 1
                row_pivot_element = row
                index_temp = np.where(abs(self.matrix[row, 0:(len(self.matrix[0]) - 1)]) == pivot_element)
                index_temp = index_temp[:1]
                index_temp = index_temp[0][0]
                break
            elif max_row > pivot_element:  # Lưu giá trị phần tử giải, tìm vị trí trên ma trận
                pivot_element = max_row
                row_pivot_element = row
                index_temp = np.where(abs(self.matrix[row, 0:(len(self.matrix[0]) - 1)]) == pivot_element)
                index_temp = index_temp[:1]
                index_temp = index_temp[0][0]
        if pivot_element != 0:  # Lưu vị trí hàng và cột của phần tử giải
            self.index_row.append(row_pivot_element)
            self.index_column.append(int(index_temp))
            """ In ra giá trị và vị trí phần tử giải"""
            print()
            print("Phần tử giải: ", round(self.matrix[self.index_row[-1]][self.index_column[-1]], 10))
            print("Vị trí: ", self.index_row[-1] + 1, self.index_column[-1] + 1)
            print()

    def Gauss_Jordan_method(self):
        """Phương pháp Gauss - Jordan"""
        global matrix
        self.find_pivot_element()
        zeros_array = np.zeros((len(self.matrix), len(self.matrix[0])))  # Tạo 1 ma trận không
        for row in range(0, len(self.matrix)):
            if row == self.index_row[-1]:
                continue
            m = - self.matrix[row][self.index_column[-1]] / self.matrix[self.index_row[-1]][
                self.index_column[-1]]  # Tìm m
            zeros_array[row] = self.matrix[self.index_row[-1]] * m
        self.matrix = self.matrix + zeros_array

    def normalize_pivot_element(self):
        """Chuẩn hóa hệ số của phần tử giải (chia để hệ số của phần tử giải =1)"""
        for i in range(len(self.index_row)):
            self.matrix[self.index_row[i]] = self.matrix[self.index_row[i]] / self.matrix[self.index_row[i]][
                self.index_column[i]]
        print("Ma trận sau khi chuẩn hóa hệ số: ")
        print(self.matrix)

    def rank(self):
        """Tìm hạng của ma trận hệ số A và hạng của ma trận mở rộng"""
        rank1 = 0  # Hạng của ma trận hệ số A
        rank2 = 0  # Hạng của ma trận mở rộng
        for row in range(0, len(self.matrix)):
            if np.amax(abs(self.matrix[row, 0:(len(self.matrix[0]) - 1)])) > 0:
                rank1 = rank1 + 1
            if np.amax(abs(self.matrix[row, 0:len(self.matrix[0])])) > 0:
                rank2 = rank2 + 1
        if rank1 < rank2:
            print("Hệ PT vô nghiệm...Niệm!")
            f=open(path + 'GJ_output.txt',"w")
            f.write("Hệ PT vô nghiệm...Niệm!")
            f.close()
        elif rank1 < (len(self.matrix[0]) - 1):
            print("Hệ PT có vô số nghiệm...Niệm!")
            self.display_solutions()
        else:
            print("Hệ PT có nghiệm duy nhất!")
            self.display_solutions()
            # solutions_checker()

    def display_solutions(self):
        """Ghi kết quả vào ma trận result, in ma trận result ra màn hình và xuất ra file output.txt"""
        # Ghi kết quả vào ma trận result
        # global result
        for column in range(len(self.matrix[0]) - 1):
            if column in self.index_column:
                vt = self.index_column.index(column)
                self.result[column][0] = self.matrix[self.index_row[vt]][len(self.matrix[0]) - 1]
                for i in range(len(self.matrix[0]) - 1):
                    if i not in self.index_column:
                        self.result[column][i + 1] = -self.matrix[self.index_row[vt]][i]
            else:
                self.result[column][column + 1] = 1

        # In ma trận result ra màn hình
        print()
        print("Nghiệm tìm được: ")
        print(self.result[:,0])

        # Xuất kết quả ra file output.txt
        np.savetxt(path + 'GJ_output.txt', self.result, fmt='%.5f')  # %.5f: lấy 5 chữ số sau dấu phẩy ghi vào file

    # Main program
    def main(self):
        print(self.matrix)
        print("- - - - - - - - - - - - - - - - - - - -")
        print()
        for i in range(0, min(len(self.matrix), len(self.matrix[0]))):
            self.Gauss_Jordan_method()
            print(self.matrix)
            print("- - - - - - - - - - - - - - - - - - - -")
        # print("- - - - - Chuẩn hóa hệ số - - - - -")
        self.normalize_pivot_element()
        print("- - - - - Kết luận - - - - -")
        self.rank()
        print()
        print("Kiểm tra nghiệm A*x = ", self.A@self.result[:,0].T)

try:
    RUN = Gauss_Jordan_Algorithms()
    RUN.main()
except:
    f = open(path + 'GJ_output.txt', "w")
    f.write("Lỗi!")
    f.close()

