"""
문제 설명
자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

제한사항
N의 범위 : 100,000,000 이하의 자연수

입출력 예
N	answer
123	6
987	24

입출력 예 설명
입출력 예 #1
문제의 예시와 같습니다.

입출력 예 #2
9 + 8 + 7 = 24이므로 24를 return 하면 됩니다.
"""
def solution(n):
    # 1
    return sum([int(v) for v in str(n)])

    # code refactoring
    # 2
    # if n < 10:
    #     return n;
    # return (n % 10) + solution(n // 10)

    # 3
    # return sum(map(int, str(n)))

print(solution(123))
print(solution(987))

# from datetime import datetime
# s = datetime.now()
# for _ in range(100000):
#     solution(100000000)
#     solution(99999999)
#     solution(98762012)
# print(datetime.now() - s)

# 1 -> 0:00:00.697535
# 2 -> 0:00:00.436367
# 3 -> 0:00:00.546246