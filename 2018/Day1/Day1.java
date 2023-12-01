package Day1;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

/**
 * 2018 Advent of Code Day 1
 * Challenge Completion
 * Author: Quinn Kleinfelter
 * Started coding at: 8EST
 * Completed at: 8:24EST
 * Code time elapsed: 24 minutes
 */
public class Day1 {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner file = new Scanner(new File("C:/Users/Quinn/Documents/GitHub/AdventOfCode2018/src/Day1/day1input.txt"));
        ArrayList<Integer> nums = new ArrayList<>();
        while(file.hasNext()){
            nums.add(Integer.parseInt(file.next()));
        }
        int freq = 0;
        HashSet<Integer> freqs = new HashSet();
        freqs.add(freq);
        boolean freqFound = false;
        int i = 0;
        while(!freqFound){
//        for(int i : nums){

            freq += nums.get(i);
            if(!freqs.contains(freq)){
                freqs.add(freq);
            }else{
                System.out.println("reached " + freq + " twice");
                freqFound = true;
            }
            if (i == nums.size() - 1) {
                i = 0;
            }else{
                i++;
            }
        }
        System.out.println(freq);
    }
}
