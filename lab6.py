'''
Created on Oct 11, 2017
@author: bobby
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
- hgeorgio
CS115 - Lab 6
'''

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 != 0 and n != 0:
        return True
    else:
        return False
    
print(isOdd(0))

# Base-2 representation of 42 = 101010
# The rightmost bit in the base-2 representation of odd numbers is 1. The rightmost bit in the base-2 representation of even numbers is 0.
# Removing the rightmost bit divides the number by 2, ignoring the remainder.
# When Y = N/2, in the case of an even number, a 0 can be appended to the end of the base-2 representation. For odd numbers, a 1 can be appended to the base-2 representation.
# The last bit represents the remainder when the base-10 number is divided by 2

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    
    return numToBinary(n // 2) + str(n % 2) # Linear recursion (has pending operation that appends the remainders)

print(numToBinary(2))

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    def binaryToNum_helper(s, count):
        if s == '':
            return 0

        return int(s[-1]) * (2 ** count) + int(binaryToNum_helper(s[:-1], count + 1))
    return binaryToNum_helper(s, 0)

print(binaryToNum('101010'))

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    result = numToBinary(binaryToNum(s) + 1)
    while len(result) < 8:
        result = '0' + result
    while len(result) > 8:
        result = result[1:]
    return result

print(increment('00000000'))
print(increment('11111111'))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
        
    def count_helper(s, count):
        if count == n + 1:
            return
        print(increment(s))
        count_helper(increment(s), count + 1)
        
    if n == 0:
        return
    else:
        count_helper(s, 1)
        
count('00000000', 1)

# Base-3 representation of 59 = 2012 (since when the recursion occurs, the remainder from integer division of 3 is appended to the base-3 string; enables usage of 0, 1, and 2)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    
    return numToTernary(n // 3) + str(n % 3)

print(numToTernary(42))

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    def ternaryToNum_helper(s, count):
        if s == '':
            return 0

        return int(s[-1]) * (3 ** count) + int(ternaryToNum_helper(s[:-1], count + 1))
    return ternaryToNum_helper(s, 0)

print(ternaryToNum('1120'))
