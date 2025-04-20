'''
Nhâp vào 1 số nguyên ở hệ thập phân, yêu cầu xuất ra 1 số ở hệ nhị phân.
Ví dụ:
N = 13 (Hệ Thập Phân) => 1101

13 | 2
 6 | 2 -> 1
 3 | 2 -> 0
 1 | 2 -> 1
 0 | 2 -> 1

'''

#Cách dùng hàm bin() trong python
n = int(input('Nhap n = '))
print(f"So {n} chuyen sang nhị phân là:", bin(n)[2:])

#Tự VIẾT
if n == 0:
    print(f"So {n} o he nhi phan la 0")
else: 
    binary = ''
    while(n > 0):
        binary  = str (n % 2) + binary
        n//=2

print (f"So {n} o hệ nhị phân {binary}")
