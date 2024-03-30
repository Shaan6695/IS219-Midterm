"""
Test file for the calculate_and_return function
"""

from main import calculate_and_return

class FakeCommandHandler:

    def __init__(self):
        self.history = []

    def add_to_history(self, calculation):
        """
        Mock method to add a calculation to history
        """
        self.history.append(calculation)

    def get_history(self):
        """
        Mock method to retrieve calculation history
        """
        return self.history

def test_calculate_and_return():
    """
    Test the calculate_and_return function with different scenarios
    """
    # Create a mock CommandHandler instance
    command_handler = FakeCommandHandler()

    # Test addition
    assert calculate_and_return(2, 2, 'add', command_handler) == 4

    # Test subtraction
    assert calculate_and_return(3, 2, 'subtract', command_handler) == 1

    # Test multiplication
    assert calculate_and_return(2, 2, 'multiply', command_handler) == 4

    # Test division
    assert calculate_and_return(4, 2, 'divide', command_handler) == 2

    # Test division by zero
    assert calculate_and_return(5, 0, 'divide', command_handler) is None

    # Test invalid operation
    assert calculate_and_return(5, 3, 'invalid', command_handler) is None

    # Test invalid numbers
    assert calculate_and_return('invalid', 3, 'add', command_handler) is None
    assert calculate_and_return(5, 'invalid', 'add', command_handler) is None

    # Test calculation history
    assert command_handler.history == [
        '2 add 2 = 4', 
        '3 subtract 2 = 1', 
        '2 multiply 2 = 4', 
        '4 divide 2 = 2'
    ]