arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12]]

N = 3  # 행의 길이 = len(arr)
M = 4  # 열의 길이 = len(arr[0])
# i 행의 좌표
# j 열의 좌표

# 1. 행 우선 순회
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j])

# 1-1. 행 우선순회를 역으로 조회!
# for i in range(N):
#     for j in range(M-1, -1, -1): #열을 반대로
#         print(arr[i][j])


# 2. 열 우선 순회
# for j in range(M):
#     for i in range(N):
#         print(arr[i][j])

# 2-1. 열 우선 순회를 역으로 조회!
# for j in range(M):
#     for i in range(N-1, -1, -1): #행을 반대로
#         print(arr[i][j])


# 3. 지그재그 순회
# for i in range(N):
#     for j in range(M):
#         print(arr[i][j + (M - 1 - 2 * j) * (i % 2)])


