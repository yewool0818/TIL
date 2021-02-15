import sys

sys.stdin = open("input.txt")

T = 10

for tc in range(1, T + 1):
    building_count = int(input())
    building_list = list(map(int, input().split()))

    # 조망권이 확보된 집
    total = 0

    # 빌딩들 순회
    for i in range(building_count):
        # 현재 위치의 빌딩 높이
        now = building_list[i]

        # 현재 위치의 건물이 없다면 == 빌딩 높이가 0이라면
        if now == 0:
            # 다음 건물로 넘어간다.
            continue # - for문의 다음 인덱스로 이동

        # 현재 위치에 건물이 있다면
        # 양 옆 건물 2개(총 4개의 건물) 건물과 높이 비교
        else:
            # 나를 제외한 주변 건물 중 가장 높은 건물 찾기

            # 최대 높이 저장용
            max_height = 0
            idx = [-2, -1, 1, 2]

            # 좌우 두개씩 총 네번 반복
            for j in range(4):
                # 위 idx list에 인덱스를 적용해서 반복하기
                if building_list[i+idx[j]] > max_height: # building_list[i-2] -> [i-1] -> [i+1] -> [i-2] 진행
                    max_height = building_list[i+idx[j]]

            # 만약 현재위치의 건물 높이가 좌우 총 4개 건물 중 가장 높다면
            if now > max_height:
                # 조망권이 확보되었다고 볼 수 있다.
                # 현재 높이에서 max_height를 빼는 이유는 max_height만큼은 조망권 확보가 안되기 때문이다.
                total += now - max_height

    print("#{} {}".format(tc, total))
