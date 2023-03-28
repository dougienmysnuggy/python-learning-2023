def find_max(a):
    largest = a[0]
    for num in a:
        if num > largest:
            largest = num
    return largest