def countOccurences(word, n, char):

    if not word or n == 0:
        return 0

    wordLen = len(word)

    word = word.lower()
    char = char.lower()

    repeats, extra = divmod(n, wordLen)

    counts = word.count(char)

    if counts == 0:
        return 0

    inRepeats = repeats * counts
    inExtra = word[:extra].count(char)

    return inRepeats + inExtra

print(countOccurences("strawberry", 62, "r"))