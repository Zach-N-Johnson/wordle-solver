import os
import utils

clear = lambda: os.system('cls')

def main():
    guess = ""
    guesses = 0
    answers = utils.getList()
    freq = utils.getFrequencies()
    word = ['s', 'l', 'a', 't', 'e']
    clear()

    print("Wordle Solver\nInput G for green\nInput Y for yellow\nInput N for gray")
    while(True):
        for i in answers:
            print(utils.toString(i))
        print(f"{len(answers)} options")
        print(f"\nTry {utils.toString(word)}")

        print("Enter your guess")
        guess = utils.toList(utils.validGuess())

        print("Enter colors")
        colors = utils.validColors()
        if colors == "GGGGG" or colors == "ggggg":
            print(f"Solved in {guesses+1} guesses")
            break
        colors = utils.toList(colors)

        answers = utils.checkFull(guess, colors, answers)

        word = utils.getNewWord(answers, freq)

        guesses += 1
        

    new_wordle = input("New Wordle? (Y, N)\n")
    if(new_wordle == "Y" or new_wordle == "y"):
        main()

main()