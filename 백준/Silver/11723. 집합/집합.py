import sys

m = int(sys.stdin.readline())

result = set()

for _ in range(m):
    fx = list(sys.stdin.readline().split())
    if len(fx) == 1:
        if (fx[0]) == "all":
            result = {i for i in range(1, 21)}
        if (fx[0]) == "empty":
            result = set()
    else:
        command, x = fx[0], int(fx[1])
        if (command == "add"):
            result.add(x)
        if (command == "remove"):
            if x in result:
                result.discard(x)
        if (command == "check"):
            if x in result:
                print(1)
            else: print(0)
        if (command == "toggle"):
            if x in result:
                result.discard(x)
            else:
                result.add(x)
