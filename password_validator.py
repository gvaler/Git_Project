import re
import sys

def validator(password):
    """
    Check if password is valid,
    return 0 if is valid, and
    1 if not
    :param password:str
    :return: int 0 or 1
    """

    if len(password) < 10:
        print('\033',"Invalid password",'\033')
        print("Make sure your password is at lest 10 letters")
        return 1
    elif re.search('[0-9]', password) is None:
        print('\033',"Invalid password",'\033')
        print("Make sure your password has a number in it")
        return 1
    elif re.search('[A-Z]', password) is None:
        print('\033',"Invalid password",'\033')
        print( "Make sure your password has a big letter in it")
        return 1
    elif re.search('[a-z]', password) is None:
        print('\033',"Invalid password",'\033')
        print("Make sure your password has a little letter in it")
        return 1
    else:
        print('\033[0;32m',"valid password",'\033[0m')
        return 0

validator(sys.argv[1])
