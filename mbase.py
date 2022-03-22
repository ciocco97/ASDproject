from subset import Subset


def mbase():
    sub1 = Subset(2, 3, 5)
    sub2 = Subset(2, 3, 7)
    print(sub1)
    print(sub1.compare(sub2))
    print(sub2.max())
