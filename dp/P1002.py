

n, m, x, y =  map(int, input().split())

dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

dp[-1][0] = 1
#马点
house_ = ((x,y),(x-2,y-1),(x-1,y-2),(x+1,y-2),(x+2,y-1),(x+1,y+2),(x+2,y+1),(x-2,y+1),(x-1,y+2))

for i in range(n + 1):
    for j in range(m + 1):
        if (i, j) not in house_:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
from tool import two_dimensions
two_dimensions(dp)

print()
print(dp[n][m])

