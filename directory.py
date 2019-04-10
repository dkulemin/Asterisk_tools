with open('sccp_extensions.txt', encoding='utf8') as fin:
    with open('output', 'w', encoding='utf8') as fout:
        ids = []
        labels = []
        for line in fin:
            if 'id =' in line:
                ids.append(line.split()[-1])
            if 'cid_name =' in line:
                tmp = line.strip('cid_name =').split()
                labels.append(', '.join(tmp))
        #print(ids)
        #print(labels)
        for name, number in zip(labels, ids):
            print('<DirectoryEntry>', file=fout)
            print(f'<Name>{name}</Name>', file=fout)
            print(f'<Telephone>{number}</Telephone>', file=fout)
            print('</DirectoryEntry>\n', file=fout)
