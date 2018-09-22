'''
Created on Sep 25, 2017
@author: bobby
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
- hgeorgio
CS115 - Hw 3
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def giveChange(amount, coins):
    ''' Input is a positive integer amount and a list of integers coins. 
    Returns the minimum amount of coins (with values defined in coins list) needed to make change and equal the input amount '''
    if amount == 0:
        # base case
        return [0, []]
    elif coins == [] or amount < 0:
        # impossible to make change
        return [float('inf'), []]
    else:
        # recursive until base case
        use_it = giveChange(amount, coins[1:])
        lose_it = giveChange(amount - coins[0], coins)[0] + 1
    return [min(use_it[0], lose_it), [coins[0]] + use_it[1]]

print(giveChange(48, [1, 5, 10, 25, 50]))

scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    return list(map(wordScore, dct))
    
def letterScore(letter, scorelist):
    ''' Returns Scrabble score for a single letter using the defined scrabbleScores list '''
    def letterScore_helper(letter, scorelist):
        
        if scorelist[0][0] == letter:
            return scorelist[0][1]
        
        return letterScore_helper(letter, scorelist[1:])
    
    return letterScore_helper(letter, scorelist)

def wordScore(S):
    ''' Returns Scrabble score for the input word S using the letterScore function '''
    origS = S
    def wordScore_helper(S, scorelist, score):
        if S == '':
            return [origS, score]
        
        return wordScore_helper(S[1:], scorelist, score + letterScore(S[0], scorelist))
    
    return wordScore_helper(S, scrabbleScores, 0)

print(wordsWithScore(['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva'], scrabbleScores))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    ''' Tail Recursion '''
    if L == []:
        return []
    if n == 0:
        return L
    return take(n - 1, L[:-1])

print(take(4, [0, 1, 2, 3, 4, 5, 6, 7]))

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    ''' Tail Recursion '''
    if L == []:
        return []
    if n == 0:
        return L
    return drop(n - 1, L[1:])

print(drop(4, [0, 1, 2, 3, 4, 5, 6, 7]))


