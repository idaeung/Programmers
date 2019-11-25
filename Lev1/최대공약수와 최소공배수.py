"""
문제 설명
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

제한 사항
두 수는 1이상 1000000이하의 자연수입니다.

입출력 예
n	m	return
3	12	[3, 12]
2	5	[1, 10]

입출력 예 설명
입출력 예 #1
위의 설명과 같습니다.

입출력 예 #2
자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.
"""
def get_GCD(a, b):
    return a if not b else get_GCD(b, a%b)

def solution(n, m):
    # 0:00:00.656091, 0:00:00.577994
    GCD = get_GCD(*[m, n] if n <= m else [n, m])
    return [GCD, int(n*m / GCD)]

    # code refactoring
    # 0:00:00.656090, 0:00:00.671707 (loop 때문에 속도가 더 느림)
    # gcd = lambda a, b: a if not b else gcd(b, a%b)
    # GCD = get_GCD(*[m, n] if n <=m else [n, m])
    # return [GCD, n*m // GCD]

# print(solution(3, 12))
# print(solution(121, 100000))
# print(solution(2, 5))
# print(solution(60, 48))
# print(solution(121, 11))

from datetime import datetime
s = datetime.now()
for _ in range(100000):
    solution(555, 100000)
    solution(43123, 1200302)
    solution(100000, 555)
    solution(1200302, 43123)
print(datetime.now() - s)
