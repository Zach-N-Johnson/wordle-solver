import os
import utils

clear = lambda: os.system('cls')

def main():
    answers = utils.get_list()
    freq = utils.get_frequencies()
    word = "slate"
    result = ""

    clear()
    print("Wordle Solver\nInput G for green, Y for yellow, and N for gray")
    while(True):
        print("\nTry", word)
        if(utils.valid_entry()):
            break
        word = "slote"

    new_wordle = input("New Wordle? (Y, N)\n")
    if(new_wordle == "Y" or new_wordle == "y"):
        main()

main()