'''
Created on Oct 28, 2017
@author: bobby
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
- hgeorgio
CS115 - Hw 8
'''

FullAdder = \
{ ('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }

def TcToNum(S):
    ''' Takes input binary string S; returns base-10 integer represented by S using twos complement '''
    def TcToNum_help(S, accumS):
        if S == '':
            return ''
        if S[0] == '1':
            # signed negative, so toggle, add 1, negate
            return -1 * binaryToNum(addB(toggle(S), '1'))
        else:
            # positive
            return binaryToNum(S)
        return TcToNum_help(S[1:], accumS)
    return TcToNum_help(S, '')

def NumToTc(N):
    ''' Takes input integer N; returns binary representation of the twos complement of N '''
    if abs(N) != 128 and abs(N) < 128:
        # can be represented with 8 bits
        if N < 0:
            result = addB(toggle(pad(numToBinary(abs(N)))), '1')
        else:
            result = pad(numToBinary(N))
    elif abs(N) == 128:
        if N == 128:
            # positive 128
            result = 'Error'
        else:
            # negative 128
            result = '10000000'
    else:
        # abs(N) > 128 and not equal to 128
        result = 'Error'
    return result

def pad(S):
    ''' Appends zeros to string S until the length of it equals 8; returns padded string '''
    while len(S) < 8:
        S = '0' + S
    return S

def toggle(S):
    ''' Changes all zeros in S to ones and all ones to zeros; returns toggled string '''
    if S == '':
        return ''
    if S[0] == '0':
        return '1' + toggle(S[1:])
    if S[0] == '1':
        return '0' + toggle(S[1:])
    
def binaryToNum(S):
    ''' Takes string S in base-2 and converts the string to a base-10 integer; returns the base-10 representation of S as an integer '''
    def baseBToNum_helper(S, count):
        if S == '':
            return 0
        return int(S[-1]) * (2 ** count) + int(baseBToNum_helper(S[:-1], count + 1))
    return baseBToNum_helper(S, 0)
    
def addB(S1, S2):
    ''' Takes binary strings S1 and S2 and performs binary addition using sumBit and carryBit from the predefined dictionary FullAdder; 
    returns the sum of S1 and S2 as a binary string '''
    if len(S1) > len(S2):
        while len(S2) < len(S1):
            S2 = '0' + S2
    if len(S2) > len(S1):
        while len(S1) < len(S2):
            S1 = '0' + S1
            
    def addB_helper(S1, S2, carryIn, bitaccum):
        if S1 == '' and S2 == '':
            result = carryIn + bitaccum
            # Ensure that there are no leading zeros
            while result[0] == '0':
                result = result[1:]
            return result

        sumBit, carryBit = FullAdder[(S1[-1], S2[-1], carryIn)]
        return addB_helper(S1[:-1], S2[:-1], carryBit, sumBit + bitaccum)
        
    return addB_helper(S1, S2, '0', '')

def numToBinary(N):
    ''' Takes base-10 integer N and converts it to base-2; returns the base-2 representation of N as a string '''
    if N == 0:
        return ''
    return numToBinary(N // 2) + str(N % 2)

print(TcToNum('11111111'))
print(TcToNum('10000000'))
print(TcToNum('01000000'))
print(NumToTc(128)) # returns error
print(NumToTc(-129)) # returns error
print(NumToTc(-128))
print(NumToTc(-127))
print(NumToTc(-1))
print(NumToTc(0))
print(NumToTc(1))
print(NumToTc(64))
print(NumToTc(126))
print(NumToTc(127))
      