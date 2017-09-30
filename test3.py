a = list()
a.append((1, 2, 3, 4, 5, 6))
a.append((2, 2, 2, 2, 2, 2))
a.append((1, 1, 1, 1, 1, 1))
a.append((3, 3, 3, 3, 3, 3))
a.append((1, 1, 2, 2, 2, 2))

b = (1, 2, 1, 1, 1, 1)

for i in a:
    if(b[0] == i[0] and b[1] == i[1]):
        print("Assooo mizeravi")
    else:
        print("Nope")
