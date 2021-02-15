bit = [0, 0, 0, 0]

for i in range(2): # 0, 1
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(*bit) # *list : 리스트 없애줌 - *: unpacking 연산자


for i in range(len(bit)):
    for b in range(2):
        bit[i] = b
        print(bit)