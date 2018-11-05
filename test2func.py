from math import sin, cos, radians

def get_magnitude():
    magnitude = -1
    while magnitude < 0:
        while True:
            magnitude = input('Magnitude: ')
            try:
                magnitude = float(magnitude)
            except ValueError:
                continue
            else:
                break

    return magnitude

def get_direction1():
    direction1 = 'blah'
    while direction1 != 'e' and direction1 != 'w' and direction1 != 'n' and direction1 != 's':
        direction1 = input('Direction 1: ')
        direction1 = direction1.strip().lower()

        if direction1 == 'east':
            direction1 = 'e'

        elif direction1 == 'west':
            direction1 = 'w'

        elif direction1 == 'north':
            direction1 = 'n'

        elif direction1 == 'south':
            direction1 = 's'

    return direction1

def get_angle():
    angle = 100
    while angle < 0 or angle > 89.999999:
        while True:
            angle = input('Angle: ')
            try:
                angle = float(angle)
            except ValueError:
                continue
            else:
                break

    return angle

def get_direction2(direction1, angle):
    direction2 = ''
    if angle:
        if direction1 == 'e' or direction1 == 'w':

            while direction2 != 'n' and direction2 != 's':
                direction2 = input('Direction2: ')
                direction2 = direction2.strip().lower()

                if direction2 == 'north':
                    direction2 = 'n'

                elif direction2 == 'south':
                    direction2 = 's'

        elif direction1 == 'n' or direction1 == 's':
    
            while direction2 != 'e' and direction2 != 'w':
                direction2 = input('Direction2: ')
                direction2 = direction2.strip().lower()

                if direction2 == 'east':
                    direction2 = 'e'

                elif direction2 == 'west':
                    direction2 = 'w'

    return direction2

def get_vector():
    new_vector = {}
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

        return new_vector