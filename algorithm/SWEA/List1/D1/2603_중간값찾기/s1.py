import sys

sys.stdin = open("input.txt")

# 점수의 개수
N = int(input())
# N개의 점수
scores = list(map(int, input().split()))

# 1. 버블 정렬
# for i in range(N-1, 0, -1):
#     for j in range(0, i):
#         if scores[j] > scores[j+1]:
#             scores[j], scores[j+1] = scores[j+1], scores[j]

# print(scores[N//2])

# 2. 선택 (selection)
# 총 길이의 반만큼만 정렬 후, 원하는 index에 있는 값을 확보

def selection(a, k):
    for i in range(len(a)-1):
        max_idx = i
        for j in range(i+1, len(a)):
            if a[max_idx] < a[j]:
                max_idx = j

        a[i], a[max_idx] = a[max_idx], a[i]

    return a

print(selection(scores, N//2+1)[N//2])

