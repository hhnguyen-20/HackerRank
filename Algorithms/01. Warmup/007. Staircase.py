# Problem: https://www.hackerrank.com/challenges/staircase/problem
# Score: 10.0


def staircase(n):
    for i in range(1, n + 1):
        print(' ' * (n  - i) + '#' * i)

n = int(input().strip())
staircase(n)
