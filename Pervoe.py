a = int(input(
    "Выберите тип операции с матрицой: \n1:Транспонирование матрицы\n2:Умножение матриц\n3:Определение ранга матрицы\n"))
if (a == 1):
    raz = str(input("Введите размер матрицы из предложенных(1х2, 2х1, 1х3, 3х1, 2х2, 3х3):\n"))
    per = int(raz[0])
    vto = int(raz[2])

    ar = [[0] * vto for i in range(per)]

    for i in range(0, per):
        for j in range(0, vto):
            print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
            ar[i][j] = int(input())

    k = [[ar[j][i] for j in range(len(ar))] for i in range(len(ar[0]))]

    print()

    for i in range(0, vto):
        if (i == 0):
            print("Транспонированная матрица:")
        else:
            print()
        for j in range(0, per):
            print(k[i][j], end=" ")

elif (a == 2):
    raz1 = str(input("Введите размер первой матрицы из предложенных(1х2, 2х1, 1х3, 3х1, 2х2, 3х3):\n"))
    per1 = int(raz1[0])
    vto1 = int(raz1[2])
    ar1 = [[0] * vto1 for i in range(per1)]

    for i in range(0, per1):
        for j in range(0, vto1):
            print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
            ar1[i][j] = int(input())

    if (per1==1):
        print("Введите размер второй матрицы из предложенных(",vto1,"x",per1,", ",vto1,"x",vto1,"): ")
        raz2=str(input())
        per2 = int(raz2[0])
        vto2 = int(raz2[2])
        ar2 = [[0] * vto2 for i in range(per2)]

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
        ar2 = [[0] * vto2 for i in range(per2)]

        for i in range(0, per2):
            for j in range(0, vto2):
                print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
                ar2[i][j] = int(input())
    else:
        print("Введите размер второй матрицы из предложенных(", vto1, "x", per1, ", ", vto1, "x 1 ): ")
        raz2 = str(input())
        per2 = int(raz2[0])
        vto2 = int(raz2[2])
        ar2 = [[0] * vto2 for i in range(per2)]

        for i in range(0, per2):
            for j in range(0, vto2):
                print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
                ar2[i][j] = int(input())

    ar = [[0] * vto2 for i in range(per1)]

    for i in range(0, per1):
        for j in range(0, vto2):
            for k in range (0, vto1):
                ar[i][j] += ar1[i][k]*ar2[k][j]

    for i in range(0, per1):
        if (i == 0):
            print("Ваша матрица, полученная из умножения двух матриц:")
        else:
            print()
        for j in range(0, vto2):
            print(ar[i][j], end=" ")

if (a==3):
    raz = str(input("Введите размер матрицы из предложенных(2х2, 3х3):\n"))
    per = int(raz[0])
    vto = int(raz[2])

    ar = [[0] * vto for i in range(per)]

    for i in range(0, per):
        for j in range(0, vto):
            print("Введите элемент матрицы [", i + 1, "][", j + 1, "]: ")
            ar[i][j] = int(input())
    ch=0
    for i in range(0, per):
        for j in range(0, vto):
            if (ar[i][j] == 0):
                ch += 1
    if (ch == per*vto):
        print("Ранг матрицы = 0")
    else:
        if (per==2):
            if ( (ar[0][0]*ar[1][1]-ar[0][1]*ar[1][0]!=0) ):
                print ("Ранг матрицы = 2")
            else:
                print("Ранг матрицы = 1")
        else:
            if ( (ar[0][0]*ar[1][1]*ar[2][2]+ar[1][0]*ar[2][1]*ar[0][2]+ar[0][1]*ar[1][2]*ar[2][0]-ar[0][2]*ar[1][1]*ar[2][0]-ar[0][1]*ar[1][0]*ar[2][2]-ar[2][1]*ar[1][2]*ar[0][0])!=0 ):
                print("Ранг матрицы = 3")
            elif( (ar[0][0]*ar[1][1]-ar[0][1]*ar[1][0])!=0 or (ar[0][1]*ar[1][2]-ar[0][2]*ar[1][1])!=0 or (ar[1][0]*ar[2][1]-ar[1][1]*ar[2][0])!=0 or (ar[1][1]*ar[2][2]-ar[1][2]*ar[2][1])!=0 or (ar[0][0]*ar[2][1]-ar[0][1]*ar[2][0])!=0 or (ar[0][1]*ar[2][2]-ar[0][2]*ar[2][1])!=0 or (ar[0][0]*ar[1][2]-ar[0][2]*ar[1][0])!=0 or (ar[1][0]*ar[2][2]-ar[1][2]*ar[2][0])!=0 ):
                print("Ранг матрицы = 2")
            else:
                print("Ранг матрицы = 1")