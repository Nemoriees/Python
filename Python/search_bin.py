def search_bin():
    print('think about a number from 0 to 1000')
    min_n = 0
    max_n = 1000
    new_number = int((max_n + min_n)/2)
    '''print(new_number)'''
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
            
    print('you have choosen ' + str(new_number))
        
