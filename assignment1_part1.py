def list_divide(numbers, divide=2):
    """
    The function returns the number of elements in the numbers list that are divisible by divide
    """
    count = 0
    for number in numbers:
        if number % divide == 0:
            count += 1
    return count

class ListDivideException(Exception):
    """
    This is the requested custom exception for the list_divide function
    """
    pass

def test_list_divide():
    """
    Test listDivide | [Below, renamed the function to match the list_divide function] -RA
    """
    assert list_divide([1,2,3,4,5]) == 2
    assert list_divide([2,4,6,8,10]) == 5
    assert list_divide([30, 54, 63,98, 100], divide=10) == 2
    assert list_divide([]) == 0
    assert list_divide([1,2,3,4,5], 1) == 5
    
if __name__ == "__main__":
    test_list_divide()
