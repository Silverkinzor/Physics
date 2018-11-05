
# Disclaimer: decimals may not be exactly accurate due to how floats work in computers
# Next step: make it into a function.

number = 429734.96726
numberString = str(number)
decimalOnly = number - int(number)
decimalString = str(decimalOnly)

decimalPlace = 1
dotReached = False
invalidDecimal = False
carryTheOne = False
beforeDecimal = 0
afterDecimal = 0

for char in numberString:

    if dotReached:
        afterDecimal += 1

    elif char == '.':
        dotReached = True

    else:
        beforeDecimal += 1

beforeStr = numberString[:beforeDecimal]
decimalString = decimalString[2:afterDecimal+2]
print(numberString, beforeStr, decimalString)

if decimalPlace == 0:
    if int(decimalString[0]) >= 5:
        roundedNum = int(beforeStr[-1])
        roundedNum += 1
        if roundedNum == 10:
            roundedNum2 = int(beforeStr[-2])
            roundedNum2 += 1
            roundedNum = 0
            beforeStr = beforeStr[:-2] + str(roundedNum2) + str(roundedNum)
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
            roundedNum2 = int(beforeStr[decimalPlace-2])
            roundedNum2 += 1
            roundedNum = 0
            beforeStr = beforeStr[:decimalPlace-2] + str(roundedNum2) + str(roundedNum)
        else:
            beforeStr = beforeStr[:decimalPlace-1] + str(roundedNum)

    else:
        beforeStr = beforeStr[:decimalPlace]

    for x in range(abs(decimalPlace)):
        beforeStr += '0'

    number = int(beforeStr)

else:
    if decimalPlace > afterDecimal:
        invalidDecimal = True

    elif int(decimalString[decimalPlace]) >= 5:
        roundedNum = int(decimalString[decimalPlace-1])
        roundedNum += 1
        if decimalPlace == 1 and roundedNum == 10:
            carryTheOne = True
        elif roundedNum == 10:
            roundedNum2 = int(decimalString[decimalPlace-2])
            roundedNum2 += 1
            roundedNum = 0
            decimalString = decimalString[:decimalPlace-2] + str(roundedNum2) + str(roundedNum)
        else:
            decimalString = decimalString[:decimalPlace-1] + str(roundedNum)

    else:
        decimalString = decimalString[:decimalPlace]

    number = beforeStr + '.' + decimalString
    number = float(number)
    if carryTheOne:
        number = int(number) + 1

if invalidDecimal:
    number = 'Error: decimalPlace out of bounds'

print(number)