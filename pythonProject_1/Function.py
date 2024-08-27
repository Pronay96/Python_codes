def name_len(lst):
    final = []
    for names in lst:
        if len(names) > 5:
            final.append(names)
    return final


list1 = []
print("Enter a name:")
for i in range(10):
    name = input()
    list1.append(name)
res_final = name_len(list1)

print("Final names:")
for result in res_final:
    print(result)
