def top_ten():  # Generator Function
    num = 1
    while num <= 10:
        val = num
        yield val ** 2
        num += 1


value = top_ten()
for j in value:
    print(j)

