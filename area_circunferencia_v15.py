#!/usr/local/bin/python3
from math import pi
import sys

ERRO = '\033[91m'
NORMAL = '\033[0m'


def help():
    print('É necessário informar o raio do círculo.')
    print('Sintaxe: {} <raio>'.format(sys.argv[0][2:]))


def circulo(raio):
    return pi * float(raio) ** 2


if __name__ == '__main__':
    if len(sys.argv) < 2:

        help()
        # sys.exit(errno.EPERM)
    elif not sys.argv[1].isnumeric():
        help()
        print(ERRO, 'O raio deve ser um valor numérico', NORMAL)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('Area do círculo', area)
