def compute_fibo(which_fibo):
    """
    Computes the which_fibo.th fibonacci number
    """

    first = 0
    second = 1
    sum_fibo = 0
    if which_fibo == 0 or which_fibo == 1:
        return which_fibo

    for f in xrange(1,which_fibo):
        sum_fibo = first + second
        first = second
        second = sum_fibo

    return second

if __name__ == "__main__":
    import sys
    print compute_fibo(int(sys.argv[1]))

