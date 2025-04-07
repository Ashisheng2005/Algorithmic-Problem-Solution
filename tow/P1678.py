
m, n = map(int, input().split())
mp = list(map(int, input().split()))
np = list(map(int, input().split()))

mp.sort()
ans = 0
for i in np:
    if i < mp[0]:
        ans += mp[0] - i
        continue    
            
    if n == 1:
        ans += abs(mp[0] - i)
        continue

    l=0
    r = n
    while l < r:
        mid = (l + r) // 2
        if mp[mid] <= i:
            l = mid + 1
        else:
            r = mid
    ans += min(abs(mp[l-1]-i), abs(mp[l]-i))

print(ans)


