def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a: int
    Returns:
        True if a is five-digit number, False otherwise
    """
    x1=a%10
    a//=10
    x2=a%10
    a//=10
    x3=a%10
    a//=10
    x4=a%10
    a//=10
    x5=a%10
    return x1>=0 and x2>=0 and x3>=0 and x4>=0 and x5>0