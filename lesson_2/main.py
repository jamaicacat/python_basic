import sys

print('\nWelcome to triangle perimeter calculation program.\n')


def get_side_length(side=''):
    result = None

    if not side:
        raise Exception('Side name was not provided.')
    else:
        while result is None:
            result = input(f'Input the "{side}" side length: ')

            try:
                result = float(result)

            except:
                print('Side length must be inputted as number.')
                result = None

    return result


def calculate_triangle_perimeter(a=None, b=None, c=None):
    if not a or not b or not c:
        raise Exception(f'Not all arguments were provided: a = {a}, b = {b}, c = {c}')

    for arg in [a, b, c]:
        if not (isinstance(arg, int) or isinstance(arg, float)):
            raise Exception(f'Argument \'{arg}\' is not a number: {type(arg)}.')

    return a + b + c


side_a = get_side_length('A')
side_b = get_side_length('B')
side_c = get_side_length('C')

if side_a == 0 or side_b == 0 or side_c == 0:
    print('\nThere are no triangles with sides equal to 0')
    print('Exiting the program.')
    sys.exit(1)

perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)

print(f'\nTriangle perimeter with sides A = {side_a}, B = {side_b}, C = {side_c} is: {perimeter}')

if perimeter > 20:
    print(f'The biggest side length is: {max([side_a, side_b, side_c])}')
elif perimeter < 10:
    print(f'The smallest side length is: {min([side_a, side_b, side_c])}')
