import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
words = set()
for _ in range(N):
    word = input()
    words.add((len(word), word))
words = list(words)
words.sort()
for _, word in words:
    print(word)