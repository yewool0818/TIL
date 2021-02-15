# 1. 순차 검색


# 1-1. 정렬이 되어있는 경우

arr = [4, 9, 11, 23, 19, 7]


key = 23

for i in range(len(arr)):
    if key == arr[i]:
        print(i, '에 위치하고 있음')
        break
else:
    print('리스트에 없음')

# 함수
def sequentailSearch(unsorted_arr, n, key):
    i = 0
    while i < n and unsorted_arr[i] != key:
        i += 1
    if i < n:
        return i
    else:
        return -1


# 1-2. 정렬이 되어있지 않은 경우
sorted_arr = sorted(arr)
key = 11
# sorted_arr = [4, 7, 9, 11, 19, 23]
for i in range(len(sorted_arr)):
    if key == sorted_arr[i]:
        print(i, "에 위치하고 있음")
        break
    elif key > arr[i]:
        print(i, "번째 까지만 탐색함")
        break
else:
    print("찾지 못 함")

def sequentailSearch2(sorted_arr, n, key):
    i = 0
    while i < n and sorted_arr[i] < key:
        i += 1
    if i < n and sorted_arr[i] == key:
        return i
    else:
        return -1

