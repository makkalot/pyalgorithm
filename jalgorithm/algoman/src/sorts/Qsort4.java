package sorts;

import java.util.Random;

public class Qsort4 implements SortInterface{
	
	/*
	 * Improvements in that version are :
	 * less swaps
	 * better performance for sorted arrays or identical entries
	 */
	
	private int[] sort_array;
	//private final int CUT_OFF = 5;
	
	public void qsort4(int l,int u){
		
		if (l>=u)
			return;
		
		//first make l random not the first member in the array
		Random r = new Random();
		long range = (long)u - (long)l + 1;
	    // compute a fraction of the range, 0 <= frac < range
	    long fraction = (long)(range * r.nextDouble());
	    int randomNumber =  (int)(fraction + l);
	    
	    //pull one from rand
	    MUtil.swap_array(sort_array, l, randomNumber);
		
		int i = l;
		int t = sort_array[l]; //the place we will divide the stuff
		int j = u+1;
		
		//the main loop
		while(true){
			
			do{
				i++;
			}while (i<=u && sort_array[i]<t  );
			
			do{
				
				j--;
				
			}while(sort_array[j]>t);
			
			if (i>j)
				break;
			
			MUtil.swap_array(sort_array, i, j);
		}
		//put the t to its real place
		MUtil.swap_array(sort_array, j, l);
		
		this.qsort4(l, j-1);
		this.qsort4(j+1, u);
	}
	
	
		public static void main(String [] args){
			
			//pass nothing here
			int[] test_array = {1,1,1,1,1,1,-7,-7,-7,-7,-7,-7,12,34,66,33,33,33};
			Qsort4 q = new Qsort4();
			q.sort(test_array);
			MUtil.print_array(test_array);
	}


		@Override
		public void sort(int[] array) {
			// TODO Auto-generated method stub
			sort_array = array;
			this.qsort4(0, sort_array.length-1);
			
		}
}