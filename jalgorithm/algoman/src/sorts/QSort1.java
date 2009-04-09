package sorts;

public class QSort1 implements SortInterface{
	
	private int[] sort_array;
	
	
	public void qsort1(int l,int u){
		
		//First qsort version
		if (l>u)
			return;
		
		int m = l;
		
		for(int i = (l+1);i<=u;i++){
			
			if (this.sort_array[i]<this.sort_array[l]){
				MUtil.swap_array(sort_array, ++m,i);
				//m++;
				//MUtil.print_array(this.sort_array);
			}
		}
		MUtil.swap_array(sort_array, m, l);
		
		
		qsort1(l,m-1);
		//MUtil.print_array(this.sort_array);
		qsort1(m+1,u);
		//MUtil.print_array(this.sort_array);
		
	}
	
	
		public static void main(String [] args){
			
			//pass nothing here
			int[] test_array = {1,-5,6,100,-9,-7};
			QSort1 q = new QSort1();
			q.sort(test_array);
			MUtil.print_array(test_array);
	}

		@Override
		public void sort(int[] array) {
			// TODO Auto-generated method stub
			sort_array = array;
			this.qsort1(0, sort_array.length-1);
		}
	
	}
