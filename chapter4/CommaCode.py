spam = ['apples', 'bananas', 'tofu', 'cats', 43]

def change(spam):
    if len(spam)== 1:
        return 'and ' + str(spam[0])
    else:
        return str(spam[0]) + ', ' + change(spam[1:])

print(change(spam))
