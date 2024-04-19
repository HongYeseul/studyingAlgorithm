import sys
N, M = map(int, sys.stdin.readline().split())

dictionary = dict()

for i in range(1, N+1):
    pokemon = sys.stdin.readline().rstrip()
    dictionary[i] = pokemon
    dictionary[pokemon] = i

# print(dictionary)

for i in range(M):
    command = sys.stdin.readline().rstrip()
    if command.isdigit():
        print(dictionary[int(command)])
    else:
        print(dictionary.get(command))