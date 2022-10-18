import timeit

def square(number):
    try:
        if number <= 0 or number > 64:
            raise ValueError("square must be between 1 and 64")
        return 2**(number-1)
    except ValueError as ve:
        raise ValueError("square must be between 1 and 64")
    pass


def total():
    number = 1
    summ = 0
    try:
        while number <= 64:
            summ += 2**(number-1)
            number += 1
    except ValueError:
        raise ValueError("square must be between 1 and 64")

    return summ
    pass


#print(square(-6))
#start = timeit.timeit()
#print(total())
#end = timeit.timeit()
#print(end-start)
