package sorts;

import java.math.BigInteger;

public class FiboMan {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long fibo_num;
		
		BigInteger first_num;
		BigInteger second_num;
		BigInteger tmp;
		
		first_num = new BigInteger("0");
		second_num = new BigInteger("1");
		fibo_num=0;
		//convert to a long
		try{
		//System.out.println("The argv is "+args[0]);
		fibo_num = Long.parseLong(args[0].trim());
		}
		catch (Exception e) {
			// TODO: handle exception
		}
		
		
		if(fibo_num == 0 || fibo_num == 1){
			System.out.println("The fibo result is :"+fibo_num);
			System.exit(0);
		}
		
		for(long i=1; i< fibo_num;i++){
			tmp=first_num.add(second_num);
			first_num = second_num;
			second_num = tmp;
		}

		System.out.println("The fibo result is :"+second_num);
	}

	
}
