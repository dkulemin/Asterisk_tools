with open('extensions.ael') as fin, open('output.txt', 'w') as fout:
    spaces = '        '
    tabs = 0
    switch_block = False
    for line in fin:
        if line.strip() == '}' or line.strip() == '};':
            fout.write(spaces * (tabs - 1) + line.strip() + '\n')
            tabs -= 1
        else:
            fout.write(spaces * tabs + line.strip() + '\n')
            if '{' in line or '}' in line:
                if line.count('{') > line.count('}'):
                    tabs += 1
                elif line.count('{') < line.count('}'):
                    tabs -= 1

'''            
            if switch_block:
                if line.strip() == '}' or line.strip() == '};':
                    fout.write(spaces * tabs + line.strip() + '\n')
                    tabs -= 1
                elif 'pattern' in line or 'case' in line or 'default' in line:
                    fout.write(spaces * tabs + line.strip() + '\n')
                    switch_block = not switch_block
                else:
                    fout.write(spaces * (tabs + 1) + line.strip() + '\n')
                    if '{' in line or '}' in line:
                        if line.count('{') > line.count('}'):
                            tabs += 1
                        elif line.count('{') < line.count('}'):
                            tabs -= 1
            else:
                if line.strip() == '}' or line.strip() == '};':
                    fout.write(spaces * (tabs - 1) + line.strip() + '\n')
                    tabs -= 1
                else:
                    fout.write(spaces * tabs + line.strip() + '\n')
                    if '{' in line or '}' in line:
                        if line.count('{') > line.count('}'):
                            tabs += 1
                        elif line.count('{') < line.count('}'):
                            tabs -= 1
                    elif 'pattern' in line or 'case' in line or 'default' in line:
                        switch_block = not switch_block

'''

'''
            if line.strip() == '}' or line.strip() == '};':
                fout.write(spaces * (tabs - 1) + line.strip() + '\n')
                tabs -= 1
            else:
                if switch_block:
                    if 'pattern' in line or 'case' in line or 'default' in line:
                        fout.write(spaces * tabs + line.strip() + '\n')
                        switch_block = not switch_block
                    else:
                        fout.write(spaces * (tabs + 1) + line.strip() + '\n')
                        if '{' in line or '}' in line:
                            if line.count('{') > line.count('}'):
                                tabs += 1
                            elif line.count('{') < line.count('}'):
                                tabs -= 1
                else:
                    fout.write(spaces * tabs + line.strip() + '\n')
                    if '{' in line or '}' in line:
                        if line.count('{') > line.count('}'):
                            tabs += 1
                        elif line.count('{') < line.count('}'):
                            tabs -= 1
                    elif 'pattern' in line or 'case' in line or 'default' in line:
                        switch_block = not switch_block
'''