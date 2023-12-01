package Day4;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

/**
 * 2018 Advent of Code Day 4
 * Challenge Completion
 * Author: Quinn Kleinfelter
 * Started coding at:
 * Completed at:
 * Code time elapsed:
 */
public class Day4 {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner file = new Scanner(new File("C:/Users/Quinn/Documents/GitHub/AdventOfCode2018/src/Day4/day4input.txt"));
        List<String> lines = new ArrayList<>();
        while(file.hasNextLine()){
            lines.add(file.nextLine());
        }
        part1(lines);
        part2(lines);
    }

    public static void part1(List<String> lines){
        List<Date> dates = new ArrayList<>();
        for(String s : lines) {
            int year = 0; // We can ignore year for this problem since they all occur in 1518 and I don't have to do weird math
            int month = Integer.parseInt(s.substring(6, 8));
            int day = Integer.parseInt(s.substring(8, 10));
            int hrs = Integer.parseInt(s.substring(12, 14));
            int min = Integer.parseInt(s.substring(15, 17));
            dates.add(new Date(year, month, day, hrs, min));
        }
        Collections.sort(dates);
        for(Date d : dates){
            System.out.println(d.toString());
        }
    }

    public static void part2(List<String> lines){

    }
}
