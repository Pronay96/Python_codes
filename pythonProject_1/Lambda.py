from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

evens = list(filter(lambda n: n % 2 == 0, lst))

double = list(map(lambda n: n*2, evens))

sum_all = reduce(lambda a, b: a+b, double)

print(evens)
print(double)
print(sum_all)
