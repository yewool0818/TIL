'''
애너그램

애너그램(anagram)은 단어나 문장을 구성하고 있는 문자의 순서를 바꾸어 다른 단어나 문장을 만드는 놀이입니다.
두 문자열이 공백으로 구분되어 입력된다고 했을 때, 서로 애너그램인지 판별하는 함수를 작성하시오.
입력 문자는 모두 소문자로 빈칸 없이 제공됩니다.

---
[입력 예시]
ohlamesaint themonalisa

[출력 예시]
True
'''

def check_anagram(text1, text2):
    # 변수 초기화
    flag = 'T'
    t1_dict = dict()
    t2_dict = dict()

    # text1과 text2를 비교
    # text1의 문자별 길이와 text2의 문자 별 길이를 비교한다.
    for t1 in set(list(text1)):
        t1_dict[t1] = list(text1).count(t1)

    for t2 in set(list(text2)):
        t2_dict[t2] = list(text2).count(t2)

    # 비교한다
    for t1_val, t2_val in zip(t1_dict.values(), t2_dict.values()):
        if t1_val != t2_val: # 서로 다르면, 
            flag = 'F'       # flag를 F로 바꾸고
            break            # 순회를 멈춘다.
   
    return flag


if __name__ == '__main__':
    print(check_anagram('ohlamesaint', 'themonalisa'))  #=> T
    print(check_anagram('apple', 'eppla'))  #=> T
    print(check_anagram('banana', 'babana'))  #=> F