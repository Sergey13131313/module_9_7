def is_prime(func):
    def wrapper(*args):
        f = func(*args)
        out_str = 'Простое'
        for i in reversed(range(2, f)):
            if f % i == 0:
                out_str = 'Составное'
                break
        print(out_str)
    return wrapper


@is_prime
def sum_three(*args):
    result = 0
    for x in args:
        result += x
    return result


sum_three(2, 3, 5)

