"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    if first == second:
        return True
    else:
        return False


    """
    If @first and @second has same value should return True
    In another case should return False
    """



def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    if type(first)==type(second):
        return True
    else:
        return False

    """
    If @first and @second has same type should return True
    In another case should return False
    """



def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    if first is second:
        return True
    else:
        return False

    """
    If @first and @second has same type should return True
    In another case should return False
    """
    


def multiple_ints(first_value: int, second_value: int) -> int:
    if type(first_value) != int or type(second_value) != int:
            raise ValueError
    else:
        return first_value * second_value

    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    try:
        first_value = int(first_value)
        second_value = int(second_value)
        return first_value * second_value
    except ValueError:
        raise ValueError( 'invalid operator! ')

    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        ValueError

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """



def is_word_in_text(word: str, text: str) -> bool:
    if word in text:
        return True
    else:
        return False

    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """



def some_loop_exercise() -> list:
    list = []
    for num in range(13):
        list_1 = list.append(num)
    list.remove(6)
    list.remove(7)
    return list

    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    number = data[:]
    for num in data:
        if num < 0:
            print(num)
            number.remove(num)
    return number

    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """


def alphabet() -> dict:
    from string import ascii_lowercase
    dictionary = {}
    x = 0
    for i in ascii_lowercase:
        x +=  1
        dictionary[x] = i
    return dictionary


"""
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """



def simple_sort(data: List[int]) -> List[list]:
    new_list = []
    my_list = data.copy()

    while my_list:
        minimum = my_list[0]
        for x in my_list:
            if x < minimum:
                minimum = x
        new_list.append(minimum)
        my_list.remove(minimum)

    print(new_list)
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    print('Done!')
