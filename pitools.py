from decimal import *
import sys
from tqdm import tqdm
import datetime


def ArctanDenom(d, ndigits):
    # Calculates arctan(1/d) = 1/d - 1/(3*d^3) + 1/(5*d^5) - 1/(7*d^7) + ...
    total = term = (10**ndigits) // d
    n = 0
    with tqdm (range (ndigits), desc="Calculating Pi... ") as tq:
        while term != 0:
            n += 1
            term //= -d*d
            total += term // (2*n + 1)
            tq.update()
            # print('ArctanDenom({}) calculated {} iterations.'.format(d, n))

    print()
    print('Total: ArctanDenom({}) took {} iterations.'.format(d, n))
    return total

def GetDetailledPi(xdigits = 10,ndigits = int(10000),outFileName="pidigits.txt" ):
    # Use Machin's Formula to calculate pi.
    print("Using ArctanDenom for calculations")
    with tqdm (range(10), desc="Writing pi in digits  ") as tq:
        pi = 4 * (4*ArctanDenom(5,ndigits+xdigits) - ArctanDenom(239,ndigits+xdigits))
        tq.update()
        # We calculated extra digits to compensate for roundoff error.
        # Chop off the extra digits now.
        pi //= 10**xdigits
        tq.update()
         # Write the result to a text file.

        #print("Writing file")
        with open(outFileName, 'wt') as outfile:
            # Insert the decimal point after the first digit '3'.
            text = str(pi)
            outfile.write(text[0] + '.' + text[1:] + '\n')
        tq.update()

    #tq.update()
    # print('Wrote to file {}'.format(outFileName))
    # print()
    # print(str(pi))
    # tq.update()

    return str(pi)
def ChopInCharBits(strInput):
    myNumberList = []
    #lets loop through the string and get chops of 2 chars
    iLenght= len(strInput)
    print("Array Lenght: " + str(iLenght))
    with tqdm (range(iLenght), desc="Chopping Pi digits to bits... ") as tq:
        for i in range(1,len(strInput),2):
            strSubString=strInput[i:i+2]
            myNumberList.append(str(strSubString))
            #print(str(i) + ": " + str(strSubString))
            tq.update()

    return myNumberList


def convertToLetters(Pi_arr):
    myCharList=[]
    with tqdm (range (len(Pi_arr)), desc="Converting digits to chars... ") as tq:
        for i in Pi_arr:
         if int(i) > 26:
             #take the two chars seperately
             # print("Splitting:" + str(i))
             # print("Char0:" + str(i)[:1])
             # print("Char1:" + str(i)[-1:])
             # myCharList.append(str(chr(int(strChars[0]))))
             # myCharList.append(str(chr(int(strChars[1]))))
             char1=str(chr(int(str(i)[:1])+65))
             char2=str(chr(int(str(i)[-1:])+65))
             myCharList.append(char1)
             myCharList.append(char2)
             # print("Char:" + str(i) + " converted to " + str(str(chr(int(strChars[0]))))  + str(chr(int(strChars[1]))))
         else:
            myCharList.append(str(chr(int(i)+65)))
            #print("Char:" + str(i) + " converted to " + str(chr(int(i))))
        tq.update()

    return myCharList

def nilakantha(reps):
        result = Decimal(3.0)
        op = 1
        n = 2
        for n in range(2, 2*reps+1, 2):
                result += 4/Decimal(n*(n+1)*(n+2)*op)
                op *= -1
        return result
def writeToFile(strArr, strFileName):
    with open(strFileName, 'wt') as outfile:
        # Insert the decimal point after the first digit '3'.
        for strChar in strArr:
            outfile.write(strChar)

# reps=1000000000
# pi=nilakantha(reps)
# print(pi)
start_time = datetime.datetime.now()
print("Pi generator started !")
Pi=GetDetailledPi(1,1000000)
print("Pi : " + str(Pi))
#Pi=Pi[0:len(Pi)]
print("Pi : " + str(Pi))

char_pi=ChopInCharBits(Pi)
#char_pi=ChopInCharBits(char_pi)
char_pi=convertToLetters(char_pi)
print(str(char_pi))
writeToFile(char_pi,"pi_chars.txt")
end_time = datetime.datetime.now()
duration_time=end_time - start_time
print("Duration:" + str(duration_time))
