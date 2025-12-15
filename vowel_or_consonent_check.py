vowel = ["A","E","I","O","U"]
letter = input("Enter a letter: ").capitalize()
if letter in vowel:
    print("The letter is vowel.")
else:
    print("The letter is consonant.")