"""
DFS

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m = map(int, input().split())

A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count+=1
        DFS(i)

print(count)
"""

"""
DFS로 소수 찾기
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())

def isPrime(num):
    for i in range(2, int(num / 2 + 1)):
        if num % i == 0:
            return False
    return True

def DFS(number):
    if len(str(number)) == N:
        print(number)
    else:
        for i in range(1, 10):
            if i % 2 == 0:
                continue
            if isPrime(number * 10 + i):
                DFS(number * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)

"""

"""
DFS로 친구 찾기

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
arrive = False
A = [[] for _ in range(N+1)]
visited = [False]*(N+1)

def DFS(now, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[now] = True
    for i in A[now]:
        if not visited[i]:
            DFS(i, depth + 1)
    visited[now] = False
    
for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)
    
for i in range(N):
    DFS(i, 1)
    if arrive:
        break
    if arrive:
        print(1)        
    else:
        print(0)
"""

"""
DFS & BFS

from collections import deque
N, M, Start = map(int, input().split())
A = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N+1):
    A[i].sort()

def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)
visited = [False] * (N+1)
DFS(Start)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Mode = queue.popleft()
        print(now_Mode, end=' ')
        for i in A[now_Mode]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

print()
visited = [False] * (N + 1)
BFS(Start)

"""

"""
미로 탑색

from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())
A = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]

for i in range(N):
    numbers = list(input())
    for j in range(M):
        A[i][j] = int(numbers[j])

def BFS(i, j):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True

    while queue:
        now = queue.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if x >= 0 and y >= 0 and x < N and y < M:
                if A[x][y] != 0 and not visited[x][y]:
                    visited[x][y] = True
                    A[x][y] = A[now[0]][now[1]] + 1
                    queue.append((x, y))
BFS(0, 0)
print(A[N-1][M-1])
"""

"""
트리의 지름 구하기 with BFS

"""

"""
binary search

N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
target_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = target_list[i]
    start = 0
    end = len(A) -1
    while start <= end:
        midi = int((start + end) / 2)
        midv = A[midi]

        if midv > target:
            end = midi -1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
        if find:
            print(1)
        else:
            print(0)
"""

"""
필요동전 최소값 구하기 with Greedy 

N ,K = map(int, input().split())
A = [0]*N
for i in range(N):
    A[i] = int(input())
    
count = 0

for i in range(N-1, -1, -1):
    if A[i] <= K:
        count += int(K/A[i])
        K = K % A[i]
        
print(count)
"""

"""
primary Queue로 카드 정렬


from queue import PriorityQueue
N = int(input())
pq = PriorityQueue()

for _ in range(N):
    date = int(input())
    pq.put(date)
    
data1 = 0
data2 = 0
sum = 0

while pq.qsize()>1:
    data1 = pq.get()
    data2 = pq.get()
    tmp = data1 + data2
    sum += tmp
    pq.put(tmp)
    
print(sum
"""


"""
회의실 시간 안겹치고 쓰기 with Greedy Algorithm

N = int(input())
A = [[0] * 2 for _ in range(N)]

for i in range(N):
    S, E = map(int, input().split())
    A[i][0] = E
    A[i][1] = S

A.sort()
count = 0
end = -1

for i in range(N):
    if A[i][1] >= end:
        end = A[i][0]
        count += 1
print(count)
"""

"""
괄호 재배치로 최소값 만들기


"""

ans = 0
A = list(map(str, input().split("-")))

def mySum(i):
    sum = 0
    temp = str(i).split("+")
    for i in temp:
        sum += int(i)
    return sum

for i in range(len(A)):
    temp = mySum(A[i])
    if i == 0:
        ans += temp
    else:
        ans -= temp
print(ans)