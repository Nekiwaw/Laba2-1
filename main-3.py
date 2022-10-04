import timeit
import numpy as np
def Obrat():
    print("Нахождение обратной матрицы (3x3) вручную:")
    ar = [[0] * 3 for i in range(3)]

    for i in range(0, 3):
        for j in range(0, 3):
            print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
            ar[i][j] = int(input())
    start = timeit.default_timer()
    opred = (ar[0][0] * ar[1][1] * ar[2][2] + ar[1][0] * ar[2][1] * ar[0][2] + ar[0][1] * ar[1][2] * ar[2][0] - ar[0][
        2] * ar[1][1] * ar[2][0] - ar[0][1] * ar[1][0] * ar[2][2] - ar[2][1] * ar[1][2] * ar[0][0])

    if (opred == 0):
        print("Обратной матрицы не существует")
    else:
        ar_minor = [[0] * 3 for i in range(3)]
        ar_minor[0][0] = ar[1][1] * ar[2][2] - ar[1][2] * ar[2][1]
        ar_minor[0][1] = -(ar[1][0] * ar[2][2] - ar[1][2] * ar[2][0])
        ar_minor[0][2] = ar[1][0] * ar[2][1] - ar[1][1] * ar[2][0]
        ar_minor[1][0] = -(ar[0][1] * ar[2][2] - ar[0][2] * ar[2][1])
        ar_minor[1][1] = ar[0][0] * ar[2][2] - ar[0][2] * ar[2][0]
        ar_minor[1][2] = -(ar[0][0] * ar[2][1] - ar[0][1] * ar[2][0])
        ar_minor[2][0] = ar[0][1] * ar[1][2] - ar[0][2] * ar[1][1]
        ar_minor[2][1] = -(ar[0][0] * ar[1][2] - ar[0][2] * ar[1][0])
        ar_minor[2][2] = ar[0][0] * ar[1][1] - ar[0][1] * ar[1][0]

        ar_trasp = [[ar_minor[j][i] for j in range(len(ar_minor))] for i in range(len(ar_minor[0]))]

        ar_obrat = ar_trasp

        stop = timeit.default_timer()
        execution_time = stop - start

        if (opred == 1 or opred == -1):
            for i in range(0, 3):
                if (i == 0):
                    print("Обратная матрица:")
                else:
                    print()
                for j in range(0, 3):
                    print(ar_obrat[i][j] * opred, end=" ")
        else:
            for i in range(0, 3):
                if (i == 0):
                    print("Обратная матрица:")
                else:
                    print()
                for j in range(0, 3):
                    if (i == 1 and j == 0):
                        print("1 /", opred, "* (", ar_obrat[i][j], end=" ")
                    elif (j == 0 and i != 1):
                        print("        (", ar_obrat[i][j], end=" ")
                    elif (j == 2):
                        print(ar_obrat[i][j], ")", end=" ")
                    else:
                        print(ar_obrat[i][j], end=" ")
    print("\nВремя нахождения обратной матрицы =", (execution_time) * 1000, "ms\n")
    print("Нахождение обратной матрицы (3x3) с помощью библиготеки Numpy:\n")

    start = timeit.default_timer()

    ar_obratn = np.linalg.inv(ar)

    stop = timeit.default_timer()
    execution_time = stop - start

    print("Обратная матрица:\n", ar_obratn)

    print("\nВремя нахождения обратной матрицы =", (execution_time) * 1000, "ms")
Obrat()