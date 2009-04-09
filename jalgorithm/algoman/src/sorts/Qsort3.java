package sorts;

public class Qsort3 implements SortInterface{
	
	/*
	 * Improvements in that version are :
	 * less swaps
	 * better performance for sorted arrays or identical entries
	 */
	
	private int[] sort_array;
	
	public void qsort3(int l,int u){
		
		if (l>=u)
			return;
		
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
		
		this.qsort3(l, j-1);
		this.qsort3(j+1, u);
	}
	
	
		public static void main(String [] args){
			
			//pass nothing here
			int[] test_array = {1,1,1,1,1,1,-7,-7,-7,-7,-7,-7,12,34,66,33,33,33};
			Qsort3 q = new Qsort3();
			q.sort(test_array);
			MUtil.print_array(test_array);
	}


		@Override
		public void sort(int[] array) {
			// TODO Auto-generated method stub
			sort_array = array;
			this.qsort3(0, sort_array.length-1);
			
		}
}
