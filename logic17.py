def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a: int
    Returns:
        True if all digits of a are in ascending order, False otherwise
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
    return x1>x2 and x2>x3 and x3>x4 and x4>x5
