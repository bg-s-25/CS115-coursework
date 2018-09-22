'''
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
- hgeorgio
Created on Sep 14, 2017
@author: bobby
Lab 2
'''

def dot(L, K):
    ''' Uses dot_helper to apply recursion and allow for evaluation until base case '''
    def dot_helper(L, K, total):
        if L == [] or K == []:
            if total != 0:
                return total
            else:
                return 0.0
        return dot_helper(L[1:], K[1:], add(total, mult(L[0], K[0])))
    return dot_helper(L, K, 0)

def explode(S):
    ''' Uses explode_helper to apply recursion and create a list of each character of the input string '''
    def explode_helper(S, newlst):
        if S == '':
            return newlst
        return explode_helper(S[1:], newlst + [S[0]])
    return explode_helper(S, [])
        
def ind(e, L):
    ''' Uses ind_helper to apply recursion and return either the index at which element e is located or the length of L if e is not contained in l
    x is the current index of L that is being checked '''
    def ind_helper(e, L, x):
        if L == [] or L == '' or L[0] == e:
            return x
        return ind_helper(e, L[1:], 1 + x)
    return ind_helper(e, L, 0)

def removeAll(e, L):
    ''' Uses myFilter function to return a list containing a certain removed element '''
    def removeAll_check(x):
        if x == e:
            return False
        else:
            return True
    return myFilter(removeAll_check, L)

def myFilter(f, L):
    ''' Returns list based on whether function f returns True or False when f(L) is evaluated '''
    def myFilter_helper(f, L, newlst):
        if L == []:
            return newlst
        if f(L[0]) == True:
            return myFilter_helper(f, L[1:], newlst + [L[0]])
        else:
            return myFilter_helper(f, L[1:], newlst)
    return myFilter_helper(f, L, [])

def deepReverse(L):
    ''' Returns reversed list with all lists contained in it also reversed '''
    def deepReverse_helper(L, newlst):
        if L == []:
            return newlst
        if isinstance(L[-1], list):
            # element in L is a list
            return deepReverse_helper(L[:-1], newlst + [deepReverse(L[-1])]) # listified reversed last element of L
        # deepReverse_helper(L[-1], newlst)
        else:
            # element in L is not a list
            return deepReverse_helper(L[:-1], newlst + [L[-1]])
    return deepReverse_helper(L, [])

def reverse(lst):
    ''' Returns reversed list '''
    if lst == []:
        return []
    return reverse(lst[1:]) + [lst[0]] # Places element at index 0 at end of new list

def mult(x, y):
    ''' Returns product of two arguments '''
    return x * y

def add(x, y):
    ''' Returns sum of two arguments '''
    return x + y

print(dot([5,3], [6,4]))
print(explode('spam'))
print(ind('b', ['a', 'b', 'c', 'd']))
print(removeAll(1, [3, 4, 1, 3, 1]))
print(myFilter(lambda x: x % 2 == 0, [2]))
print(deepReverse([1, [2, 3], 4, [5, 6]]))
print(deepReverse([1, 2, 3, 4]))