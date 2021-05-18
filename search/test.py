from wand.image import Image
import os

def organizer(): # creates a dict from words and meaning and appends to already created dict
    k = []
    m = []
    k1 = k.append(input('enter'))

'''
def finder(a, b):
    access = PyPDF2.PdfFileReader(open('AbrahamLincoln.pdf', 'rb'))
    pages = list(range(0, access.numPages))
    print(access.numPages)
    find = access.getPage(4)
    content = find.extractText()


pdf_file = "scanned_apple_10k_snippet.pdf"
    files = []
    with(Image(filename=pdf_file, resolution=500)) as conn:
        for index, image in enumerate(conn.sequence):
            image_name = os.path.splitext(pdf_file)[0] + str(index + 1) + '.png'
            Image(image).save(filename=image_name)
            files.append(image_name)
            
def finder():
    content, form = extract_text('AbrahamLincoln.pdf'), []
    c = open('test.txt', 'w')
    c.write(content.lower())
    c.close()
    for i in open('test.txt', 'r'):
        x = i.split()
        for y in x:
            if y == 'sought':
                start, end, catch = x.index(y), len(x), period(x)
                if catch:
                    end = catch
                else:
                    pass
                print(catch, end)
                r = range(start, end)
                for v in r:
                    form.append(x[v])
    print(form)

s = 'he sought the holding for me. Plus my fam'
b = s.split()
for i in b:
    if i.find('sought') != -1:
        print(b.index(i))
'''
x = 'xmskc. kajnkvk jdsniunj sdjsiu'
print(x.split('.'))