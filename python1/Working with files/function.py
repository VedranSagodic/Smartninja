#definiranje funkcija
def pozdrav(name):
    return"Hello {0}!".format(name)

def calculate_sum(num1, num2):
    result= num1 + num2
    return result

def cube(num):
    result = num*num
    return result

def pedometer(distance, steps):
    step_number= distance / steps
    return step_number

def absolute(x, y):
    if x > y:
        return x - y
    else:
        return y-x

def square_cube(num):
    square = num*num
    cube = num*num*num
    return square, cube



