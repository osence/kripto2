# Напишите программу генерации совместного ключа методом Диффи-Хеллмана
# Пояснение алгоритма Диффи-Хеллмана
# 1) Генерация простого модуля (Простого числа и малого )
import random

P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 71, 73, 79, 8, 3, 89, 97, 101]


def generatePrime(border):
    n = random.randint(2, border / 2)
    n = 2 * n - 1
    while not isPrime(n):
        n = random.randint(2, border / 2)
        n = 2 * n - 1
    return n


def isPrime(n):
    for elem in P:
        if n % elem == 0:
            if n == elem:
                return True
            else:
                return False
    r = 100000
    return rabinMiller(n, r)


# Генерация двух простых чисел A B


def rabinMiller(n, r):
    b = n - 1
    betta = bin(b)
    k = -1
    while b > 0:
        k += 1
        betta = betta[:k + 2] + str(b % 2) + betta[k + 3:]
        b = b // 2
    for j in range(r):
        a = random.randint(2, n - 1)
        if euclid(a, n)[0] > 1:
            return False
        d = 1
        for i in range(k, -1, -1):
            x = d
            d = d ** 2 % n
            if (d == 1) and not (x == 1) and not (x == n - 1):
                return False
            if betta[i + 2] == 1:
                d = (d * a) % n
        if not d == 1:
            return False
    return True


def euclid(a, b):
    if a == 0:
        return [b, 0, 1]
    else:
        g, x, y = euclid(b % a, a)
        return [g, y - (b // a) * x, x]


def modExp(a, b, n):
    if b == 0:
        return 1
    if b % 2 == 0:
        x = modExp(a, b // 2, n)
        return x ** 2 % n
    x = modExp(a, (b - 1) // 2, n)
    x = x ** 2 % n
    return (a * x) % n


def generateG(border):
    q = generatePrime(2 ** 64)
    n = random.randint(2, border)
    p = n * q + 1
    while not isPrime(p):
        n = random.randint(2, border)
        p = n * q + 1
    a = random.randint(2, p - 1)
    g = modExp(a, n, p)
    while g == 1:
        a = random.randint(2, p - 1)
        g = modExp(a, n, p)
    return [g, q, p]


def deffieHellman(g, x, q, p):
    xx = x % q
    bigx = modExp(g, xx, p)
    return bigx


g, q, p = generateG(2 ** 64)
x = random.randint(1, 2 ** 16)
y = random.randint(1, 2 ** 16)
bigx = modExp(g, x, p)
bigy = modExp(g, y, p)
answerx = modExp(bigy, x, p)
answery = modExp(bigx, y, p)
print('Выбраны случайные числа', x, y)
print('Найденые X и Y ',bigx, bigy)
print('Сверка полученных ответов ', answerx, answery)
