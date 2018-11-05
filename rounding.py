
# Even though python has its own round function, I'll try making my own.
# Gotta get back into programming.

number = 4214.384121453281
numberString = str(number) # argh, what the hec

decimalPlace = 0
dotReached = False
beforeDecimal = 0

for char in numberString:

    if dotReached:
        break

    elif char == '.':
        dotReached = True
        beforeDecimal += 1

    else:
        beforeDecimal += 1

print(beforeDecimal)

# cuts the string to only the numbers that it will be working with.
r = beforeDecimal + decimalPlace + 1

numberString = numberString[:r]
print(numberString)

roundingNum = numberString[-1]
print(roundingNum)

if decimalPlace == 0:
    roundedNum = numberString[-3]
else:
    roundedNum = numberString[-2]

roundedNum = int(roundedNum)
print(roundedNum)

if int(roundingNum) >= 5:
    roundedNum += 1
    if decimalPlace == 0:
        numberString = numberString[:(r-3)]
    else:
        numberString = numberString[:(r-2)]
    numberString = numberString +  str(roundedNum)

else:
    if decimalPlace == 0:
        numberString = numberString[:(r-2)]
    else:
        numberString = numberString[:(r-1)]

print(numberString)
if decimalPlace == 0:
    number = int(numberString)
else:
    number = float(numberString)
print(number)