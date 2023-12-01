package Day3;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * 2018 Advent of Code Day 3
 * Challenge Completion
 * Author: Quinn Kleinfelter
 * Started coding at:
 * Completed at:
 * Code time elapsed:
 */
public class Day3 {
    private static int[][] grid = new int[1000][1000];
    public static void main(String[] args) throws FileNotFoundException {
        Scanner file = new Scanner(new File("C:/Users/Quinn/Documents/GitHub/AdventOfCode2018/src/Day3/day3input.txt"));
        ArrayList<String> lines = new ArrayList<>();
        while(file.hasNextLine()){
            lines.add(file.nextLine());
        }
        part1(lines);
        part2(lines);
    }

    public static void part1(List<String> lines){
        Pattern numberPattern = Pattern.compile("\\d+");
        for (String str: lines) {
           List<Integer> numbers=  new ArrayList<>();
            Matcher numberMatcher  = numberPattern.matcher(str);
            while (numberMatcher.find()){
                numbers.add(Integer.parseInt(numberMatcher.group()));
            }
            for(int i =numbers.get(1);i<numbers.get(1)+numbers.get(3);i++){
                for(int j =numbers.get(2);j<numbers.get(2)+numbers.get(4);j++){
                    grid[i][j]+=1;
                }
            }
        }
        int count = 0;
        for(int i = 0; i < 1000; i++){
            for (int j = 0; j < 1000; j++){
                if(grid[i][j] >= 2){
                    count++;
                }
            }
        }

        System.out.println("Overlapping grids: " + count);
    }

    public static void part2(ArrayList<String> lines){
        Pattern numberPattern = Pattern.compile("\\d+");
        for (String str: lines){
            boolean flag = true;
            List<Integer> numbers=  new ArrayList<>();
            Matcher numberMatcher  = numberPattern.matcher(str);
            while (numberMatcher.find()){
                numbers.add(Integer.parseInt(numberMatcher.group()));
            }
            for(int i =numbers.get(1);i<numbers.get(1)+numbers.get(3);i++){
                for(int j =numbers.get(2);j<numbers.get(2)+numbers.get(4);j++){
                    if(grid[i][j] > 1){
                        flag = false;
                    }
                }
            }
            if(flag){
                System.out.println(numbers.get(0));
            }
        }

    }
}
