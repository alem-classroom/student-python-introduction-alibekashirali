import random

def is_positive(num):
    # return true if num is positive, otherwise return false
    if num > 0:
        return true
    else:
        return false
    
def is_even(num):
    # return true if num is even, otherwise return false
    if (num%2) == 0:
        return true
    else:
        return false

def is_positive_and_even(num):
    # return true if num is positive and even, otherwise return false
    if ((num%2) == 0) and num > 0:
        return true
    else:
        return false

def is_positive_or_even(num):
    # return true if num is positive or even, otherwise return false
    if ((num%2) == 0) or num > 0:
        return true
    else:
        return false
