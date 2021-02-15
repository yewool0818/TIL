arr = [[1,2,3,4], [1,2,3]]

# for i in arr:
#     print(i)

# 3 4
# 1 2 3 4
# 5 6 7 8
# 9 1 2 3

# 입력 방법 세 가지

# 1. 기본
# N : 행의 개수, M : 열의 개수
N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

for i in arr:
    print(i)


# 2. 미리 빈 리스트를 만들어 놓고 반복문
N, M = map(int, input().split())

arr = [0] * N

for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in arr:
    print(i)


# 3. 리스트 컴프리헨션을 활용
N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

for i in arr:
    print(i)
