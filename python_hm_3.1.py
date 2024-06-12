digit_1_input = int (input('Please enter first number: '))
digit_2_input = int (input('Please enter second number: '))

action_input = int (input('Please enter action: \n 1 + \n 2 - \n 3 / \n 4 * \n'))

if action_input == 1:
    print(digit_1_input + digit_2_input)
if action_input == 2:
    print(digit_1_input - digit_2_input)
if action_input == 3:
    print(digit_1_input / digit_2_input)
if action_input == 4:
    print(digit_1_input * digit_2_input)



