import random

input_digits = ""

print('Please give AI some data to learn...')
print('The current data length is 0, 100 symbols left')

MAX_LENGTH = 100
test_string = ''
while len(input_digits) <= MAX_LENGTH:
    print("Print a random string containing 0 or 1:")
    print()
    digits = input()

    for d in digits:
        if d in ('0', '1'):
            input_digits += d

    if len(input_digits) >= MAX_LENGTH:
        print()
        print('Final data string:')
        print(input_digits)

        print()


        break
    else:
        print('Current data length is {}, {} symbols left'.format(len(input_digits), MAX_LENGTH - len(input_digits)))

keys = ['000', '001', '010', '011', '100', '101', '110', '111']
binary_dict = dict.fromkeys(keys)

for k in keys:
    index = -1
    zero = 0
    one = 0
    while True:
        index = input_digits.find(k + '0', index + 1)

        if index == -1:
            break
        zero += 1

    while True:
        index = input_digits.find(k + '1', index + 1)

        if index == -1:
            break
        one += 1

    r = '{},{}'.format(zero, one)
    binary_dict[k] = r

print("""You have $1000. Every time the system successfully predicts your next press, you lose $1.\n
Otherwise, you earn $1. Print "enough" to leave the game. Let's go!
""")

total_dollar = 1000
while True:
    print('Print a random string containing 0 or 1:')
    test_string = input()
    if test_string == 'enough':
        print('Game over!')
        break
    if len(test_string) == 0:
        continue

    continue_flag = False
    for ch in test_string:
        if ch not in ['0', '1']:
            continue_flag = True

    if continue_flag:
        print()
        continue

    start_idx = 0
    end_idx = 3

    predict_string = str(random.randint(0, 1)) + str(random.randint(0, 1)) + str(random.randint(0, 1))
    while end_idx < len(test_string):
        pattern = test_string[start_idx:end_idx]
        result = str(binary_dict[pattern]).split(',')
        zero = int(result[0])
        one = int(result[1])

        zero_prob = zero / (zero + one)
        one_prob = one / (zero + one)

        predict = str(random.randint(0, 1))
        if zero_prob > one_prob:
            predict = '0'
        elif zero_prob < one_prob:
            predict = '1'

        predict_string += predict

        start_idx += 1
        end_idx += 1

    print('prediction:')
    print(predict_string)

    current_predict = 0
    for i in range(3, len(test_string)):
        if test_string[i] == predict_string[i]:
            total_dollar -= 1
            current_predict += 1
        else:
            total_dollar += 1

    acc = round((current_predict / (len(test_string) - 3)) * 100, 2)

    print()
    print('Computer guessed right {} out of {} symbols ({} %)'.format(current_predict, len(test_string) - 3, acc))
    print('Your capital is now ${}'.format(total_dollar))
    print()
