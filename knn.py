# coding=utf-
import math

from tabulate import tabulate


# Retorna o maior valor entre 3 variavies
def maior(a, b, c):
    if (a >= b and a > c):
        return a
    elif (b >= c):
        return b
    else:
        return c


# Calcula a distancia euclidiana entre 2 valores
def calcDist(value1, value2):
    # print value1,value2
    return math.sqrt(((value1[0] - value2[0]) ** 2 + value1[1] - value2[1]) ** 2 + (value1[2] - value2[2]) ** 2 + (
                value1[3] - value2[3]) ** 2)


# Retorna uma lista com todas os valores do arquivo

def readFile(fileName):
    lista = []
    file = open(fileName)
    for lineNumber, line in enumerate(file):
        number = lineNumber - 1
        if lineNumber > 0:
            # Converte os valores de string pra float
            # Último valor por causa do split pega o \n (ex: "Setosa"\n =: 'Setosa')
            lista.append(line.split(','))
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


# Retorna uma lista com os K menores distancias euclidianas da lista
def searchKMenores(value, data, k):
    menores = []
    distances = []

    while k > 0:
        menor = 0
        for i in range(len(data)):
            if ((i not in menores) and calcDist(value, data[menor]) > calcDist(value, data[i])):
                menor = i
        k += -1
        menores.append(menor)
    return menores


# classA = [classA-Correct, classB-incorrect, classC-incorrect]
# Retorna a classe do objeto baseado nos menores valores
def thisClass(menores, data):
    countA = 0
    countB = 0
    countC = 0
    for i in menores:
        if 'Setosa' in data[i][4]:
            countA += 1
        elif 'Versicolor' in data[i][4]:
            countB += 1
        else:
            countC += 1
    if maior(countA, countB, countC) == countA:
        return 'Setosa'
    elif maior(countA, countB, countC) == countB:
        return 'Versicolor'
    else:
        return 'Virginica'


def imprime(classA, classB, classC, k):
    sumA = classA[1] + classA[2] + classA[3]
    sumB = classB[1] + classB[2] + classB[3]
    sumC = classC[1] + classC[2] + classC[3]
    print('Matriz de confusão')
    print(tabulate([classA, classB, classC], headers=[' ', 'Setosa', 'Versicolor', 'Virginica']))
    print('')
    print('')
    print('Estatisticas para K =', k)
    if (classA[1] > 0):
        print('{:.2f}% das Setosas foram classificadas corretamente'.format((classA[1] * 100) / sumA))
    if (classB[2] > 0):
        print('{:.2f}% das Versicolors foram classificadas corretamente'.format((classB[2] * 100) / sumB))
    if (classC[3] > 0):
        print('{:.2f}% das Virginicas foram classificadas corretamente'.format((classC[3] * 100) / sumC))
    print('')

    if (classA[2] > 0):
        print('{:.2f}% das Setosas foram classificadas como Versicolors'.format((classA[2] * 100) / sumA))
    if (classB[1] > 0):
        print('{:.2f}% das Versicolors foram classificadas como Setosas'.format((classB[1] * 100) / sumB))
    if (classC[1] > 0):
        print('{:.2f}% das Virginicas foram classificadas como Setosas'.format((classC[1] * 100) / sumC))

    print('')

    if (classA[3] > 0):
        print('{:.2f}% das Setosas foram classificadas como Virginicas'.format((classA[3] * 100) / sumA))
    if (classB[3] > 0):
        print('{:.2f}% das Versicolors foram classificadas como Virginicas'.format((classB[3] * 100) / sumB))
    if (classC[2] > 0):
        print('{:.2f}% das Virginicas foram classificadas como Versicolors'.format((classC[2] * 100) / sumC))


# MAIN
print('Digite o valor de K:')
k = int(input())
menores = []
treinamento = readFile('iris_treino.csv')
teste = readFile('iris_test.csv')
setosa = ['Setosa', 0, 0, 0]
versicolor = ['Versicolor', 0, 0, 0]
virginica = ['Virginica', 0, 0, 0]
for line, inst in enumerate(teste):
    menores = searchKMenores(teste[line], treinamento, k)
    classIris = thisClass(menores, treinamento)

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
