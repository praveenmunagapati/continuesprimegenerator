#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      sir
#
# Created:     22/10/2022
# Copyright:   (c) sir 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    for Number in range (1, 10**50):
        count = 0
        for i in range(2, (Number//2 + 1)):
            if(Number % i == 0):
                count = count + 1
                break
        if (count == 0 and Number != 1):
            yield Number

if __name__ == '__main__':
    prime = main()
    print(next(prime))
    print(next(prime))
    print(next(prime))
    #do not uncomment
    """while True:
        print(next(prime))"""


