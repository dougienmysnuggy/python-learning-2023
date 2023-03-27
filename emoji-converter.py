def emoji_message(message):
    emojis = {
        ":)": "😃",
        ":(": "😥"
    }
    new_message = ''
    message = message.split(' ')
    for word in message:
        new_message += emojis.get(word, word) + ' '
    return new_message


sample_text = "Hi :("
print(emoji_message(sample_text))