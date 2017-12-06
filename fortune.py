import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'No 1'
    elif answerNumber == 2:
        return 'No 2'
    elif answerNumber == 3:
        return 'No 3'
    elif answerNumber == 4:
        return 'No 4'
    elif answerNumber == 5:
        return 'Yes'
    elif answerNumber == 6:
        return 'No 6'
    elif answerNumber == 7:
        return 'No 7'
    elif answerNumber == 8:
        return 'No 8'
    elif answerNumber == 9:
        return 'No 9'

r = random.randint(1,9)
fortune = getAnswer(r)
print(fortune)

while fortune != 'No':
    global fortune
    fortune = getAnswer(r)
    print(fortune)
