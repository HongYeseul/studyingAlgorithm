import sys
from collections import Counter

N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
makeResult = list(map(int, sys.stdin.readline().split()))

counter = Counter(cards)

for card in makeResult:
    if card in counter:
        print(counter[card], end=" ")
    else:
        print("0", end=" ")