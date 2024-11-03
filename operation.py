def add(a, b):
    '''
    Feature X
    ----------
    This function takes two inputs and returns the sum of the two numbers.
    
    Parameters:
        a (int/float): First number.
        b (int/float): Second number.
    
    Returns:
        int/float: Sum of a and b.
    '''
    return a + b


def subtract(a, b):
    '''
    Feature Y
    ----------
    This function takes two inputs and returns the difference of the two numbers.
    
    Parameters:
        a (int/float): First number.
        b (int/float): Second number.
    
    Returns:
        int/float: Difference of a and b.
    '''
    return a - b


def multiply(a, b):
    '''
    Feature Z
    ----------
    This function takes two inputs and returns the product of the two numbers.
    
    Parameters:
        a (int/float): First number.
        b (int/float): Second number.
    
    Returns:
        int/float: Product of a and b.
    '''
    return a * b


def divide(num1, num2):
    '''
    Division
    ----------
    This function takes two inputs and returns the quotient of the first number 
    divided by the second. If the second number is zero, it returns an error message.
    
    Parameters:
        num1 (int/float): Numerator.
        num2 (int/float): Denominator.
    
    Returns:
        int/float/str: Quotient of num1 divided by num2, or an error message if division by zero.
    '''
    return num1 / num2 if num2 != 0 else 'Error (divide by zero)'


def power(num1, num2):
    '''
    Exponentiation
    ----------
    This function raises the first input to the power of the second input.
    
    Parameters:
        num1 (int/float): Base number.
        num2 (int/float): Exponent.
    
    Returns:
        int/float: Result of num1 raised to the power of num2.
    '''
    return num1 ** num2


def sqrt(num1):
    '''
    Square Root
    ----------
    This function returns the square root of the input number.
    
    Parameters:
        num1 (int/float): The number to find the square root of.
    
    Returns:
        float: Square root of num1.
    '''
    return num1 ** 0.5