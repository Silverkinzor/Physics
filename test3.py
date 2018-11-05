from math import sin, cos, radians, degrees, atan, sqrt
from test2func import get_direction1, get_angle, get_direction2, get_magnitude

vectors = []
vector_creation = True
try_again = ''
displacementVector = {}
answer = ''
answerMagnitude = 0
answerAngle = 0
decimalPlace = 2
c = 1

while vector_creation:

    try_again = ''
    new_vector = {}
    print('Vector ' + str(c))
    new_vector['magnitude'] = get_magnitude()

    if new_vector['magnitude'] == 0:
        new_vector['direction1'] = ''
        new_vector['angle'] = 0
        new_vector['direction2'] = ''
        new_vector['xcomp'] = 0
        new_vector['ycomp'] = 0

    else:
        new_vector['direction1'] = get_direction1()
        new_vector['angle'] = get_angle()
        new_vector['direction2'] = get_direction2(direction1=new_vector['direction1'], angle=new_vector['angle'])

        if new_vector['angle'] == 0:

            if new_vector['direction1'] == 'n' or new_vector['direction1'] == 's':
                new_vector['xcomp'] = 0
                new_vector['ycomp'] = new_vector['magnitude']

            elif new_vector['direction1'] == 'e' or new_vector['direction1'] == 'w':
                new_vector['xcomp'] = new_vector['magnitude']
                new_vector['ycomp'] = 0

            else:
                # should never happen
                print('error1 Something went wrong!')

        else:
            if new_vector['direction1'] == 'n' or new_vector['direction1'] == 's':
                new_vector['xcomp'] = (new_vector['magnitude'])*(sin(radians(new_vector['angle'])))
                new_vector['ycomp'] = (new_vector['magnitude'])*(cos(radians(new_vector['angle'])))

            else:
                new_vector['xcomp'] = (new_vector['magnitude'])*(cos(radians(new_vector['angle'])))
                new_vector['ycomp'] = (new_vector['magnitude'])*(sin(radians(new_vector['angle'])))

        if new_vector['direction1'] == 'w' or new_vector['direction2'] == 'w':
            new_vector['xcomp'] = new_vector['xcomp']*-1

        if new_vector['direction1'] == 's' or new_vector['direction2'] == 's':
            new_vector['ycomp'] = new_vector['ycomp']*-1

    vectors.append(new_vector)

    c += 1

    while try_again != 'y' and try_again != 'n':
        try_again = input('\nCreate another vector? (Y/N):')
        try_again = try_again.strip().lower()

    if try_again == 'n':
        vector_creation = False

c = 1
print('')
for vector in vectors:
#    print('\nVector ' + str(c) + ':')
#    for key, value in vector.items():
#        print(key + ': ' + str(value))
    
    if vector['angle']:
        print('d' + str(c) + ' = ' + str(vector['magnitude']) + 
              ' [' + vector['direction1'].upper() + ' ' + str(vector['angle']) + 
              ' ' + vector['direction2'].upper() + ']')
    else:
        print('\nd' + str(c) + ' = ' + str(vector['magnitude']) + 
              ' [' + vector['direction1'].upper() + ']')

    c += 1

displacementVector['xcomp'] = vectors[1]['xcomp'] - vectors[0]['xcomp']
displacementVector['ycomp'] = vectors[1]['ycomp'] - vectors[0]['ycomp']
displacementVector['angle'] = abs(degrees(atan(displacementVector['ycomp']/displacementVector['xcomp'])))
displacementVector['magnitude'] = sqrt((abs(displacementVector['xcomp'])**2) + (abs(displacementVector['ycomp'])**2))

if displacementVector['angle']:
    if displacementVector['xcomp'] > 0:
        displacementVector['direction1'] = 'e'

    elif displacementVectorp['xcomp'] < 0:
        displacementVector['direction1'] = 'w'

    else:
        # should never happen
        print('error5 Something went wrong!')

    if displacementVector['ycomp'] > 0:
        displacementVector['direction2'] = 'n'

    elif displacementVector['ycomp'] < 0:
        displacementVector['direction2'] = 's'

    else:
        # should never happen
        print('error6 Something went wrong!')

    answerMagnitude = round(displacementVector['magnitude'], decimalPlace)
    answerAngle = round(displacementVector['angle'], decimalPlace)
    answer = ('\nΔd = ' + str(answerMagnitude) + ' [' + displacementVector['direction1'].upper() + 
             ' ' + str(answerAngle) + '° ' +displacementVector['direction2'].upper() +']')

else:

    if displacementVector['xcomp']:
        if displacementVector['xcomp'] > 0:
            displacementVector['direction1'] = 'e'

        elif displacementVector['xcomp'] < 0:
            displacementVector['direction1'] = 'w'

        else:
            # should never happen
            print('error3 Something went wrong!')

    elif displacementVector['ycomp']:
        if displacementVector['ycomp'] > 0:
            displacementVector['direction1'] = 'n'

        elif displacementVector['ycomp'] < 0:
            displacementVector['direction1'] = 's'

        else:
            # should never happen
            print('error4 Something went wrong!')

    else:
        # should never happen
        print('error2 Something went wrong!')

    displacementVector['direction2'] = ''
    answerMagnitude = round(displacementVector['magnitude'], decimalPlace)
    answer = ('\nΔd = ' + str(answerMagnitude) + ' [' + 
              displacementVector['direction1'].upper() + ']')

# print(displacementVector)
print(answer)