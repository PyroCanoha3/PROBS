height = 11
width = height * 3

for stick_count in range(1, height, 2):
    print(('.|.' * stick_count).center(width, '-'))

print('FREECK '.center(width, '-'))

for stick_count in range(height-2, 0, -2):
    print(('.|.' * stick_count).center(width, '-'))