"""
합 구하기
n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum = sum + int(i)

print(sum)

"""

"""
세준이의 주작질

n = input()
mylist = list(map(int, input().split()))
mymax = max(mylist)
sum = sum(mylist)

print(sum*100/mymax/int(n))
"""

"""

import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp =0

for i in numbers:
    temp = temp+1
    prefix_sum.append(temp) 

for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
    
"""


"""

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
"""

"""
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))

S = [0] * n
C = [0] * m
S[0] = A[0]
answer = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i]

for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        answer += 1
    C[remainder] += 1

for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)

print(answer)
"""


"""
n = int(input())
count = 1
start_ind = 1
end_ind = 1
sum = 1

while end_ind != n:
    if sum == n:
        count += 1
        end_ind += 1
        sum += end_ind
    elif sum > n:
        sum -= start_ind
        start_ind += 1
    else:
        end_ind += 1
        sum += end_ind

print(count)

"""


"""
import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()
count = 0
i = 0
j = N -1

while i < j:
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)

"""

"""
import sys
input = sys.stdin.readline
N = int(input())
Result = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N):
    find = A[k]
    i = 0
    j = N - 1
    while i<j:
        if A[i] + A[j] == find:
            if i != k and j != k:
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1
print(Result)
"""

"""
window dna

checkList = [0]*4
myList = [0]*4
checkSecret = 0

def myadd(c):
    global checkSecret, myList, checkList
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret+=1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret+=1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret+=1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret+=1

def myremove(c):
    global checkSecret, myList, checkList
    if c == 'A':
        myList[0] -= 1
        if myList[0] == checkList[0]:
            checkSecret -= 1
    elif c == 'C':
        myList[1] -= 1
        if myList[1] == checkList[1]:
            checkSecret -= 1
    elif c == 'G':
        myList[2] -= 1
        if myList[2] == checkList[2]:
            checkSecret -= 1
    elif c == 'T':
        myList[3] -= 1
        if myList[3] == checkList[3]:
            checkSecret -= 1

S,P = map(int, input().split())
Result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
    if checkList[i] == 0:
        checkList += 1

for i in range(P):
    myadd(A[i])
if checkSecret == 4:
    Result+= 1
for i in range(P,S):
    j = i -P
    myadd(A[i])
    myremove(A[j])
    if checkSecret == 4:
        Result += 1
print(Result)
"""


"""
스택 기본
N = int(input())
A = [0]*N
for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += "+\n"
        stack.pop()
        answer += "-\n"
    else:
        n = stack.pop()
        if n > su:
            print("NO")
            result = False
            break
        else:
            answer += "-\n"
if result:
    print(answer)
"""

"""
오큰수 문제

N = int(input())
ans = [0]*N
A = list(map(int, input().split()))
myStack = []

for i in range(N):
    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]
    myStack.append(i)
    
while myStack:
    ans[myStack.pop()] = -1
    
result = "" 

for i in range(N):
    result += str(ans[i]) + ""
print(result)
"""

"""
카드 게임
from collections import deque
N = int(input())
myQueue = deque()

for i in range(1, N+1):
    myQueue.append(i)

while len(myQueue) > 1:
    myQueue.popleft()
    myQueue.append(myQueue.popleft())

print(myQueue[0])

"""
