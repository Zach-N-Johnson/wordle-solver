import os
import utils

clear = lambda: os.system('cls')

def main():
    guesses = 0
    answers = utils.get_list()
    freq = utils.get_frequencies()
    word = ['s', 'l', 'a', 't', 'e']
    clear()

    print("Wordle Solver\nInput G for green\nInput Y for yellow\nInput N for gray")
    while(True):
        print(f"\nTry {utils.toString(word)}")
        if(utils.valid_entry()):
            print(f"Solved in {guesses+1} guesses")
            break


        
        guesses += 1
        

    new_wordle = input("New Wordle? (Y, N)\n")
    if(new_wordle == "Y" or new_wordle == "y"):
        main()

main()