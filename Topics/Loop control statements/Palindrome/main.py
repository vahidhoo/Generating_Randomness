word = input()
palindrome = True

if len(word) % 2 != 0:
    palindrome = False
else:

    negative_index = -1
    for i in range(0, int(len(word) / 2)):
        if word[i] != word[negative_index]:
            palindrome = False
            break
        negative_index -= 1

if palindrome:
    print('Palindrome')
else:
    print('Not palindrome')
