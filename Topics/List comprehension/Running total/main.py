input_digits = [int(x) for x in input()]

cumulative = []
index = -1

for i in input_digits:
    sum_count = 0
    if index >= 0:
        sum_count += cumulative[index]

    sum_count += i
    cumulative.append(sum_count)
    index += 1

print(cumulative)
