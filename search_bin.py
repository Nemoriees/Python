import random

def search_bin():
    print('think about a number from 0 to 1000')
    min_n = 0
    max_n = 1000
    new_number = int((max_n + min_n)/2)
    tries = 0
    answer = 0
    
    while answer == 0 :
        print('is your number higher or lower than ' + str(new_number))
        a = input('h - higher \nl - lower \na - accurate \n')
        '''print(a)'''
        if a == 'h':
            min_n = new_number
            new_number = int((max_n + min_n)/2)
        elif a == 'l':
            max_n = new_number
            new_number = int((max_n + min_n)/2)
        elif a =='a':
            answer = 1
        else:
            print("type 'h', 'l' or 'a'")
            tries = tries -1
        tries = 1 + tries
        
    if tries == 1:
         print("you have choosen %s, it took %d try to guess it" % (str(new_number), tries))
    else:
        print("you have choosen %s, it took %d tries to guess it" % (str(new_number), tries))


def try_to_guess():
    number = random.randrange(1001)
    try:
        a = int(input("I've choosen the number from 0 to 1000, try to guess it "))
    except ValueError:
        a = int(input("You must choose a number!  "))
        
    tries = 1
    while a != number:
        if a > number:
            try:
                a = int(input("Chosen number is lower, try again: "))
            except ValueError:
                a = int(input("You must choose a number!  "))
                '''problem => if I type something else than int two times error occure'''

        elif a < number:
            try:
                a = int(input("Chosen number is higher, try again: "))
            except ValueError:
                a = int(input("You must choose a number!  "))
                
        else:
            tries = tries - 1
        tries = tries +1  
    print ("congratulation, the number is %d, it took you %d tries" % (number, tries))
        
