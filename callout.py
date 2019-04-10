with open('numbers.txt') as fin:
    for line in fin:
        a = line.split()
        print('\t\tif (${CALLERID(num)}=%s) {' % a[1])
        print('\t\t\tnum=3452{0};'.format(a[0]))
        print('\t\t\tgoto call;')
        print('\t\t}')
