package sorts;

import java.io.FileOutputStream;
import java.io.IOException;
import java.math.BigInteger;

public class FiboMan {

	/**
	 * @param args
	 */
	public static long rec_fib(long fibo_num){
		
		if (fibo_num == 0 || fibo_num == 1)
			return fibo_num;
		
		return rec_fib(fibo_num-1) + rec_fib(fibo_num-2);
		
	}
	
	public static void iter_fib(long fibo_num){

		
		BigInteger first_num;
		BigInteger second_num;
		BigInteger tmp;
		
		first_num = new BigInteger("0");
		second_num = new BigInteger("1");
		
		//convert to a long
		
		if(fibo_num == 0 || fibo_num == 1){
			System.out.println("The fibo result is :"+fibo_num);
			System.exit(0);
		}
		
		for(long i=1; i< fibo_num;i++){
			tmp=first_num.add(second_num);
			first_num = second_num;
			second_num = tmp;
		}

		try{
		FileOutputStream fo = new FileOutputStream("fib.txt");
		fo.write(second_num.toString().getBytes());
		System.out.println("The fibo result is :written to fib.txt");
		}
		catch (IOException e) {
			// TODO: handle exception
			System.exit(0);
		}
		
	}
	
	public static void main(String[] args) throws IOException{
		// TODO Auto-generated method stub
		long fibo_num;
		String type_method = new String("empty");
		
		fibo_num=0;
		//convert to a long
		try{
		//System.out.println("The argv is "+args[0]);
			type_method = args[0].trim();
			fibo_num = Long.parseLong(args[1].trim());

			if(type_method.equals("iter")==true)
				FiboMan.iter_fib(fibo_num);
			else{
				fibo_num = FiboMan.rec_fib(fibo_num);
				System.out.println("The recursive result is "+fibo_num);
			}

		}
		catch (Exception e) {
			// TODO: handle exception
		}
		
			
	}

	
}
