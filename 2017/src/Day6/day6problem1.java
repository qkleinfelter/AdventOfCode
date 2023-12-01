package Day6;

import java.util.Arrays;
import java.util.HashSet;

public class day6problem1 {
    public static void main(String[] args){
       // int[] input = {0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11};
        int[] input = {0,2,7,0};
        HashSet<int[]> priors = new HashSet();
        boolean seenBefore = false;
        int count = 0;
        while(!seenBefore){
            redistributeBlocks(input);
            count++;
            System.out.println(Arrays.toString(input));
            if(!(priors.add(input))){
                seenBefore = true;
            }
        }
        System.out.println(count);
    }
    public static void redistributeBlocks(int[] in){
        int largest = 0;
        for(int i=0; i<in.length; i++){
            if(in[i] > in[largest]){
                largest = i;
            }
        }
        int blocksToDis = in[largest];
        in[largest] = 0;
        int j = largest + 1;
        while(blocksToDis > 0){
            if(j > in.length - 1){j = 0;}
            in[j]++;
            blocksToDis--;
            j++;
        }
    }
}
