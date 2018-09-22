'''
Created on Sep 17, 2017
@author: bobby
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
- hgeorgio
CS115 - Hw 2
'''

import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']


def letterScore(letter, scorelist):
    ''' Returns Scrabble score for a single letter using the defined scrabbleScores list '''
    def letterScore_helper(letter, scorelist):
        
        if scorelist[0][0] == letter:
            return scorelist[0][1]
        
        return letterScore_helper(letter, scorelist[1:])
    
    return letterScore_helper(letter, scorelist)

def wordScore(S, scorelist):
    ''' Returns Scrabble score for the input word S using the letterScore function '''
    def wordScore_helper(S, scorelist, score):
        if S == '':
            return score
        
        return wordScore_helper(S[1:], scorelist, score + letterScore(S[0], scorelist))
    
    return wordScore_helper(S, scorelist, 0)

def scoreList(Rack):
    ''' Input is a list of letters, uses filter and an inner function to map a list containing words made up of letters in list Rack, and their respective Scrabble scores '''
    def filterFun(word):
        
        def filterFun_helper(Rack, word, lettersLeft, accumbool):
            
            if word == '':
                return accumbool
            
            if word[0] in Rack and word[0] in lettersLeft:
                accumbool = True
                lettersLeft.remove(word[0])
            else:
                return False
            
            return filterFun_helper(Rack, word[1:], lettersLeft, accumbool)
        
        return filterFun_helper(Rack, word, list(Rack), False)
    
    wordList = filter(filterFun, Dictionary)
    wordScoreList = map(lambda x: wordScore(x, scrabbleScores), wordList)
    
    return list(map(list, zip(wordList, wordScoreList)))

def bestWord(Rack):
    ''' Input is a list of letters, returns a list containing the word with highest score from scoreList and its score '''
    sList = scoreList(Rack)
    def bestWord_helper(Rack, sList, best):
        
        if sList == []:
            return best
        
        if sList[0][1] >= best[1]:
            best = sList[0]
            
        return bestWord_helper(Rack, sList[1:], best)
    
    return bestWord_helper(Rack, sList, ['', 0])

print(letterScore('b', scrabbleScores))
print(wordScore('spam', scrabbleScores))
print(scoreList(['a', 's', 'm', 't', 'p']))
print(bestWord(['a', 's', 'm', 't', 'p']))
print(scoreList(['b', 't', 'f', 'c', 'a', 'o']))
print(scoreList(['a', 's', 'm', 'o', 'f', 'o']))