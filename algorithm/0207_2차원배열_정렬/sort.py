# Bubble Sort

def bubbleSort(a): # 정렬할 List
    for i in range(len(a)-1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a

# print(bubbleSort([66, 7, 78, 12, 42]))
