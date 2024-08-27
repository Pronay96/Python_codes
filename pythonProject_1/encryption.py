def remove_duplicates(sentence):
    list1 = []
    unique_words = sentence.split(" ")
    for i in unique_words:
        if i not in list1:
            list1.append(i)
    return list1


def caesar_cipher(unique_words, key):
    ciphertext = " ".join(unique_words)
    n = ""
    for i in ciphertext:
        if i.isalpha():
            n = n + chr(ord(i) + key)
        else:
            n = n + i
    return n


def main():
    sentence = input("Enter a sentence: ")
    unique_words = remove_duplicates(sentence)
    print("The unique words in the sentence is:", unique_words)

    key = int(input("Enter the key: "))
    ciphertext = caesar_cipher(unique_words, key)
    print("The ciphertext is/are:",ciphertext)

main()
