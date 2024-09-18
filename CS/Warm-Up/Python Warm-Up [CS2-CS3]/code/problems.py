
def is_palyndrom(n):
    reversed_number = 0
    number = n
    while (number > 0):
        reversed_number = (number % 10) + reversed_number*10
        number = number//10
    if reversed_number == n:
        return True
    else:
        return False
    
def is_palyndrom2(n):
    number = 0
    if  n % 2 == 0:
        return False
    i = 0
    while (n > 0):
        number = (10**i)*(n % 2) + number
        n = int((n - n % 2)/2)
        i = i + 1
    print(number)
    if is_palyndrom(number):
        return True
    else:
        return False
    
def largest_palyndrom():
    max_number = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if is_palyndrom(i*j) and max_number < i*j:
                max_number = i*j
    print(max_number)
    
def sum_of_palyndrom():
    sum = 0
    for i in range(1, 1000000, 2):
        if is_palyndrom(i) and is_palyndrom2(i):
            sum += i
            print(i)
    print(sum)
    
x = 1000
y = x
y = 1001
print(x)