package sorts;

public class QSort2 implements SortInterface{

	/**
	 * @param args
	 */
	
	public int partition(int[] sort_array,int left,int right,int pivot_index){
		//the partition part
		int pivot = sort_array[pivot_index];
		
		//move the pivot to the end
		MUtil.swap_array(sort_array, pivot_index, right);
		
		int store_index = left;
		
		for(int i = left;i<right;i++){
			
			if(pivot>=sort_array[i]){
				MUtil.swap_array(sort_array, store_index, i);
				store_index++;
				//MUtil.print_array(sort_array);
			}
			
		}
		MUtil.swap_array(sort_array, right, store_index);
		//MUtil.print_array(sort_array);
		return store_index;
		
	}
	
	public void qsort2(int[] array,int left,int right){
		
		//sorting
		if (right > left){
			
			int pivot_index = (left+right)/2;
			pivot_index = partition(array, left, right, pivot_index);
			qsort2(array, left, pivot_index-1);
			//MUtil.print_array(array);
			qsort2(array, pivot_index+1, right);
		}
		
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//int [] sort_array = {1,-5,6,100,-9,-7};
		int [] sort_array = {1,1,1,1,1,1,-7,-7,-7,-7,-7,-7,12,34,66,33,33,33};
		QSort2 q2 = new QSort2();
		q2.sort(sort_array);
		MUtil.print_array(sort_array);

	}

	@Override
	public void sort(int[] array) {
		// TODO Auto-generated method stub
		this.qsort2(array, 0, array.length-1);
	}

}
