import fibo
import sys

if __name__ == "__main__":
    
    if sys.argv[1] == "iter":
        result =  fibo.iter_fibo(int(sys.argv[2]))
    else :
        result =  fibo.rec_fibo(int(sys.argv[2]))
        print "The recursive result is :",result
        sys.exit(0)
    
    f = open("fibo.txt","w")
    #print "The type of the result is : ",type(result)
    #print "The type of the result is : ",result.__repr__()
    f.write(str(result))
    f.close()
    print "Result written into fibo.txt"
    
