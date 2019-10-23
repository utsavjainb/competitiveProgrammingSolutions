def sol(n, a, b):
    decrem = b
    ans = []
    if n < a:
        return []
    if (a <= n <= b):
        return [n]
    if n/a < 2:
        return []
    while(n > 0):
        if n - decrem >= a:
            ans.insert(0, decrem)
            n -= decrem
        else:
            #decrem -= 1
            
            while(n-decrem < a):
                decrem -= 1
                if n - decrem == 0:
                    ans.insert(0, decrem)
                    return ans
                if(decrem < a):
                    return []
            
            ans.insert(0, decrem)
            ans.insert(0, a)
            n -= a
            return ans
    return ans
    
def rec(n, a, b):
    ans = []
    def helper(n, a, b):
        if n < a:
            return []
        if (a <= n <= b):
            return [n]
        if n/a < 2:
            return []
        else:
            decrem = b
            return [decrem] + helper(n - decrem, a, decrem)

    ans += helper(n, a, b)
    return ans

total = input().split()
n = int(total[0])
a = int(total[1])
b = int(total[2])
ans = sol(n, a, b)
if(len(ans) > 0):
    print("YES")
    for i in ans:
        print(i, end=" ")
else:
    print("NO")
