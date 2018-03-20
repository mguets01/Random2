# happy numbers

def sum_of_squares(x):
    x = str(x)
    sum = 0
    for i in range(0, len(x)):
        sum = sum + (int(x[i])**2)
    return sum

def happy_number(number):
    z = number
    for i in range(0,1000):
        y = sum_of_squares(z)
        if y == 1:
            print(number, " is a happy number!")
            break
        else:
            z = y
            continue

def find_happy(x, y):
    for i in range(x, y+1):
        happy_number(i)

find_happy(1,1000)

# get a list
