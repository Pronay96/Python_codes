import math
import os
import random
import re
import sys
import collections


def collectionfunc(text1, dictionary1, key1, val1, deduct, list1):

    # Create dict with the count of words in text
    counter_1 = Counter(text1.split(" "))
    my_key = list(counter_1.keys())
    my_key.sort()
    sorted_dict = {key: counter_1[key] for key in my_key}
    print(sorted_dict)

    # Counter object using dict, subtracting deduct from counter object
    counter_2 = Counter(dictionary1)
    for key, value in deduct.items():
        new_val = counter_2[key] - deduct[key]
        counter_2[key] = new_val

    dict_counter = dict(counter_2)
    print(dict_counter)

    # Ordered dict using key1 and val1
    ordered_dict = collections.OrderedDict()
    for it in range(len(key1)):
        ordered_dict[key1[it]] = val1[it]

    # Delete key from ordered_dict using 2nd value from key1
    del ordered_dict[key1[1]]

    # Reinsert the 2nd value from key1 as key and respective value from val1
    ordered_dict[key1[1]] = val1[1]
    print(dict(ordered_dict))

    # Create default dict with 'even', 'odd' as keys
    # Extract the even and odd from the list and store them in the dict to respective keys as list
    lst_odd = []
    lst_even = []
    dict_gen = {}
    for nums in list1:
        if nums % 2 != 0:
            lst_odd.append(nums)
            dict_gen['odd'] = lst_odd
        else:
            lst_even.append(nums)
            dict_gen['even'] = lst_even
    print(dict_gen)


if __name__ == '__main__':
    from collections import Counter

    text1 = input()

    n1 = int(input().strip())
    qw1 = []
    qw2 = []
    for _ in range(n1):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
        qw2_item = int(input().strip())
        qw2.append(qw2_item)
    testdict = {}
    for i in range(n1):
        testdict[qw1[i]] = qw2[i]
    collection1 = (testdict)

    qw1 = []
    n2 = int(input().strip())
    for _ in range(n2):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
    key1 = qw1

    qw1 = []
    n3 = int(input().strip())
    for _ in range(n3):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
    val1 = qw1

    n4 = int(input().strip())
    qw1 = []
    qw2 = []
    for _ in range(n4):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
        qw2_item = int(input().strip())
        qw2.append(qw2_item)
    testdict = {}
    for i in range(n4):
        testdict[qw1[i]] = qw2[i]
    deduct = testdict

    qw1 = []
    n5 = int(input().strip())
    for _ in range(n5):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
    list1 = qw1

    collectionfunc(text1, collection1, key1, val1, deduct, list1)
