
direction1 = 'blah'
direction2 = ''
angle = 100

while direction1 != 'e' and direction1 != 'w' and direction1 != 'n' and direction1 != 's':
    direction1 = input()
    direction1 = direction1.strip().lower()

    if direction1 == 'east':
        direction1 = 'e'

    elif direction1 == 'west':
        direction1 = 'w'

    elif direction1 == 'north':
        direction1 = 'n'

    elif direction1 == 'south':
        direction1 = 's'

print('direction1: ' + direction1)

while angle < 0 or angle > 90:
    while True:
        angle = input('angle: ')
        try:
            angle = int(angle)
        except ValueError:
            continue
        else:
            break

if angle:
    if direction1 == 'e' or direction1 == 'w':

        while direction2 != 'n' and direction2 != 's':
            direction2 = input()
            direction2 = direction2.strip().lower()
            if direction2 == 'north':
                direction2 = 'n'
            elif direction2 == 'south':
                direction2 = 's'

    elif direction1 == 'n' or direction1 == 's':
    
        while direction2 != 'e' and direction2 != 'w':
            direction2 = input()
            direction2 = direction2.strip().lower()
            if direction2 == 'east':
                direction2 = 'e'
            elif direction2 == 'west':
                direction2 = 'w'

    print('direction2: ' + direction2)

    print('Direction: [' + direction1.upper() + ' ' + angle + ' ' + direction2.upper() + ']')

else:
    print('Direction: [' + direction1.upper() + ']')