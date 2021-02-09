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

    # 넘버와 카운트 비교
    for number, count in card_cnt_dict.items():
        # count가 가장 많으면 가장 많은 카드 숫자와 장수에 각각 number, count값 할당
        if count > most_freq_count:
            most_freq_number = number
            most_freq_count = count

        # count가 다른 값에서 할당된 most_freq_count와 겹칠 때,
        if count == most_freq_count:
            # 현재의 number가 기존의 most_freq_number보다 크다면, 현재의 nunmber로 대체!
            if most_freq_number < number:
                most_freq_number = number

    print("#{} {} {}".format(tc, most_freq_number, most_freq_count))