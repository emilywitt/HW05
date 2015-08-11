#!/usr/bin/env python
# HW05_ex00_logics.py
##############################################################################

def even_odd():
    """ Print even or odd:
        Takes one integer from user
            accepts only non-word numerals
            must validate
        Determines if even or odd
        Prints determination
        returns None
    """
    while True:
        number = raw_input("Enter a number> ")
        try:
            number == int(number)
            if int(number) % 2 == 0:
                print "even"
            if int(number) % 2 != 0:
                print "odd"
        except:
            print "I accept only non-word numerals, if you please."
    return none


def ten_by_ten():
    n = 1
    while n <= 100:
        if n < 11:
            print str(n) + " ",
        elif n % 10 == 1:
            print("\n")
            print n,
        else:
            print n,   
        n += 1


def find_average():
    """ Takes numeric input (non-word numerals) from the user, one number
    at a time. Once the user types 'done', returns the average.
    """
    count = 0
    added = 0

    while True:
        number = raw_input("Give me as many numbers (on separate lines) as you'd like averaged> ")
        try:
            eval(number)
            temporary = int(number)
            added = added + temporary
            count += 1
        except:
            if number == "done":
                break
            else:
                print "Try again"
    average = round(float(added)/float(count),1)
    print average

##############################################################################
def main():
    """ Calls the following functions:
        - even_odd()
        - ten_by_ten()
    Prints the following function:
        - find_average()
    """
    #even_odd()
    #ten_by_ten()
    find_average()

if __name__ == '__main__':
    main()
