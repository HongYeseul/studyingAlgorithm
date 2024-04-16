import math, sys

def func(num):
    f = math.floor(num)
    if ((f + 0.5) <= num):
        return f + 1
    else:
        return f

n = int(sys.stdin.readline())

vote = []
for _ in range(n):
    vote.append(int(sys.stdin.readline()))

vote.sort()

people = func(n * 0.15)
# print("삭제하는 사람 개수:",people)

del vote[:people]
del vote[len(vote) - people:len(vote)]

# print(vote)

if len(vote)!=0:
    print(func(sum(vote)/len(vote)))
elif len(vote) == 1:
    print(vote[0])
else:
    print(0)
