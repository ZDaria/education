def better_fib(n):
    if n >= 0 and n <= 1:
        return n
    else:
        fib = [0, 1]
        for i in range(2, n + 1):
            fib.append(fib[i - 1] + fib[i - 2])
        return fib[n]


print(better_fib(10))


def get_fibs_value():
    list_var = [0, 1, 1]
    while list_var[-1] + list_var[-2] < 4000000:
        list_var.append(list_var[-1] + list_var[-2])
    return list_var


print(sum(i for i in get_fibs_value() if i % 2 == 0))


def simple(i):
    result = 0
    for n in range(1, i):
        if n % 3 == 0 or n % 5 == 0:
            result += n
    print(result)
    return result


def sum_of_n(n):
    return int((n / 2) * (n + 1))


def main(n):
    a = len(set(i for i in range(1, n) if i % 3 == 0))
    b = len(set(i for i in range(1, n) if i % 5 == 0))
    c = len(set(i for i in range(1, n) if i % 15 == 0))
    print(a, b, c)
    result = 3 * sum_of_n(a) + 5 * sum_of_n(b) - 15 * sum_of_n(c)
    print(result)
    return result


n = 35
a = simple(n)
b = main(n)
