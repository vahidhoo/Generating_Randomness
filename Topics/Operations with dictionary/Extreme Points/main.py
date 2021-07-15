# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
vals = test_dict.values()

min_val = min(vals)
max_val = max(vals)

min_key = ''
max_key = ''
for k, v in test_dict.items():
    if v == min_val:
        min_key = k
    if v == max_val:
        max_key = k

print('min: {}'.format(min_key))
print('max: {}'.format(max_key))
