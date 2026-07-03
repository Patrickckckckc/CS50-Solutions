import inflect

inflector = inflect.engine()

names = []

while True:
    try:
        new_name = input('Name: ')
        names.append(new_name)
    except EOFError:
        print(f'\nAdieu, adieu, to {inflector.join(names)}')
        break;
