import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    # N : 카드가 몇장인지
    N = int(input())
    # cards : 카드들
    cards =[int(card) for card in input()]

    # 카드 번호와 해당 개수 딕셔너리
    card_cnt_dict = {}

    # 각 카드 번호 별 개수 세기
    for card_number in cards:
        card_cnt_dict[card_number] = card_cnt_dict.get(card_number, 0) + 1

    # 가장 많은 카드 숫자와 장수
    most_freq_number = 0
    most_freq_count = 0

    # card_cnt_dict을 value 내림차순으로 정렬 - 인덱싱이 가능하도록 tuple로 반환
    sorted_card_cnt = sorted(card_cnt_dict.items(), key=lambda x: x[1], reverse=True)

    # 가장 많은 카드 숫자가 둘 이상인 경우
    if sorted_card_cnt[0][1] == sorted_card_cnt[1][1]:
        print(sorted_card_cnt)
        # cnt가 가장 많은 그 값을 가진 카드 넘버들의 리스트를 만든다.
        most_freq_count = sorted_card_cnt[0][1]
        most_freq_numbers = []
        for card_n_cnt in sorted_card_cnt:
            if card_n_cnt[1] == most_freq_count:
                most_freq_numbers.append(card_n_cnt[0])
        # 그 중에 가장 큰 수를 number로 할당한다.
        most_freq_number = max(most_freq_numbers)

    # 하나인 경우
    else:
        # 해당 카드의 번호와 장수를 각각 할당해준다.
        most_freq_number, most_freq_count = sorted_card_cnt[0][0], sorted_card_cnt[0][1]


    print("#{} {} {}".format(tc, most_freq_number, most_freq_count))