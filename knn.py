# coding=utf-
import math

from tabulate import tabulate


def maior(a, b, c):
    if a >= b and a > c:
        return a
    elif b >= c:
        return b
    else:
        return c


def calc_dist(value1, value2):
    return math.sqrt(((value1[0] - value2[0]) ** 2 + value1[1] - value2[1]) ** 2 + (value1[2] - value2[2]) ** 2 + (
            value1[3] - value2[3]) ** 2)


def read_file(file_name):
    lista = []
    file = open(file_name)
    for lineNumber, linha in enumerate(file):
        number = lineNumber - 1
        if lineNumber > 0:
            lista.append(linha.split(','))
            for i in range(0, 4):
                lista[number][i] = float(lista[number][i])
            if 'Setosa' in lista[number][4]:
                lista[number][4] = 'Setosa'
            elif 'Versicolor' in lista[number][4]:
                lista[number][4] = 'Versicolor'
            elif 'Virginica' in lista[number][4]:
                lista[number][4] = 'Virginica'
    file.close()
    return lista;


def search_k_menores(value, data, k_val):
    smallers = []

    while k_val > 0:
        menor = 0
        for i in range(len(data)):
            if (i not in smallers) and calc_dist(value, data[menor]) > calc_dist(value, data[i]):
                menor = i
        k_val += -1
        smallers.append(menor)
    return smallers


def this_class(smallers_values, data):
    count_a = 0
    count_b = 0
    count_c = 0
    for i in smallers_values:
        if 'Setosa' in data[i][4]:
            count_a += 1
        elif 'Versicolor' in data[i][4]:
            count_b += 1
        else:
            count_c += 1
    if maior(count_a, count_b, count_c) == count_a:
        return 'Setosa'
    elif maior(count_a, count_b, count_c) == count_b:
        return 'Versicolor'
    else:
        return 'Virginica'


def imprime(class_a, class_b, class_c, k_value):
    sumA = class_a[1] + class_a[2] + class_a[3]
    sumB = class_b[1] + class_b[2] + class_b[3]
    sumC = class_c[1] + class_c[2] + class_c[3]
    print('Matrix of confusion')
    print(tabulate([class_a, class_b, class_c], headers=[' ', 'Setosa', 'Versicolor', 'Virginica']))
    print('')
    print('')
    print('Statistics for K =', k_value)
    if class_a[1] > 0:
        print('{:.2f}% of Setosas were classified correctly'.format((class_a[1] * 100) / sumA))
    if class_b[2] > 0:
        print('{:.2f}% das Versicolors were classified correctly'.format((class_b[2] * 100) / sumB))
    if class_c[3] > 0:
        print('{:.2f}% das Virginicas were classified correctly'.format((class_c[3] * 100) / sumC))
    print('')

    if class_a[2] > 0:
        print('{:.2f}% of Setosas were classified as Versicolors'.format((class_a[2] * 100) / sumA))
    if class_b[1] > 0:
        print('{:.2f}% of Versicolors were classified as Setosas'.format((class_b[1] * 100) / sumB))
    if class_c[1] > 0:
        print('{:.2f}% of Virginicas were classified as Setosas'.format((class_c[1] * 100) / sumC))

    print('')

    if class_a[3] > 0:
        print('{:.2f}% of Setosas were classified as Virginicas'.format((class_a[3] * 100) / sumA))
    if class_b[3] > 0:
        print('{:.2f}% of Versicolors were classified as Virginicas'.format((class_b[3] * 100) / sumB))
    if class_c[2] > 0:
        print('{:.2f}% of Virginicas were classified as Versicolors'.format((class_c[2] * 100) / sumC))


print('Enter the value of K:')
k = int(input())
menores = []
treinamento = read_file('iris_treino.csv')
teste = read_file('iris_test.csv')
setosa = ['Setosa', 0, 0, 0]
versicolor = ['Versicolor', 0, 0, 0]
virginica = ['Virginica', 0, 0, 0]
for line, inst in enumerate(teste):
    menores = search_k_menores(teste[line], treinamento, k)
    classIris = this_class(menores, treinamento)

    if inst[4] == 'Setosa':
        if classIris == 'Setosa':
            setosa[1] += 1
        elif classIris == 'Versicolor':
            setosa[2] += 1
        elif classIris == 'Virginica':
            setosa[3] += 1
    elif inst[4] == 'Versicolor':
        if classIris == 'Setosa':
            versicolor[1] += 1
        elif classIris == 'Versicolor':
            versicolor[2] += 1
        elif classIris == 'Virginica':
            versicolor[3] += 1
    elif inst[4] == 'Virginica':
        if classIris == 'Setosa':
            virginica[1] += 1
        elif classIris == 'Versicolor':
            virginica[2] += 1
        elif classIris == 'Virginica':
            virginica[3] += 1

imprime(setosa, versicolor, virginica, k)
