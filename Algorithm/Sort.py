"""
N = int(input())
A = [0] * N

for i in range(N):
    A[i] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if A[j] > A[j+1]:
            temp = A[j]
            A[j] = A[j+1]
            A[j+1] = temp
for i in range(N):
    print(A[i])
"""


"""
import sys
input = sys.stdin.readline

N = int(input())
A = []

for i in range(N):
    A.append((int(input()), i))

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i

print(Max + 1)

"""


"""
N = int(input())
A = list(map(int, input().split()))
S = [0]*N

for i in range(1,N):
    insert_point = i
    insert_value = A[i]
    for j in range(i-1, -1, -1):
        if A[j] > A[i]:
            insert_point = j + 1
            break
        if j == 0:
            insert_point = 0
    for j in range(i, insert_point, -1):
        A[j] = A[j-1]
    A[insert_point] = insert_value

"""

"""
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

def quickSort(S,E,K):
    global A
    if S < E:
        pivot = partition(S, E)
        if pivot == K:
            return
        elif K < pivot:
            quickSort(S, pivot-1, K)
        else:
            quickSort(pivot+1, E, K)

def swap(i, j):
    global A
    temp  = A[i]
    A[i] = A[j]
    A[j] = temp

def partition(S,E):
    global A

    if S+1 == E:
        if A[S] > A[E]:
            swap(S,E)
        return E

    M = (S+E)//2
    swap(S,M)
    pivot = A[S]
    i = S + 1
    j = E

    while i <=j:
        while pivot <A[j] and j > 0:
            j = j-1
        while pivot > A[i] and i < len(A)-1:
            i = i + 1
        if i <= j:
            swap(i,j)
            i = i + 1
            j = j - 1

    A[S] = A[j]
    A[j] = pivot
    return j

quickSort(0, N - 1, K-1)
print(A[K-1])
"""

"""
import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_Sort(s,e):
    if e-s < 1:
        return
    m = int((s + (e - s) / 2))
    merge_Sort(s,m)
    merge_Sort(m+1, e)
    for i in range(s, e+1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m + 1

    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

N = int(input())
A = [0]*int(N+1)
tmp = [0]*int(N+1)

for i in range(1, N+1):
    A[i] = int(input())

merge_Sort(1,N)

for i in range(1, N+1):
    print(str(A[i]) + '\n')
"""

