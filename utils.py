import json

def get_list():
    file = open("data/answers.txt", "r")

    answers = []
    for line in file:
        answers.append(line.strip())

    file.close()

    return answers

def get_frequencies():
    with open("data/frequencies.txt") as f:
        freq = f.read()

    return json.loads(freq)

