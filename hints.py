num_set = set()
num_list = []

with open('numbers.txt') as fin:
    for line in fin:
        num_set.add(line.strip())

num_list = sorted(num_set)

with open('output', 'w') as fout:
    for num in num_list:
        print(f'        hint(SIP/{num}) {num} => {{}}', file=fout)
