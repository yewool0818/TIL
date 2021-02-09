# 2차원 배열
arr = [[0, 1, 2, 3], 
       [4, 5, 6, 7]]

# 순회
# 행 우선 순회
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j])

# 열 우선 순회
for j in range(len(arr[0])):
    for i in range(len(arr)):
        print(arr[i][j])


# 전치 행렬
arr2 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

result = [[0] * len(arr2)] * len(arr2)

for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        if i < j :
            result[i][j], result[j][i] = arr2[j][i], arr2[i][j]

print(result)


# 연습문제 1
random_list = []
inside_list = []
for _ in range(0, 5):
    for _ in range(0, 5):
        inside_list += [0]
    random_list.append(inside_list)
print(random_list)

random_list = [[0]*5]*5
for i in range(5):
    for j in range(5):
        random_list[i][j] = random.randint(1, 50)
print(random_list)