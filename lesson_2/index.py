import sys

print('\nWelcome to triangle perimeter calculation program.')
print('If you want to stop program execution, enter \'exit\'. \n')


def get_side_length(side=''):
    result = None

    if not side:
        raise Exception('Side name was not provided.')
    else:
        while not result:
            result = input(f'Input the "{side}" side length.: ')

            if result == 'exit':
                print('Exiting the program.')
                sys.exit(1)

            try:
                result = float(result)

                if result == 0:
                    print('Side length can\'t be equal to 0. Try again.')
                    result = None
                elif result < 0:
                    print('Side length can\'t be less than 0. Try again.')
                    result = None

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

perimeter = calculate_triangle_perimeter(side_a, side_b, side_c)

print(f'\nTriangle perimeter with sides A = {side_a}, B = {side_b}, C = {side_c} is: {perimeter}')
