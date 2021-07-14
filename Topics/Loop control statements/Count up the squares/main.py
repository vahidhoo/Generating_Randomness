# put your python code here
total_square = 0
total = 0
while True:
    num = int(input())

    total += num
    total_square += num ** 2

    if total == 0:
        print(total_square)
        break
