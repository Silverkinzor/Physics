# A program to add and subtract vectors. Displacement and sum.

from math import sin, cos, radians, degrees, atan, sqrt
from test2func import get_direction1, get_angle, get_direction2, get_magnitude

print('Vector Addition/Subtraction v.0.1' +
      '\n(May not be perfectly accurate, due to floats)' +
      '\n---------------------------------------------------')

menu = ''
decimalPlace = 2
try_again = ''
vectors = []
vector_creation = True
displacementVector = {}

while menu != '0':

    print('\nActions:' + 
          '\n1. Vector Addition (Sum)' + 
          '\n2. Vector Subtraction (2) (Displacement)' + 
          '\n3. Total Subtraction, then Addition (Total Displacement)' +
          '\n9. Set rounding value' + 
          '\n0. Exit')

    try_again = ''
    vectors = []
    vector_creation = True
    displacementVector = {}
    resultantVector = {}
    answer = ''
    answerMagnitude = 0
    answerAngle = 0
    c = 1

    menu = input('\nWhat do you want to do?: ') # menu selection
    menu = (menu.strip()).lower()

    if menu == '0':
        pass

    elif menu == '1':
        vectors = []
        vector_creation = True
        resultantVector = {}
        c = 1

        while vector_creation:

            try_again = ''
            new_vector = {}
            print('\nVector ' + str(c))
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
    
            if vector['angle']:
                print('v' + str(c) + ' = ' + str(vector['magnitude']) + 
                      ' [' + vector['direction1'].upper() + ' ' + str(vector['angle']) + 
                      '° ' + vector['direction2'].upper() + ']')

            elif not vector['magnitude']:
                print('v' + str(c) + ' = 0')

            else:
                print('v' + str(c) + ' = ' + str(vector['magnitude']) + 
                      ' [' + vector['direction1'].upper() + ']')

            c += 1

        resultantVector['xcomp'] = 0
        resultantVector['ycomp'] = 0

        for vector in vectors:
            resultantVector['xcomp'] += vector['xcomp']
            resultantVector['ycomp'] += vector['ycomp']

        if resultantVector['xcomp']:
            resultantVector['angle'] = abs(degrees(atan(resultantVector['ycomp']/resultantVector['xcomp'])))
        else:
            resultantVector['angle'] = 0
            resultantVector['direction1'] = ''

        resultantVector['magnitude'] = sqrt((abs(resultantVector['xcomp'])**2) + (abs(resultantVector['ycomp'])**2))

        if resultantVector['angle']:
            if resultantVector['xcomp'] > 0:
                resultantVector['direction1'] = 'e'

            elif resultantVector['xcomp'] < 0:
                resultantVector['direction1'] = 'w'

            else:
                # should never happen
                print('error5 Something went wrong!')

            if resultantVector['ycomp'] > 0:
                resultantVector['direction2'] = 'n'

            elif resultantVector['ycomp'] < 0:
                resultantVector['direction2'] = 's'

            else:
                # should never happen
                print('error6 Something went wrong!')

            answerMagnitude = round(resultantVector['magnitude'], decimalPlace)
            answerAngle = round(resultantVector['angle'], decimalPlace)
            answer = ('\nΣv = ' + str(answerMagnitude) + ' [' + resultantVector['direction1'].upper() + 
                     ' ' + str(answerAngle) + '° ' +resultantVector['direction2'].upper() +']')

        else:

            if resultantVector['xcomp']:
                if resultantVector['xcomp'] > 0:
                    resultantVector['direction1'] = 'e'

                elif resultantVector['xcomp'] < 0:
                    resultantVector['direction1'] = 'w'

                else:
                    # should never happen
                    print('error3 Something went wrong!')

            elif resultantVector['ycomp']:
                if resultantVector['ycomp'] > 0:
                    resultantVector['direction1'] = 'n'

                elif resultantVector['ycomp'] < 0:
                    resultantVector['direction1'] = 's'

                else:
                    # should never happen
                    print('error4 Something went wrong!')

            resultantVector['direction2'] = ''
            
            if resultantVector['magnitude']:
                answerMagnitude = round(resultantVector['magnitude'], decimalPlace)
                answer = ('\nΣv = ' + str(answerMagnitude) + ' [' + 
                          resultantVector['direction1'].upper() + ']')
            else:
                answer = ('\nΣv = 0')

        print(answer)

    elif menu == '2':
        vectors = []
        c = 1

        for x in range(2):

            try_again = ''
            new_vector = {}
            print('\nVector ' + str(c))
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


        c = 1
        print('')
        for vector in vectors:
    
            if vector['angle']:
                print('d' + str(c) + ' = ' + str(vector['magnitude']) + 
                      ' [' + vector['direction1'].upper() + ' ' + str(vector['angle']) + 
                      '° ' + vector['direction2'].upper() + ']')

            elif not vector['magnitude']:
                print('d' + str(c) + ' = 0')

            else:
                print('d' + str(c) + ' = ' + str(vector['magnitude']) + 
                      ' [' + vector['direction1'].upper() + ']')

            c += 1

        displacementVector['xcomp'] = vectors[1]['xcomp'] - vectors[0]['xcomp']
        displacementVector['ycomp'] = vectors[1]['ycomp'] - vectors[0]['ycomp']
        if displacementVector['xcomp']:
            displacementVector['angle'] = abs(degrees(atan(displacementVector['ycomp']/displacementVector['xcomp'])))
            displacementVector['direction1'] = ''
        else:
            displacementVector['angle'] = 0
        displacementVector['magnitude'] = sqrt((abs(displacementVector['xcomp'])**2) + (abs(displacementVector['ycomp'])**2))

        if displacementVector['angle']:
            if displacementVector['xcomp'] > 0:
                displacementVector['direction1'] = 'e'

            elif displacementVector['xcomp'] < 0:
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

            displacementVector['direction2'] = ''
            
            if displacementVector['magnitude']:
                answerMagnitude = round(displacementVector['magnitude'], decimalPlace)
                answer = ('\nΔd = ' + str(answerMagnitude) + ' [' + 
                          displacementVector['direction1'].upper() + ']')
            else:
                answer = ('\nΔd = 0')

        print(answer)

    elif menu == '3':
        vectors = []
        vector_creation = True
        resultantVector = {}
        c = 1

        while vector_creation:

            try_again = ''
            new_vector = {}
            print('\nVector ' + str(c))
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

                # End of vector creation

        c = 1
        print('')
        for vector in vectors:
    
            if vector['angle']:
                print('d' + str(c) + ' = ' + str(vector['magnitude']) + 
                        ' [' + vector['direction1'].upper() + ' ' + str(vector['angle']) + 
                        '° ' + vector['direction2'].upper() + ']')

            elif not vector['magnitude']:
                print('d' + str(c) + ' = 0')

            else:
                print('d' + str(c) + ' = ' + str(vector['magnitude']) + 
                        ' [' + vector['direction1'].upper() + ']')

            c += 1

        c = 0
        displacementVectors = []
        for x in range(len(vectors) - 1):
            displacementVector = {}

            displacementVector['xcomp'] = vectors[c+1]['xcomp'] - vectors[c]['xcomp']
            displacementVector['ycomp'] = vectors[c+1]['ycomp'] - vectors[c]['ycomp']
            if displacementVector['xcomp']:
                displacementVector['angle'] = abs(degrees(atan(displacementVector['ycomp']/displacementVector['xcomp'])))
                displacementVector['direction1'] = ''
            else:
                displacementVector['angle'] = 0
            displacementVector['magnitude'] = sqrt((abs(displacementVector['xcomp'])**2) + (abs(displacementVector['ycomp'])**2))

            if displacementVector['angle']:
                if displacementVector['xcomp'] > 0:
                    displacementVector['direction1'] = 'e'

                elif displacementVector['xcomp'] < 0:
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

                displacementVector['direction2'] = ''
            
            displacementVectors.append(displacementVector)
            c += 1


        resultantVector['xcomp'] = 0
        resultantVector['ycomp'] = 0
        c = 1
        print('')
        for vector in displacementVectors:
    
            if vector['angle']:
                print('Δd' + str(c) + ' = ' + str(round(vector['magnitude'], decimalPlace)) + 
                        ' [' + vector['direction1'].upper() + ' ' + str(round(vector['angle'], decimalPlace)) + 
                        '° ' + vector['direction2'].upper() + ']')

            elif not vector['magnitude']:
                print('Δd' + str(c) + ' = 0')

            else:
                print('Δd' + str(c) + ' = ' + str(vector['magnitude']) + 
                        ' [' + vector['direction1'].upper() + ']')
            c += 1
            resultantVector['xcomp'] += vector['xcomp']
            resultantVector['ycomp'] += vector['ycomp']

        if resultantVector['xcomp']:
            resultantVector['angle'] = abs(degrees(atan(resultantVector['ycomp']/resultantVector['xcomp'])))
        else:
            resultantVector['angle'] = 0
            resultantVector['direction1'] = ''

        resultantVector['magnitude'] = sqrt((abs(resultantVector['xcomp'])**2) + (abs(resultantVector['ycomp'])**2))

        if resultantVector['angle']:
            if resultantVector['xcomp'] > 0:
                resultantVector['direction1'] = 'e'

            elif resultantVector['xcomp'] < 0:
                resultantVector['direction1'] = 'w'

            else:
                # should never happen
                print('error5 Something went wrong!')

            if resultantVector['ycomp'] > 0:
                resultantVector['direction2'] = 'n'

            elif resultantVector['ycomp'] < 0:
                resultantVector['direction2'] = 's'

            else:
                # should never happen
                print('error6 Something went wrong!')

            answerMagnitude = round(resultantVector['magnitude'], decimalPlace)
            answerAngle = round(resultantVector['angle'], decimalPlace)
            answer = ('\nΣΔd = ' + str(answerMagnitude) + ' [' + resultantVector['direction1'].upper() + 
                        ' ' + str(answerAngle) + '° ' +resultantVector['direction2'].upper() +']')

        else:

            if resultantVector['xcomp']:
                if resultantVector['xcomp'] > 0:
                    resultantVector['direction1'] = 'e'

                elif resultantVector['xcomp'] < 0:
                    resultantVector['direction1'] = 'w'

                else:
                    # should never happen
                    print('error3 Something went wrong!')

            elif resultantVector['ycomp']:
                if resultantVector['ycomp'] > 0:
                    resultantVector['direction1'] = 'n'

                elif resultantVector['ycomp'] < 0:
                    resultantVector['direction1'] = 's'

                else:
                    # should never happen
                    print('error4 Something went wrong!')

            resultantVector['direction2'] = ''
            
            if resultantVector['magnitude']:
                answerMagnitude = round(resultantVector['magnitude'], decimalPlace)
                answer = ('\nΣΔd = ' + str(answerMagnitude) + ' [' + 
                            resultantVector['direction1'].upper() + ']')
            else:
                answer = ('\nΣΔd = 0')

        print(answer)
        print('Or you know, just do d(final) - d(initial) to make this all alot simpler.')


    elif menu == '9':
        print('\ndecimalPlace=' + str(decimalPlace))
        while try_again != 'y' and try_again != 'n':
            try_again = input('\nWould you like to change this value? (Y/N):')
            try_again = try_again.strip().lower()

        if try_again == 'y':
            print('\nPlease enter a new value. Must be an integer.')
            while True:
                try:
                    decimalPlace = input('decimalPlace=')
                    decimalPlace = int(decimalPlace)
                except ValueError:
                    pass
                else:
                    print('Change saved.')
                    break

    else: # the user inputs something in the menu that isn't one of the options
        print('Enter one of the options.')

# To do:
# Create option 3
# Clean all of this code up into functions