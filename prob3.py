from functools import reduce
numbers = [23, 92, 7, 20, 434, 23]
find_max_lambda = lambda x, y: x if x > y else y



def find_max(numbers, func):
    max_num = numbers[0]
    return reduce(func, numbers)


print(find_max(numbers, find_max_lambda))
