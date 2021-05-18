from pdfminer.high_level import extract_text
import linecache


form = []

def criterion():  # defines search requirements
    a, b = input('enter search'), input('enter class')
    finder(a, b)


def pre():  # defines class for search
    content = extract_text('AbrahamLincoln.pdf')
    c = open('test.txt', 'w')
    c.write(content.lower())
    c.close()


def period(x):  # locates periods
    for i in x:
        if i.find('.') != -1:
            end = x.index(i) + 1
            return end

def compiler(x):
    with open('sum.txt', 'w') as f:
        content = ' '.join(x)
        new = content.split('.')
        print(new)
        for i in new:
            f.write(i + '\n')
    f.close()

def finder():
    search = 'birth'
    pre()
    filter()
    with open('test.txt', 'r') as file:
        for num, i in enumerate(file, 1):
            x = i.split()
            for y in x:
                if y.find(search) != -1:
                    if period(i.split()) is not None:
                        start, end = x.index(y), period(x)
                        r = range(start, end)
                        for v in r:
                            form.append(x[v])
                    else:
                        start, end = x.index(y), len(x)
                        r = range(start, end)
                        for v in r:
                            form.append(x[v])
                        check(num)
    compiler(form)

def check(num):
    x = linecache.getline('test.txt', num + 1)
    y = x.split()
    if period(y) is not None:
        start, end = 0, period(y)
        r = range(start, end)
        for v in r:
            form.append(y[v])
    else:
        form.append(x)



def filter():
    with open("test.txt") as f:
        c = ("".join(line for line in f if not line.isspace()))
    with open("test.txt", 'w') as e:
        e.write(c)


if __name__ == '__main__':
    finder()
