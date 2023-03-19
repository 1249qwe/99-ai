# 用python写一个打印九九乘法表的程序

for i in range(1, 10): # 循环1到9

    for j in range(1, i + 1): # 循环1到i

        print(f"{j} x {i} = {j * i}", end=" ") # 打印j乘以i的结果，用空格分隔

    print() # 换行
