
def strong_password():
    while True:
        password = input('Please Enter a passowrd: ')
        special_characters = [x for x in '[@_!#$%^&*()<>?/\|}{~:]']
        if len(password) >=8 and (any(x.isupper() for x in password)) and (any(x in special_characters for x in password)):
            print('Password Accepted')
            break
        else: 
            message = """"
            Ooops...To meet the required security level: your password must be between 8 - 32 characters long and 
            include at least 3 of the following character types: English alphabet uppercase letter (A-Z) English alphabet 
            lowercase letter (a-z) Decimal digit number (0-9).
            Try again .....
            """
            print(message)
strong_password()
