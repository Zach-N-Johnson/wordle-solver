import os
import utils
import timeit

clear = lambda: os.system('cls')

def main():
    guess = ""
    guesses = 0
    answers = utils.getAnswers()
    freq = utils.getFreqs(answers)
    words = utils.getTopFive(answers, freq)
    clear()

    print("Wordle Solver\nInput G for green, Y for yellow, and N for gray")
    while(True):
        print(f"Top {len(words)} options:")
        for i in words:
            print(utils.toString(i))

        print("\nEnter your guess")
        guess = utils.toList(utils.validGuess())

        print("\nEnter colors")
        colors = utils.validColors()
        if colors == "GGGGG" or colors == "ggggg":
            print(f"Solved in {guesses+1} guesses")
            break
        
        colors = utils.toList(colors)
        answers = utils.checkFull(guess, colors, answers)
        freq = utils.getFreqs(answers)
        words = utils.getTopFive(answers, freq)
        guesses += 1
        
        clear()
        print(f"{len(answers)} options left")

    new_wordle = input("New Wordle? (Y, N)\n")
    if(new_wordle == "Y" or new_wordle == "y"):
        main()

def getAverage():
    guesses = 0
    answers = utils.getAnswers()
    totals = [0, 0, 0, 0, 0, 0, 0, 0]
    loops = 0
    start = timeit.default_timer()

    for i in answers:
        thisGuesses = 0
        freq = utils.getFreqs(answers)
        thisAnswers = utils.getAnswers()
        guess = ['s', 'a', 'l', 'e', 't']
        while(True):
            colors = utils.getColors(i, guess)
            if utils.toString(colors) == "GGGGG" or utils.toString(colors) == "ggggg":
                thisGuesses += 1
                if loops % 50 == 0:
                    print(loops)
                if thisGuesses >= 7:
                    totals[7] += 1
                else:
                    totals[thisGuesses] += 1
                guesses += thisGuesses
                loops += 1
                break
            
            thisAnswers = utils.checkFull(guess, colors, thisAnswers)
            freq = utils.getFreqs(thisAnswers)
            thisGuesses += 1
            guess = utils.getNewWord(thisAnswers, freq)

    stop = timeit.default_timer()
    print(f"\n\n\n\nTotal guesses - {guesses}")
    print(f"Average - {guesses/2315}")
    print(f"1 - {totals[1]}")
    print(f"2 - {totals[2]}")
    print(f"3 - {totals[3]}")
    print(f"4 - {totals[4]}")
    print(f"5 - {totals[5]}")
    print(f"6 - {totals[6]}")
    print(f"x - {totals[7]}")
    print(f"Time - {stop-start}")
        

getAverage()