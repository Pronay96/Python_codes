def replace_words(sentence, words):
    words1 = words.lower()
    sentence1 = sentence.lower()

    if words1 in sentence1:
        size = len(words)
        new_sentence = sentence1.replace(words1, ("*" * size))
        return new_sentence.capitalize()
    else:
        return False


def main():
    sentence = input("Enter the sentence:\n")
    word = input("Enter the word:\n")

    result = replace_words(sentence, word)

    if result:
        print(result)
    else:
        print("The given word is not found in the sentence")


main()