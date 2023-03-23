def set_remove(x):
    print(list(set(x)))

def loop_remove(x):
    new_list = []
    for i in x:
        if i not in new_list:
            new_list.append(i)
    print(new_list)

def main():
    a = [1, 2, 1, 3, 4, 3, 8, 9, 1, 2, 3, 7, 6]
    set_remove(a)
    loop_remove(a)

if __name__ == "__main__":
    main()