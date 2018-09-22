'''
Created on Oct 19, 2017
@author: bobby
Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
- hgeorgio
CS115 - Hw 7
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

def numToBaseB(N, B):
    ''' Takes base-10 integer N and converts it to base B; returns the base B representation of N as a string '''
    if N == 0:
        return ''
    return numToBaseB(N // B, B) + str(N % B)

def baseBToNum(S, B):
    ''' Takes string S in base B and converts the string to a base-10 integer; returns the base-10 representation of S as an integer '''
    def baseBToNum_helper(S, count):
        if S == '':
            return 0
        return int(S[-1]) * (B ** count) + int(baseBToNum_helper(S[:-1], count + 1))
    return baseBToNum_helper(S, 0)

def baseToBase(B1, B2, SinB1):
    ''' Takes integers B1 and B2 and SinB1, a string in base B1, converts SinB1 to base-10 and then converts the base-10 number to base B2 using numToBaseB; returns string SinB1 in base B2 '''
    return numToBaseB(baseBToNum(SinB1, B1), B2)

def add(S, T):
    ''' Takes strings S and T, converts both strings to base-10 numbers and adds them; returns binary representation of the sum as a string '''
    return numToBaseB(baseBToNum(S, 2) + baseBToNum(T, 2), 2)

def addB(S1, S2):
    ''' Takes binary strings S1 and S2 and performs binary addition using sumBit and carryBit from the predefined dictionary FullAdder; returns the sum of S1 and S2 as a binary string '''
    # Pad S1, S2 to same length by appending zeros
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

print(add('100', '1'))
print(addB('11', '1'))
print(addB('011', '100'))