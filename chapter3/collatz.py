
def collatz(number):
    if number%2 == 0:
        return number//2
    else:
        return 3 * number + 1
    

number = 0
while number != 1:
    try:
        num_in = int(input('Type the number: '))
        print(collatz(num_in))
        number = collatz(num_in)
    except ValueError:
        print ("This is not integer, try again.")

#try_list = [3, 10, 5, 16, 8, 4, 2, 1, 0, 'puppy']

#for i in range(len(try_list)):
#    print(collatz(try_list[i]))

    
#print(collatz(1))
#print(collatz(2))
#print(collatz(3))
#print(collatz(4))
