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
        print("Top five options:")
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
    f = open("solutions.txt", "a")
    guesses = 0
    answers = utils.getAnswers()
    total1 = total2 = total3 = total4 = total5 = total6 = totalx = 0
    loops = 0
    start = timeit.default_timer()

    for i in answers:
        thisGuesses = 0
        freq = utils.getFreqs(answers)
        thisAnswers = utils.getAnswers()
        guess = ['s', 'a', 'l', 'e', 't']
        while(True):
            f.write(f"{utils.toString(guess)} \n")
            colors = utils.getColors(i, guess)
            if utils.toString(colors) == "GGGGG" or utils.toString(colors) == "ggggg":
                thisGuesses += 1
                if loops % 50 == 0:
                    print(loops)
                if thisGuesses == 1:
                    total1 += 1
                elif thisGuesses == 2:
                    total2 += 1
                elif thisGuesses == 3:
                    total3 += 1
                elif thisGuesses == 4:
                    total4 += 1
                elif thisGuesses == 5:
                    total5 += 1
                elif thisGuesses == 6:
                    total6 += 1
                else:
                    totalx += 1
                guesses += thisGuesses
                loops += 1
                f.write("\n")
                break
            
            thisAnswers = utils.checkFull(guess, colors, thisAnswers)
            freq = utils.getFreqs(thisAnswers)
            thisGuesses += 1
            guess = utils.getNewWord(thisAnswers, freq)

    stop = timeit.default_timer()
    print(f"\n\n\n\nTotal guesses - {guesses}")
    print(f"Average - {guesses/2315}")
    print(f"1 - {total1}")
    print(f"2 - {total2}")
    print(f"3 - {total3}")
    print(f"4 - {total4}")
    print(f"5 - {total5}")
    print(f"6 - {total6}")
    print(f"x - {totalx}")
    print(f"Time - {stop-start}")
        

getAverage()