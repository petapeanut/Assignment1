list = []

def factorize(N):
    """
    This is the "example" module.

    The example module supplies one function, factorize().  For example,
    >>> factorize(3)
    [3, 1]

    """

    i = 2

    isPrime = True

    if (N > 0):

        while i <= N:

            if N % i == 0:

                list.append(i)

                isPrime = False

                factorize(N / i)

                i += 1

                break

            i += 1

        if isPrime:

            list.append(N)

        return list


# factorize(345)
# print(list)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

