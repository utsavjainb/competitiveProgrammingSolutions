def max_cost(budget, comp_prices):

    def helper(budget, current_cost, comp_prices, curr_row):
        if curr_row == len(comp_prices) - 1:
            for price in comp_prices[curr_row]:
                if current_cost + price <= budget:
                    return current_cost + price
            return 0

        else:
            compcost = 0
            for price in comp_prices[curr_row]:
                if current_cost + price <= budget:
                    compcost = price
                    ans = helper(budget, current_cost + price, comp_prices, curr_row + 1)

                    #print("ans: " + str(ans))
                    if ans > 0:
                        return ans
                    else:
                        continue
            if compcost == 0:
                return 0


    return helper(budget, 0, comp_prices, 0)


t = int(input())
budgets = []
num_of_comps = []
for i in range(t):
    budget = int(input())
    numcomp = int(input())
    trash = input()
    comp_prices = []
    for j in range(numcomp):
        comp_prices.append(sorted([int(y) for y in input().split()], reverse=True))
    print(max_cost(budget, comp_prices))

