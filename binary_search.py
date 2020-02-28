#!/bin/python3

def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT:
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''

    left = 0
    right = len(xs)-1
    if not xs:
        return None

    def go(left, right):

        mid = (left + right) // 2

        if (left == right or len(xs)==1) and xs[mid] <= 0:
            return None

        if (left == right or len(xs)==1 or right == 1) and xs[mid] > 0:
            return mid

        if 0 < xs[mid]:
            right = mid

        if 0 > xs[mid]:
            left = mid + 1

        if 0 == xs[mid]:
            return mid + 1

        return go(left, right)

    return go(left, right)


def _find_index(xs, val):

    left = 0
    right = len(xs) - 1
    if not xs:
        return None

    def go(left, right):

        mid = (left + right) // 2

        if (left == right or len(xs) == 1) and xs[mid] != val:
            return None

        if (left == right or len(xs) == 1) and xs[mid]== val:
            return mid

        if val < xs[mid]:
            left = mid + 1

        if val > xs[mid]:
            right = mid

        if val == xs[mid]:
            return mid

        return go(left, right)

    return go(left, right)


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT:
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2

    I highly recommend creating stand-alone functions for steps 1 and 2
    that you can test independently.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([1, 2, 3], 4)
    0
    '''


    test = _binary_search(xs, x)
    if test is None or not xs:
        return 0

    abs_max = xs[0]
    abs_min = xs[-1]

    low = x-1
    high = x
    lowest = _binary_search(xs, low)
    highest = _binary_search(xs, high)

    while lowest is None:
        if low >= abs_min - 1:
            low -= 1
            lowest = _binary_search(xs, low)
        else:
            lowest = _binary_search(xs, x)

    while highest is None:
        if high > abs_max:
            highest = 0
        else:
            high += 1
            highest = _binary_search(xs, x)

    if highest == lowest:
        return len(xs) - highest

    return lowest-highest


def _binary_search(xs, x):

    lo = 0
    hi = len(xs)

    while lo < hi:
        mid = (lo + hi) // 2

        if xs[mid] < x:
            hi = mid
        elif xs[mid] > x:
            lo = mid + 1
        elif mid > 0 and xs[mid-1] == x:
            hi = mid
        else:
            return mid

    return None

def argmin(f, lo, hi, epsilon=1e-3):
    '''
    Assumes that f is an input function that takes a float as input and returns a float with a unique global minimum,
    and that lo and hi are both floats satisfying lo < hi.
    Returns a number that is within epsilon of the value that minimizes f(x) over the interval [lo,hi]

    HINT:
    The basic algorithm is:
        1) The base case is when hi-lo < epsilon
        2) For each recursive call:
            a) select two points m1 and m2 that are between lo and hi
            b) one of the 4 points (lo,m1,m2,hi) must be the smallest;
               depending on which one is the smallest,
               you recursively call your function on the interval [lo,m2] or [m1,hi]

    >>> argmin(lambda x: (x-5)**2, -20, 20)
    5.000040370009773
    >>> argmin(lambda x: (x-5)**2, -20, 0)
    -0.00016935087808430278
    '''

    print("hi=", hi, "lo=", lo)
    middle = (hi + lo)/2
    # base case
    if hi-lo < epsilon:
        print("returning", hi)
        return hi
    else:
        m1 = middle - middle/10000000000000
        m2 = middle + middle/10000000000000
        print("f(m1)=", f(m1), "f(m2)=", f(m2), "f(lo)=", f(lo), "f(hi)=", f(hi))
        smallest = min(f(m1), f(m2), f(lo), f(hi))
        if f(m2) == smallest or f(hi) == smallest:
            print("[m2,hi]")
            return argmin(f, m2, hi, epsilon)
        if f(m1) == smallest or f(lo) == smallest:
            print("[lo,m1]")
            return argmin(f, lo, m1, epsilon)


epsilon = 1e-6
lo = 0
hi = 1e20
x_min = 5000
f = lambda x: (x-x_min)**2

y =abs(argmin(f,lo,hi,epsilon)-x_min)
print("argmin(f,lo,hi,epsilon)=", argmin(f,lo,hi,epsilon), "and y =", y)
print(y <= epsilon)
# abs(argmin(f,lo,hi,epsilon) - x_min) <= epsilon
