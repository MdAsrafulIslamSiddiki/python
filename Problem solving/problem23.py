def minion_game(string):
    consonent = 0
    vowel = 0

    for i in range(len(string)):
        if string[i] in 'AEIOU':
            vowel = vowel + (len(string)-i)
        else: 
            consonent = consonent + (len(string)-i)
    if consonent > vowel:
        print("Stuart {}".format(consonent))
    elif vowel> consonent:
        print("Kevin {}".format(vowel))
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)