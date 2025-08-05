def occurencesInRepeatedString(word: str, n: int, letter: str):

    if not word or n == 0:
        return 0

    wLen = len(word) # O(1)

    if wLen == 0:
        return 0

    word = word.lower() # O(n)
    letter = letter.lower() # O(1)
    repeats = n / wLen # O(1)
    leftOver = n % wLen
    repeatsInOneWord = word.count(letter)   # O(n)
    repeatsInLeftOver = word[:leftOver].count(letter)   # O(n) worst case

    return int((repeats * repeatsInOneWord) + repeatsInLeftOver)


# python 2, use raw_input
word = input("Enter the word: ")
n = int(input("Enter the number of letters repeated in the string: "))
letter = input("Enter the letter you would like counted: ")
print(f"there are {occurencesInRepeatedString(word, n, letter)} occurences of {letter} in {word}")

# "STRAWBERRY", n = 62, r
#   length = 10
#   62/10 = 6 rem 2
#   r = 3 times in 1 word, 3 * 6 = 18
#   2 extra letters st, no r in this

# Overall O(n) time complexity
# Space Complexity = O(n) since storing a new lower case version of the string
# Count is case-sensitive hence we have to store a new lower case string
