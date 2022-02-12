import json

def get_list():
    file = open("data/answers.txt", "r")

    answers = []
    for line in file:
        answers.append(list(line.strip()))

    file.close()

    return answers

def get_frequencies():
    with open("data/frequencies.txt") as f:
        freq = f.read()

    return json.loads(freq)

def valid_entry():
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
    if(result == "GGGGG" or result == "ggggg"):
        return True
    else:
        return False

def toString(word):
    new_word = ""
    for i in word:
        new_word += i
    
    return new_word