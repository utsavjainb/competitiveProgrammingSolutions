def lexicoSmallestPermuatation(arr, n_set): 
    last_inserted = 0
    while len(n_set) > 0:
        min_num = min(n_set)
        n_set.remove(min(n_set))
        if min_num == 1:
            arr.insert(0, 1)
            continue
        
        for x in range(last_inserted, len(arr)):
            if arr[x] > min_num:
                arr.insert(x, min_num)
                last_inserted = x
                break
        else:
            arr.append(min_num)
    return arr
        
        
        
inp = input().split()
n = inp[0]
m = inp[1]
x = int(n) + int(m)
nlist = [int(y) for y in input().split()]
mlist = set([int(y) for y in input().split()])
arr = lexicoSmallestPermuatation(nlist, mlist)
for i in arr:
    print(i, end = " ")