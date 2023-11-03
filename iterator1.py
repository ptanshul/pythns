list1 = ["A", "b", "G"]
iter1 = list1.__iter__()
if iter1.isupper():
    print(iter1.__next__())