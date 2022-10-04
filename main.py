import numpy as np
a = int(input("Выберите тип операции с матрицой: \n1:Транспонирование матрицы\n2:Умножение матриц\n3:Определение ранга матрицы\n"))
if (a == 1):
    raz = str(input("Введите размер матрицы из предложенных(1х2, 2х1, 1х3, 3х1, 2х2, 3х3):\n"))
    per = int(raz[0])
    vto = int(raz[2])

    ar = np.array([[0] * vto for i in range(per)])

    for i in range(0, per):
        for j in range(0, vto):
            print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
            ar[i][j] = int(input())

    ar_transp = ar.transpose()

    print("Транспонировання матрица:\n", ar_transp)
elif (a == 2):
    raz1 = str(input("Введите размер первой матрицы из предложенных(1х2, 2х1, 1х3, 3х1, 2х2, 3х3):\n"))
    per1 = int(raz1[0])
    vto1 = int(raz1[2])
    ar1 = np.array([[0] * vto1 for i in range(per1)])

    for i in range(0, per1):
        for j in range(0, vto1):
            print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
            ar1[i][j] = int(input())

    if (per1==1):
        print("Введите размер второй матрицы из предложенных(",vto1,"x",per1,", ",vto1,"x",vto1,"): ")
        raz2=str(input())
        per2 = int(raz2[0])
        vto2 = int(raz2[2])
        ar2 = np.array([[0] * vto2 for i in range(per2)])

        for i in range(0, per2):
            for j in range(0, vto2):
                print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
                ar2[i][j] = int(input())

    elif (vto1==1):
        if (per1==3):
            print("Введите размер второй матрицы из предложенных(", vto1, "x", per1, ", ", vto1, "x", per1-1, "): ")
        else:
            print("Введите размер второй матрицы из предложенных(", vto1, "x", per1, ", ", vto1, "x", per1+1, "): ")
        raz2 = str(input())
        per2 = int(raz2[0])
        vto2 = int(raz2[2])
        ar2 = np.array([[0] * vto2 for i in range(per2)])

        for i in range(0, per2):
            for j in range(0, vto2):
                print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
                ar2[i][j] = int(input())
    else:
        print("Введите размер второй матрицы из предложенных(", vto1, "x", per1, ", ", vto1, "x 1 ): ")
        raz2 = str(input())
        per2 = int(raz2[0])
        vto2 = int(raz2[2])
        ar2 = np.array([[0] * vto2 for i in range(per2)])

        for i in range(0, per2):
            for j in range(0, vto2):
                print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
                ar2[i][j] = int(input())

    ar = [[0] * vto2 for i in range(per1)]

    ar_proiz = ar1.dot(ar2)
    print("Ваша матрица, полученная из умножения двух матриц:\n", ar_proiz )

if (a==3):
    raz = str(input("Введите размер матрицы из предложенных(2х2, 3х3):\n"))
    per = int(raz[0])
    vto = int(raz[2])

    ar = np.array([[0] * vto for i in range(per)])

    for i in range(0, per):
        for j in range(0, vto):
            print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
            ar[i][j] = int(input())
    print("Ранг матрицы =", np.linalg.matrix_rank(ar, tol=None))