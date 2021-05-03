import pandas as pd


def access():
    a = pd.read_csv('dbk.csv')
    b = a['words']
    c = a['meaning']
    return b, c


if __name__ == '__main__':
    #access()
    n = access()
    print(n)