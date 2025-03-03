def unique_vowels(word):
    stack = []
    vowels = "aerio"

    for char in word.lower():
        if char in vowels and char not in stack:
            stack.append(char)

    print("unique vowels are as :","".join(stack))

word=input("Enter a word :  ")
unique_vowels(word)