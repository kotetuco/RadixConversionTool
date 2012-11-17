# -*- coding: utf-8 -*-

import sys

# Get arguments
argvs = sys.argv
argc = len(argvs)

# Default value
choice = "d2b"
inputStr = ""
decNum = 0

# Input "choice" value
if (argc >= 2):
    choice = argvs[1]

# Input changed number
if (argc >= 3):
    # argument
    inputStr = argvs[2]
else:
    # console
    inputStr = raw_input("Please input number:")

# 10->2
if choice in "d2b":
    try:
        decNum = int(inputStr, 10)
        binStr = format(decNum, 'b')
        print "Bin number:", binStr
    except:
        print "Please binary number."

# 2->10
elif choice in "b2d":
    try:
        decNum = int(inputStr, 2)
        print "Decimal number:", decNum
    except:
        print "Please decimal number."

# 16->2    
elif choice in "h2b":
    try:
        decNum = int(inputStr, 16)
        binStr = format(decNum, 'b')
        print "Bin number:", binStr
    except:
        print "Please binary number."

# 2->16
elif choice in "b2h":
    try:
        decNum = int(inputStr, 2)
        print "Hex number:", hex(decNum)
    except:
        print "Please hexadecimal number."

# 16->10
elif choice in "h2d":
    try:
        decNum = int(inputStr, 16)
        print "Decimal number:", decNum
    except:
        print "Please decimal number."

# 10->16
elif choice in "d2h":
    try:
        decNum = int(inputStr, 10)
        print "Hex number:", hex(decNum)
    except:
        print "Please hexadecimal number."

else:
    print 'Paramater error.'
