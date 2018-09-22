'''
Created on Sep 30, 2017
@author: bobby
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
- hgeorgio
CS115 - Hw 4
'''

def pascal_row(n):
    ''' Input is an integer n. Returns a list of integers representing the nth Pascal row of the Pascal Triangle 
    using pascal_adj_sums to get sum of every two terms from the previous row. '''
    if n == 0:
        return [1]
    if n == 1:
        return [1, 1]
    return [1] + pascal_adj_sums(n - 1, [], n) + [1]

def pascal_adj_sums(n, sumslst, nOrig):
    ''' Input is an integer n, a list, and the original inputted n value from pascal_row. 
    Returns a list of sums of adjacent terms in the previous Pascal row. '''
    if len(pascal_row(n)) == 1:
        return sumslst
    else:
        return pascal_adj_sums(n - 1, sumslst + [pascal_row(nOrig - 1)[n] + pascal_row(nOrig - 1)[n - 1]], nOrig)

def pascal_triangle(n):
    ''' Input is an integer n. Returns a list containing lists of each Pascal row from the nth row to 0th row. '''
    if n == -1:
        return []
    return pascal_triangle(n - 1) + [pascal_row(n)]

print(pascal_row(0))
print(pascal_row(1))
print(pascal_row(2))
print(pascal_row(3))
print(pascal_row(4))
print(pascal_row(5))
print(pascal_row(6))
print(pascal_row(7))
print(pascal_triangle(5))