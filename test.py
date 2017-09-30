ranking = list()
ranking .append((6, 10, 5))
ranking.append((5, 10, 8))
ranking.append((7, 9, 3))
ranking.append((60, 10121, 10))

order = list()

order.append((7, 2))
order.append((7, 10))
order.append((5, 10))

a = order[2][0]
b = order[2][1]

x = tuple((a, b))

print(ranking[1])


def Verifica(L1, L2, i):

    for j in range(len(L2)):
        a = L1[i][0]
        b = L1[i][1]
        x = tuple((a, b))
        print(x)
        if(set(x).issubset(L2[j])):
            return True


print(Verifica(order, ranking, 2))
