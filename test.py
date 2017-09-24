if __name__ == "__main__":
    tamanho = 5
    mapa = [[None] * tamanho for _ in range(tamanho)]

    class elementos(object):

        def __init__(self, crd_x, crd_y, peso):
            self.x = crd_x
            self.y = crd_y
            self.peso = peso

        def pega_peso(self, peso):
            return self.peso

        def __str__(self):
            return self.x, self.y, self.peso

    red = list()

    print("x", 10, "y", 20, "peso", 30)

    red.append(elementos(1, 2, 4))
    red.append(elementos(2, 1, 2))
    red.append(elementos(5, 1, 1))

    print(red[1].pega_peso)
