def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a: int
    Returns:
        True if all digits sum is odd, False otherwise
    """
    b=a%10+a//100
    c=(a%100-a%10)//10
    return (b+c)%2!=0