package sorts;

import java.util.Random;

public class MUtil {
	
	public static int[] swap_items(int first,int second){
		
		int tmp = first;
		first = second;
		second = tmp;
		
		return new int[] {first,second};
		
	}
	
	public static void print_array (int[] sortme){
		System.out.println("\n\n");
		for (int tmp:sortme){
			System.out.print("  "+tmp);
			
		}
		System.out.println("\n\n");
	}
	
	public static void swap_array(int[] array,int first,int second){
		
		//sSystem.out.println("I will swap those "+array[first]+" With that "+array[second]);
		int tmp = array[first];
		array[first] = array[second];
		array[second] = tmp;
		
	}
	
	public static int[] generate_array(int how_many,int start,int end){
		
		int [] final_list = new int[how_many];
		Random r = new Random();
		
		for(int i = 0;i<how_many;i++){
			
			long range = (long)end - (long)start + 1;
		    // compute a fraction of the range, 0 <= frac < range
		    long fraction = (long)(range * r.nextDouble());
		    int randomNumber =  (int)(fraction + start);
		    //add it to the end
		    final_list[i]=randomNumber;
		    
			
		}
		return final_list;
		
	}
	
	
	
	public static void main(String[] argv){
		
		int[] mylist;
		mylist = MUtil.generate_array(20, 100, 200);
		MUtil.print_array(mylist);
		
		
	}

}
