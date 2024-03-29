# get answer list
def getAnswers():
    file = open("data/answers.txt", "r")
    answers = []
    for line in file:
        answers.append(list(line.strip()))
    file.close()
    return answers

# check if color entry is valid, return input
def validColors():
    while(True):
        not_ok = False
        result = input()
        for i in result:
            if(not (i == 'G' or i == 'Y' or i == 'N' or i == 'g' or i == 'y' or i == 'n')):
                not_ok = True
                break
        if(len(result) != 5):
            print("Response must be five letters")
        elif not_ok:
            print("Response must only use G, Y, or N")
        else:
            break
    return result

# check if guess entry is valid, return guess
def validGuess():
    while(True):
        guess = input()
        if len(guess) == 5:
            break
        else:
            print("Response must be five letters")
    return guess

# convert list to string
def toString(word):
    return "".join(word)

# convert string to list
def toList(word):
    return list(word)

# return new list with only the possible words left after guess
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

# return list after green check
def checkGreen(pos, letter, list):
    for i in reversed(list):
        if not(i[pos] == letter):
            list.remove(i)
    return list

# return list after yellow check
def checkYellow(pos, letter, list):
    for i in reversed(list):
        if i[pos] == letter or letter not in i:
            list.remove(i)
    return list

# return list after gray check
def checkGray(letter, list):
    for i in reversed(list):
        if letter in i:
            list.remove(i)
    return list

# check for duplicates in a list, return the duplicate item
def checkDup(list):
    if len(list) == len(set(list)):
        return None
    return getDup(list)

# helper for checkDup
def getDup(list):
    l = []
    dups = []
    for i in list:
        if i not in l:
            l.append(i)
        else:
            dups.append(i)
    return dups

# get new frequency data for answer list by percentage
def getFreqs(list):
    answers = list
    total = len(list) * 5
    freqs = dict.fromkeys(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 0)
    for i in answers:
        for j in i:
            freqs[j] += 1
        if checkDup(i):
            freqs[checkDup(i)[0]] -= 1
            total -= 1
            if len(checkDup(i)) == 2:
                freqs[checkDup(i)[1]] -= 1
    for i in freqs:
        freqs[i] /= total
    return freqs

# use new freq data to return word with highest possible freq
def getNewWord(answers, freq):
    answersfreq = []
    for i in answers:
        totalfreq = 0
        dups = checkDup(i)
        for j in i:
            totalfreq += freq[j]
        if dups:
            totalfreq -= freq[checkDup(i)[0]]
            if len(dups) == 2:
                totalfreq -= freq[checkDup(i)[1]]
        answersfreq.append(totalfreq)
    answersfreq, answers = (list(t) for t in zip(*sorted(zip(answersfreq, answers))))
    return answers[-1]

# use new freq data to return list of five words with highest possible freq
def getTopFive(answers, freq):
    answersfreq = []
    topfive = []
    count = 0

    for i in answers:
        totalfreq = 0
        dups = checkDup(i)
        for j in i:
            totalfreq += freq[j]
        if dups:
            totalfreq -= freq[dups[0]]
            if len(dups) == 2:
                totalfreq -= freq[dups[1]]
        answersfreq.append(totalfreq)
    answersfreq, answers = (list(t) for t in zip(*sorted(zip(answersfreq, answers))))
    for i in reversed(answers):
        if count == 5:
            break
        else:
            topfive.append(i)
            count += 1
    return topfive

def getColors(word, guess):
    colors = []
    for i in range(0, 5):
        if word[i] == guess[i]:
            colors.append("G")
        else:
            if guess[i] in word:
                colors.append("Y")
            else:
                colors.append("N")
    return colors