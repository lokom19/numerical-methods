tempx = [0 for _ in range(len(A[i]))]
e = float(input('Введите эпсилон: '))
x = [0 for i in range(0, len(A))]
flag = True

while flag == True:
    for i in range(len(A)):
        tempx[i] = B1[i]
        for j in range(len(A[i])):
            if i != j:
                tempx[i] -= A[i][j] * x[j]
        try:
            tempx[i] /= A[i][i]
            print(A[i][i])
        except ZeroDivisionError:
            continue
            # tempx[i]/=A[i][i]
        # print(tempx[i])
    norm = abs(x[0] - tempx[0])
    for k in range(len(A)):
        if abs(x[k] - tempx[k]) < e:
            # print(f' Модуль: {x[k]-tempx[k]}')
            flag = False
        x[k] = tempx[k]

print(x)