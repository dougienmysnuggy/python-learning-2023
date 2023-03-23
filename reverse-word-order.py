def get_user_input():
    return input('Type a sentence: ')

def main():
    words = get_user_input().split()
    backwords_sentence = words[::-1]
    print(" ".join(backwords_sentence))

if __name__ == "__main__":
    main()