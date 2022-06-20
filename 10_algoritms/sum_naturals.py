def sum_natural_for(n):
    sum_num = 0

    for i in range(1, n + 1):
        sum_num += i

    return sum_num


def sum_natural_while(n):
    sum_num = 0

    while n >= 1:
        sum_num += n
        n -= 1

    return sum_num


def sum_natural_recurtion(n):
    if n == 1:
        return 1
    return n + sum_natural_recurtion(n - 1)

print(sum_natural_recurtion(10))