def tribonacci_iterate(n):
    ans_list = [0,1,1]
    for i in range(100):
        if i <= 2:
            continue
        else:
            ans_list.append(ans_list[i-3]+ans_list[i-2]+ans_list[i-1])
    return ans_list[n]
print(tribonacci_iterate(89))