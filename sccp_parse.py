with open('sccp.conf') as file, open('out.txt', 'w', encoding='utf-8') as out:
    out.writelines('Номер,Подпись\n')
    for f in file:
        # print(','.join(f.split(' ')), end='')
        A = f.strip().split(' = ')
        if A[0] == 'id':
            print(A[1], end=',')
            out.write(A[1] + ',')
        if A[0] == 'label':
            print(A[1])
            out.write(A[1] + '\n')
