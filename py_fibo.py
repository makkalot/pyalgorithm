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

def compute_fibo_rec(fib_num):
    
    if fib_num == 0 or fib_num == 1:
        return fib_num

    return compute_fibo_rec(fib_num-1) +compute_fibo_rec(fib_num-2)

if __name__ == "__main__":
    import sys
    """
    result = compute_fibo(int(sys.argv[1]))
    f = open("fibo.txt","w")
    f.write(str(result))
    f.close()
    print "Result written into fibo.txt"
    """

    result = compute_fibo_rec(int(sys.argv[1]))
    print "The result is : ",result
    sys.exit(0)
    f = open("fibo.txt","w")
    f.write(str(result))
    f.close()
    print "Result written into fibo.txt"

    
