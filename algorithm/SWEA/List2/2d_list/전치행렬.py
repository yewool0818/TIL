# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])

# 3 * 3 행렬
arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

for i in range(len(arr)):  # 0, 1, 2
    for j in range(len(arr[0])):  # 0, 1, 2
        if i < j:  # 한 번만 바꾸도록
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

for i in range(len(arr)):
    print(arr[i])
    # [1, 4, 7]
    # [2, 5, 8]
    # [3, 6, 9]

