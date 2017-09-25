# matriz 7,7

Mat = [None] * 7
for i in range(7):
    Mat[i] = [None] * 7

lista = list()

# le o arquivo e pega o mapa
for ln in open("MatrizTeste.txt"):
    ln = ln.split()
    lista.append(ln[0])

# x é para percorrer a lista
x = 0
# preenche matriz com valores lista
for i in range(7):
    for j in range(7):
        Mat[i][j] = lista[x]
        x = x + 1

# printa matriz  formatada
for i in range(7):
    print(Mat[i][:])
