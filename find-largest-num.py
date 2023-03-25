a = [13, 7, 68, 2, 3, 6, 10, 22, 135, 68686, 8675, 309]
largest = a[0]
for num in a:
    if num > largest:
        largest = num
print(largest)
