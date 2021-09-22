"""
Problem Statement
~~~~~~~~~~~~~~~~~


"""


def fizzbuzz(n: int):
    """
    Print integers 1 to N, but print “Fizz” if an integer is divisible by 3,
    “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is
     divisible by both 3 and 5.

    :param n: [int] stop
    :return: None
    :raises: TypeError: when input n is not of type int
    """
    if n < 1:
        return
    i = 1
    while i <= n:
        if i%3==0 or i%5==0:
            if i%(3*5)==0:
                print("FizzBuzz")
            elif i%3==0:
                print("Fizz")
            elif i%5==0:
                print("Buzz")
        else:
            print(i)

        i += 1


if __name__ == "__main__":
    fizzbuzz(30)