import utils

answers = utils.get_list()
freq = utils.get_frequencies()
word = "slate"
result = ""


def main():
    while(True):
        print("Wordle Solver\nInput G for green, Y for yellow, and N for gray\n")
        print("Try", word)
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
            break
    new_wordle = input("New Wordle? (Y, N)\n")
    if(new_wordle == "Y" or new_wordle == "y"):
        clean()
        main()

def clean():
    return

main()