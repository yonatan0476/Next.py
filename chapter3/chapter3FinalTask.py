# 3.4

from string import punctuation


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, index):
        self._char = char
        self._index = index

    def __str__(self):
        return "The username contains an illegal character \"%s\" at index %d" % (self._char, self._index)


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"


class PasswordMissingCharacter(Exception):
    def __str__(self):
        return "The password is missing a character"


class PasswordMissingCharacterUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Uppercase)"


class PasswordMissingCharacterLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Lowercase)"


class PasswordMissingCharacterDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Digit)"


class PasswordMissingCharacterSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + " (Special)"


def check_input(username, password):
    try:
        if len(username) < 3:
            raise UsernameTooShort
        elif len(username) > 16:
            raise UsernameTooLong
        for index in range(len(username)):
            if username[index] in punctuation.replace('_', ''):
                raise UsernameContainsIllegalCharacter(username[index], index)
        if len(password) < 8:
            raise PasswordTooShort
        elif len(password) > 40:
            raise PasswordTooLong
        elif not any(char.isupper() for char in password):
            raise PasswordMissingCharacterUppercase
        elif not any(char.islower() for char in password):
            raise PasswordMissingCharacterLowercase
        elif not any(char.isdigit() for char in password):
            raise PasswordMissingCharacterDigit
        elif not any(char in punctuation for char in password):
            raise PasswordMissingCharacterSpecial
    except Exception as e:
        print(e)
        return False
    else:
        print("OK")
        return True


def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    while not check_input(username, password):
        username = input("Enter username: ")
        password = input("Enter password: ")


if __name__ == '__main__':
    main()
