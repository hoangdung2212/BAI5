print("Sinh vien: Hoang Van Dung")
print("MSSV:235752012610063")
# main.py

import mymath

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập các phần tử của danh sách
lst = []
for _ in range(n):
    value = float(input("Nhập giá trị của phần tử: "))
    lst.append(value)

# Sử dụng các hàm từ module mymath để tìm phần tử lớn nhất, nhỏ nhất và sắp xếp danh sách
max_value = mymath.find_max(lst)
min_value = mymath.find_min(lst)
sorted_lst = mymath.sort_list(lst)

# In kết quả
print("Danh sách sau khi sắp xếp:", sorted_lst)
print("Phần tử lớn nhất trong danh sách là:", max_value)
print("Phần tử nhỏ nhất trong danh sách là:", min_value)
