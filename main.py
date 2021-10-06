'''
Returneaza true daca n este prim si false daca nu.
'''

import math


def is_prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


'''
Returneaza produsul numerelor din lista lst.
'''


def get_product(lst):
    produs = 1
    for numar in lst:
        produs = produs * numar
    return produs

'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''


def get_cmmdc(x, y):
  if x == 0:
    return y
  if y == 0:
    return x

  if x == y:
    return x

  if x > y:
    return get_cmmdc(x - y, y)
  return get_cmmdc(x, y - x)

'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''





def main():
    print(is_prime(13))
    print(get_product([1, 2, 3]))
    print(get_cmmdc(72, 14))
    print(get_cmmdc(25, 100))


if __name__ == '__main__':
    main()