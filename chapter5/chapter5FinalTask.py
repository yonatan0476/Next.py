# 5.4


import functools


def check_id_valid(id_number):
    """
    Checks the validity of an ID number.
    This function takes an ID number as input and performs the following steps to determine its validity:
    1. Converts the ID number to a string.
    2. If the length of the ID number is less than 9 digits, pads it with leading zeros to make it 9 digits long.
    3. Multiplies each digit at an even position by 2, and keeps the same value for digits at odd positions.
    4. If the result is greater than 9, adds the two digits.
    5. Calculates the sum of all the resulting digits.
    6. Checks if the sum is divisible by 10.
    :param id_number: The ID number to be checked for validity.
    :type id_number: int
    :return: True if the ID number is valid, False otherwise.
    :rtype: bool
    """
    id_number = str(id_number)
    if len(id_number) < 9:
        id_number = (9 - len(id_number)) * '0' + id_number
    mult = [int(id_number[place - 1]) * 2 if place % 2 == 0 else int(id_number[place - 1]) for place in
            range(1, len(id_number) + 1)]
    add_9 = [result // 10 + result % 10 if result > 9 else result for result in mult]
    return functools.reduce(lambda sum, digit: sum + digit, add_9, 0) % 10 == 0


class IDIterator:
    """
    Iterator for generating valid ID numbers.
    """

    def __init__(self, id):
        """
        Initializes an IDIterator object.
        :param id: The starting ID number for iteration.
        :type id: int
        """
        self._id = id

    def __iter__(self):
        """
        Returns the iterator object itself.
        :return: The iterator object (self).
        :rtype: IDIterator
        """
        return self

    def __next__(self):
        """
        Returns the next valid ID number, by incrementing the id and checking it using check_id_valid function.
        If a valid ID number is found, it is returned.
        If the maximum limit (999999999) is reached without finding a valid ID number, StopIteration is raised.
        :return: The next valid ID number.
        :rtype: int
        :raise: StopIteration: raise an Exception if the maximum limit (999999999) is reached.
        """
        id_help = self._id
        while id_help < 999999999:
            id_help += 1
            if check_id_valid(id_help):
                self._id = id_help
                return self._id
        raise StopIteration


def id_generator(id_received):
    """
    Generates valid ID numbers starting from the given ID.
    The generation continues until the maximum limit (999999999) is reached or no more valid ID numbers are available.
    :param id_received: The starting ID number.
    :type id_received: int
    :yield: The next valid ID number.
    :rtype: Generator
    """
    while id_received < 999999999:
        id_received += 1
        if check_id_valid(id_received):
            yield id_received


def main():
    # Receiving an ID and a choice for the creation method
    my_id = int(input("Enter an ID: "))
    choice = input("Generator or Iterator? (gen / it)? ")
    if choice == "it":
        # Creating an iterator
        my_id_iterator = IDIterator(my_id)
        for i in range(10):
            print(next(my_id_iterator))
    elif choice == "gen":
        # Creating a generator
        ids_gen = id_generator(my_id)
        for i in range(10):
            print(next(ids_gen))


if __name__ == '__main__':
    main()
