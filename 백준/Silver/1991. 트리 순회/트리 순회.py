import sys

N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]
for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    node, left, right = ord(node)-64, ord(left)-64, ord(right)-64
    
    tree[node].append(left)
    tree[node].append(right)


def preOrder(start):
    if start != -18:
        print(chr(start+64), end="")
        preOrder(tree[start][0])
        preOrder(tree[start][1])

def inOrder(start):
    if start != -18:
        inOrder(tree[start][0])
        print(chr(start+64), end="")
        inOrder(tree[start][1])

def postOrder(start):
    if start != -18:
        postOrder(tree[start][0])
        postOrder(tree[start][1])
        print(chr(start+64), end="")

# 전위/중위/후위
preOrder(1)
print()
inOrder(1)
print()
postOrder(1)