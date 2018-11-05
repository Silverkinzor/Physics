# Disclaimer: decimals may not be exactly accurate due to how floats work in computers
# Next step: create test(s), optimize

def roundFunction(number, decimalPlace):

    numberString = str(number)
    decimalOnly = number - int(number)
    decimalString = str(decimalOnly)

    dotReached = False
    invalidDecimal = False
    carryTheOne = False
    outOfBounds = False
    beforeDecimal = 0
    afterDecimal = 0
    c = 0

    for char in numberString:

        if dotReached:
            afterDecimal += 1

        elif char == '.':
            dotReached = True

        else:
            beforeDecimal += 1

    beforeStr = numberString[:beforeDecimal]
    decimalString = decimalString[2:afterDecimal+2]

    if decimalPlace == 0:
        if int(decimalString[0]) >= 5:
            roundedNum = int(beforeStr[-1])
            roundedNum += 1
            if roundedNum == 10:
                while roundedNum == 10:
                    try:
                        roundedNum = int(beforeStr[(-2-c)])
                    except IndexError:
                        outOfBounds = True
                        break
                    else:
                        roundedNum += 1
                        c += 1
            
                if outOfBounds:
                    beforeStr = int(beforeStr) + 1
                else:
                    beforeStr = beforeStr[:(-1-c)] + str(roundedNum)
                    for x in range(c):
                        beforeStr += '0'

            else:
                beforeStr = beforeStr[:-1] + str(roundedNum)

        number = int(beforeStr)


    elif decimalPlace < 0:
        if abs(decimalPlace) >= beforeDecimal:
            invalidDecimal = True

        elif int(beforeStr[decimalPlace]) >= 5:
            roundedNum = int(beforeStr[decimalPlace-1])
            roundedNum += 1
            if roundedNum == 10:
                while roundedNum == 10:
                    try:
                        roundedNum = int(beforeStr[(decimalPlace-2-c)])
                    except IndexError:
                        outOfBounds = True
                        break
                    else:
                        roundedNum += 1
                        c += 1
            
                if outOfBounds:
                    beforeStr = int(beforeStr) + 1
                else:
                    beforeStr = beforeStr[:(decimalPlace-1-c)] + str(roundedNum)
                    for x in range(c):
                        beforeStr += '0'
            else:
                beforeStr = beforeStr[:decimalPlace-1] + str(roundedNum)

        else:
            beforeStr = beforeStr[:decimalPlace]

        # adding back in the 0s that the rounding ignores
        for x in range(abs(decimalPlace)):
            beforeStr += '0'

        number = int(beforeStr)

    else:
        if decimalPlace > afterDecimal:
            invalidDecimal = True

        elif int(decimalString[decimalPlace]) >= 5:
            decimalString = decimalString[:decimalPlace]
            roundedNum = int(decimalString[decimalPlace-1])
            roundedNum += 1
            if decimalPlace == 1 and roundedNum == 10:
                carryTheOne = True
            elif roundedNum == 10:
                while roundedNum == 10:
                    try:
                        roundedNum = int(decimalString[(decimalPlace-2-c)])
                    except IndexError:
                        outOfBounds = True
                        break
                    else:
                        roundedNum += 1
                        c += 1
                if outOfBounds:
                    carryTheOne = True
                else:
                    decimalString = decimalString[:(decimalPlace-1-c)] + str(roundedNum)
            else:
                decimalString = decimalString[:decimalPlace-1] + str(roundedNum)

        else:
            decimalString = decimalString[:decimalPlace]

        if carryTheOne:
            number = int(number) + 1
        else:
            number = beforeStr + '.' + decimalString
            number = float(number)

    if invalidDecimal:
        number = 'Error: decimalPlace out of bounds'

    return number