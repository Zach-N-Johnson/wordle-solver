import json
from re import L

def getList():
    file = open("data/answers.txt", "r")

    answers = []
    for line in file:
        answers.append(list(line.strip()))

    file.close()

    return answers

def getFrequencies():
    with open("data/frequencies.txt") as f:
        freq = f.read()

    return json.loads(freq)

def validColors():
    while(True):
        not_ok = False
        result = input()
        for i in result:
            if(not (i == 'G' or i == 'Y' or i == 'N' or i == 'g' or i == 'y' or i == 'n')):
                not_ok = True
        if(len(result) != 5):
            print("Response must be five letters")
        elif(not_ok):
            print("Response must only use G, Y, or N")
        else:
            break
    return result

def validGuess():
    while(True):
        guess = input()
        if(len(guess) != 5):
            print("Response must be five letters")
        else:
            break
    return guess

def toString(word):
    new_word = ""
    for i in word:
        new_word += i
    return new_word

def toList(word):
    return list(word)

def checkFull(word, colors, list):
    k = 0
    for i in colors:
        if i == 'G' or i == 'g':
            list = checkGreen(k, word[k], list)
        elif i == 'Y' or i == 'y':
            list = checkYellow(k, word[k], list)
        else:
            list = checkGray(word[k], list)
        k += 1
    return list

def checkGreen(pos, letter, list):
    for i in reversed(list):
        if not(i[pos] == letter):
            list.remove(i)
    return list

def checkYellow(pos, letter, list):
    for i in reversed(list):
        check = True
        if i[pos] == letter:
            list.remove(i)
        else:
            for j in i:
                if j == letter:
                    check = False
            if check:
                list.remove(i)
    return list

def checkGray(letter, list):
    for i in reversed(list):
        for j in i:
            if j == letter:
                list.remove(i)
                break
    return list