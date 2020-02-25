#Partner 1: Eric
#Partner 2: Mia
########################
import random
#Assignment Name: GitHub Practice

def getNRandom(n):
    '''takes in an integer and returns a list of n random integers between 1 and 10, inclusive'''
    if n < 11:
        return random.sample(range(1,11), n)
    else:
        return False


def multiplyRandom(numbers):
    '''takes in a list of n numbers and returns the product of the numbers'''
    product = 1
    for i in numbers:
        product = product * i
    return product


def main():
    print(multiplyRandom(getNRandom(10)))

if __name__ == "__main__":
    main()
