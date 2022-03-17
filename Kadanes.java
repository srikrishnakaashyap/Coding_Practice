public class Kadanes {

    public int kanades(int arr[]) {
        int length = arr.length;

        int curr_max = arr[0];
        int max_till_here = arr[0];

        for(int i = 1; i < length; i++){

            curr_max = curr_max + arr[i];

            max_till_here = Math.max(max_till_here, curr_max);

            if(curr_max < 0){
                curr_max = 0;
            }
        }
        return max_till_here;
    }



    public static void main(String args[]){

        int arr[] = {-2,1,-3,4,-1,2,1,-5,4};

        Kadanes k = new Kadanes();

        System.out.println(k.kanades(arr));
        
    }
    
}
