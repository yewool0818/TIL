import sys
sys.stdin = open('input.txt')

N = int(input())
result = 1 if N%2 == 1 else 0
print(result)

numbers = list(map(int, input().split()))
result = sum(numbers)
print(result)

N = int(input())
numbers = []
for _ in range(N):
    row = list(map(int, input().split()))
    numbers.append(row)
print(numbers[1][1])



