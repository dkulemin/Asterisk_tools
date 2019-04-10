with open('sccp_extensions.txt', encoding='utf8') as fin, open('output', 'w', encoding='utf8') as fout:
    dict = {}
    id = 0
    for line in fin:
        if 'id =' in line:
            id = line.strip('id =').split()[-1]
            #print(id)
        if 'cid_name =' in line:
            dict[id] = ' '.join(line.strip('cid_name =').split())
    for key, value in dict.items():
        fout.write(f'{key} {value}\n')

