# print(4 & 12)

# 1 << n : 2^n 즉, 원소가 n개일 경우 모든 부분집합의 수를 의미한다.
# print(1 << 3)  # 8 : 3의 부분집합의 개수

# i & (1<<j) : i의 j번째 비트가 1인지 아닌지 리턴한다.
# print(4 & (1 << 3))  # 0

materials = ['계란', '치즈', '떡']

N = len(materials) # N : 원소의 개수

for i in range(1 << N):  # 모든 부분집합 개수만큼 반복
    ans = " "
    for j in range(N):   # 원소의 수만큼 비트를 비교함
        if i & (1 << j): # i의 j번째 비트가 1이면 j번째 원소 출력
            ans += materials[j] + " "

    print(ans, "라면입니다.")


