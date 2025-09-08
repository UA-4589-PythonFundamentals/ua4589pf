
def check_password():
    user_password = input('Please enter your password: ')
    error = []

    if len(user_password) < 8:
        error.append('The password must be 8 characters long')

    if not any(not x.isalnum() for x in user_password):
        error.append('No special character')

    if not any(x.islower() for x in user_password):
        error.append('No lowercase letters')

    if not any(x.isupper() for x in user_password):
        error.append('No capital letters ')

    if not any(x.isdigit() for x in user_password):
        error.append('No number')

    if error:
        print('Check your password: ')
        for err in error:
            print(' -', err)

    return user_password
