'''
마지막 정점법호, 간선
6 8
0 1 0 2 0 5 0 6 5 3 4 3 5 4 6 4
'''
V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjM = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjM[n1][n2] = 1
    # adjM[n2][n1] = 1  # 무향그래프인 경우 필요하고 유향일땐 없어야됨

for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjL[n1].append(n2)
    # adjL[n2].append(n1) # 무향그래프인 경우 필요하고 유향일땐 없어야됨


print()
