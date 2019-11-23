"""
문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

제한 조건
n은 10,000,000,000이하인 자연수입니다.

입출력 예
n	return
12345	[5,4,3,2,1]
"""
def solution(n):
    # 0:00:00.416232
    return list(map(int, str(n)))[::-1]

    # code refactoring
    # 0:00:00.411518
    # return list(map(int, reversed(str(n))))


print(solution(12345))

# from datetime import datetime
# s = datetime.now()
# for _ in range(100000):
#     solution(12345)
#     solution(3)
#     solution(1230553)
# print(datetime.now() - s)

