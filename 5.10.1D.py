# sort.py

def bubbleSort(nlist):
    n = len(nlist)
    for i in range(n):
        # Cờ hiệu để kiểm tra nếu danh sách đã được sắp xếp
        swapped = False
        for j in range(0, n-i-1):
            if nlist[j] > nlist[j+1]:
                # Hoán đổi các phần tử nếu chúng ở sai thứ tự
                nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
                swapped = True
        # Nếu không có phần tử nào được hoán đổi trong vòng lặp bên trong, danh sách đã được sắp xếp
        if not swapped:
            break
