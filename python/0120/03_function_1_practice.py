##### sort() 와 sorted() 차이
# sort() : 원본 자체를 바꿈
a = [5, 1, 3, 2]
a.sort()
#print(a)

# sorted() : 정렬 후 반환
a = [5, 1, 3, 2]
b = sorted(a)
#print(b)


##### 둘 중 합이 큰 리스트 반환
def my_list_max(numbers1, numbers2):
    # 1. 변수 초기화
    numbers1_total = 0
    numbers2_total = 0

    # 2. 각 리스트의 합 구하기 - 리스트의 길이가 다를 수 있기 때문에 for문을 각각 돌린다.
    for number in numbers1:
        numbers1_total += number

    for number in numbers2:
        numbers2_total += number

    # 3. 합의 크기 비교하여 큰 수 리턴
    if numbers1_total > numbers2_total:
        return numbers1
    else:
        return numbers2

# print(my_list_max([1, 2], [3, 4]))
# print(my_list_max([10, 3], [5, 9]))


##### 원기둥의 부피
def cylinder(r, h):
    return 3.14 * r ** 2 * h

# print(cylinder(5,2))
# print(cylinder(2,5)) # 순서를 바꾸면 다른 값이 나옵니다.



##### 기본 인자
def greeting(age, name='밀크'):
    print(f'안녕? 난 {age}살 {name}이라고 해!')

greeting(3)

