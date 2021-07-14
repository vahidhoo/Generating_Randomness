# the list "walks" is already defined
# your code here
avg_per_day = sum(x['distance'] for x in walks) // len(walks)

print(avg_per_day)
