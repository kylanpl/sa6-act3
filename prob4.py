l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [2, 4, 6, 8, 10, 12, 14, 16]

l3 = list(filter(lambda x : x in l2, l1))
print(l3)