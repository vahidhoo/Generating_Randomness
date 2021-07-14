input_str = input()
ll = [w.lower() for w in input_str.split(' ')]
input_dict = {w: ll.count(w) for w in ll}

for k, v in input_dict.items():
    print('{} {}'.format(k, v))
