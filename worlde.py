import re
import words

possibleSolution = words.wordsList

a_z = "abcdefghijklmnopqrstuvwxyz"
a_zAstricks = "[a-z]*"
inputValidation = "^[a-z]{5}$"
openbracket = "["
closebracket = "]"
dollar = "$"

listOfLists = []
answerCharSet = set()

for i in range(5):
    listOfLists.append(a_z)

# All 5 letters will be in this regex
regexexp = openbracket + listOfLists[0] + closebracket + openbracket + listOfLists[1] + closebracket + openbracket + listOfLists[2] + closebracket + openbracket + listOfLists[3] + closebracket + openbracket + listOfLists[4] + closebracket + dollar
r = re.compile(regexexp)
possibleSolution = list(filter(r.match, possibleSolution))
print(possibleSolution)
print(len(possibleSolution))

while len(possibleSolution) > 1:

    while True:
        val = input("Enter your 5 letter word: ")
        if re.match(inputValidation, val):
            break
        else:
            print("Invalid input, try again")
        
    for i in range(0, len(val)):
        pos = int(input( 'is "' + val[i] + '" green(1), yellow(2), black(3): '))
        if pos == 1: # The character exists in the answer at the correct position
            listOfLists[i] = val[i]
            answerCharSet.add(val[i])
        elif pos == 2: # The character exists in the answer at the wrong position
            listOfLists[i] = listOfLists[i].replace(val[i], "")
            answerCharSet.add(val[i])
        elif pos == 3: # The character does not exist in the answer
            for j in range(0, len(listOfLists)):
                listOfLists[j] = listOfLists[j].replace(val[i], "")

    # Update the regex and filter the possible solutions
    regexexp = openbracket + listOfLists[0] + closebracket + openbracket + listOfLists[1] + closebracket + openbracket + listOfLists[2] + closebracket + openbracket + listOfLists[3] + closebracket + openbracket + listOfLists[4] + closebracket + dollar
    r = re.compile(regexexp)
    possibleSolution = list(filter(r.match, possibleSolution))

    # Iterate through possibleSolution and check if the word is in answerCharSet
    if answerCharSet :
        for letter in answerCharSet:
            regexexp = a_zAstricks + letter + a_zAstricks
            r = re.compile(regexexp)
            possibleSolution = list(filter(r.match, possibleSolution))

    print(possibleSolution)
    print(len(possibleSolution))