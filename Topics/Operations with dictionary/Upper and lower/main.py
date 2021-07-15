# the list with words from string
# please, do not modify it
some_iterable = input().split()

# use dictionary comprehension to create a new dictionary
dic = {k.upper(): k.lower() for k in some_iterable}

print(dic)
