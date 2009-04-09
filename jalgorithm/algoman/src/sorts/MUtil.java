package sorts;

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

}
