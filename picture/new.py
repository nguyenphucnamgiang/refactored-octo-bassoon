def exercise_1():
    print('-'*25,'Sum of digit','-'*25, sep='-')
    number = int(input('input number of terms: '))
    while number > 9:
        number = sum(int(d) for d in str(number))

    print(f'Sum of digit: {number}')


def exercise_2():
    print('-'*25,'Sum expression','-'*25, sep='-')
    x = int(input('Input the value  of x: '))
    terms = int(input('Input the value  of terms: '))
    lst = [1]
    while len(lst) < terms:
        lst.append(lst[-1] + 2)
    result = 0
    string = 'S = '
    for i in range(len(lst)):
        if i % 2 == 0:
            result += x**lst[i]
            string += f' ({x})^{lst[i]} -'
        else :
            result -= x**lst[i]
            string += f' ({x})^{lst[i]} +'
    print(f'{string[:-1]} = {result}')

def exercise_3():
    print('-'*25,'Athrimetic progression','-'*25, sep='-')
    starting_number = int(input('Input the starting number of the A.P. series: '))
    number_of_items = int(input('Input the number of items for the A.P. series: '))
    common_difference = int(input('Input the common differece the A.P. series: '))
    string = 'S = '
    result = 0
    for i in range(number_of_items):
        result += starting_number + common_difference*i
        string += f' {starting_number + common_difference*i} +'
            
    print(f'{string[:-1]} = {result}')
    
def isPrime(n:int):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def exercise_4():
    print('-'*25,'Sum of two primes','-'*25, sep='-')
    number = int(input('Input the number: '))
    for i in range(2,(number//2)+1):
        if isPrime(i) and isPrime(number-i):
            print(f'{number} can be written as {i} + {number-i}')
         
            
def exercise_5():
    print('-'*25,'Alphabet triangle','-'*25, sep='-')
    n = int(input('Input the number: '))
    add = 0
    for i in range(n):
        print(" " * (n - i - 1), end="")
        for j in range(i + 1):
            print(chr(65 + add), end=" ")
            add += 1
        print("")
        
    
def menu():
    print('-'*25,'MENU','-'*25, sep='-')
    print(' '*18,'[1] Sum of digit')
    print(' '*18,'[2] Sum expression')
    print(' '*18,'[3] Athrimetic progression')
    print(' '*18,'[4] Sum of two primes')
    print(' '*18,'[5] Alphabet triangle')
    print(' '*18,'[0] Exit')
    print('-'*60)



print(' '*6,f'Name     :    Nguyễn Phúc Nam Giang')
print(' '*6,f'ID       :    HE182202')
print(' '*6,f'Class    :    PFP191.M')
print('-'*60, end= '\n\n')



while True :
    menu()
    choice = int(input('Enter your option: '))
    if choice == 1:
        exercise_1()
    elif choice == 2:
        exercise_2()
    elif choice == 3:
        exercise_3()
    elif choice == 4:
        exercise_4()
    elif choice == 5:
        exercise_5()
    elif choice == 0:
        break 
        
        
    
    





