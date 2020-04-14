words = []

for i in range(0,5):
    word = input("Enter a word: ")
    count = 0
    for j in range(0,len(word)):
        if (word[j] == word[0]):
            count += 1

    if (count > 1):
        words.append(word)
    print("")

print(words)
