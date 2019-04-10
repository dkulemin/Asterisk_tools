import json


output = []
with open('phones.txt') as fin:
    for line in fin:
        num, mac = line.split()
        output.append({"Name": num,
                       "Password": "Hgls!Qud_" + num,
                       "MAC": mac,
                       "Type": "yealink",
                       "Config": "/etc/phones.d/T23G/001565c45457.cfg"})
with open('phones_out.txt', 'w') as fout:
    print('[', file=fout)
    for i in output[:-1]:
        print('\t', i, end=',\n', file=fout)
    print('\t', output[-1], file=fout)
    print(']', file=fout)

print(output)
#print(json.dump(output))
