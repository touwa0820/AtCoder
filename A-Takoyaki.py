import math
N, X, T = map(int,input().split())

s = math.ceil(N/X)
print(s*T)