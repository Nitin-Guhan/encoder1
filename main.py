def encode(password):
    password = list(password)
    count = 0
    for num in password:
        new_num = int(num)
        password[count] = new_num
        count += 1
    for i in range(len(password)):
        if password[i] < 7:
            password[i] = password[i] + 3
        else:
            if password[i] == 7:
                password[i] = 0
            elif password[i] == 8:
                password[i] = 1
            else:
                password[i] = 2
    nstring = ''
    for value in password:
        nstring += str(value)
    return nstring
def decode(Password):
    nstring = ''
    for char in Password:
        if int(char) > 2:
            nstring += str((int(char) - 3))
        else:
            if char == '2':
                nstring += str('9')
            elif char == '1':
                nstring += str('8')
            elif char == '0':
                nstring += str('7')
    return nstring








if __name__ == '__main__':
    encoder_decoder = True
    while encoder_decoder:
        print('Menu\n---------------\n1. Encode\n2. Decode\n3. Quit')
        print()
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input('Please enter your password to encode: ')
            encoded_pass = encode(password)
            print('Your password has been encoded and stored!\n')
        elif option == 2:
            print(f'The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}\n')
        elif option == 3:
            encoder_decoder = False


