package Day2;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

import static java.util.Comparator.comparing;

/**
 * 2018 Advent of Code Day 2
 * Challenge Completion
 * Author: Quinn Kleinfelter
 * Started coding at: 4:56pm EST
 * Completed at: 5:44pm EST
 * Code time elapsed: 48 minutes
 */
public class Day2 {
    public static void main(String[] args) throws FileNotFoundException {
        part1();
        part2();
    }

    public static void part1() throws FileNotFoundException {
        int checksum;
        int duplicates = 0, triples = 0;
        Scanner file = new Scanner(new File("C:/Users/Quinn/Documents/GitHub/AdventOfCode2018/src/Day2/day2input.txt"));
        ArrayList<String> ids = new ArrayList<>();
        while(file.hasNext()){
            ids.add(file.next());
        }
        for(String id : ids){
            Map<Character, Integer> freq = new HashMap<>();
            boolean found2 = false, found3 = false;
            for(int i = 0; i < id.length(); i++){
                char c = id.charAt(i);
                freq.put(c, freq.getOrDefault(c,0) + 1);
            }
            for(Map.Entry<Character, Integer> dict : freq.entrySet()){
                if(!found2 && dict.getValue() == 2){
                    duplicates++;
                    found2 = true;
                }if(!found3 && dict.getValue() == 3){
                    triples++;
                    found3 = true;
                }
            }
        }
        checksum = duplicates * triples;
        System.out.println("The checksum for this ID list is " + checksum);
    }

    public static void part2() throws FileNotFoundException {
        int checksum;
        int duplicates = 0, triples = 0;
        Scanner file = new Scanner(new File("C:/Users/Quinn/Documents/GitHub/AdventOfCode2018/src/Day2/day2input.txt"));
        ArrayList<String> ids = new ArrayList<>();
        while(file.hasNext()){
            ids.add(file.next());
        }
        List<String> result = new ArrayList<>();
        for (int i = 0; i < ids.size(); i++) {
            for (int j = i + 1; j < ids.size(); j++) {
                String a = ids.get(i);
                String b = ids.get(j);
                StringBuilder sb = new StringBuilder();
                for (int k = 0; k < a.length(); k++) {
                    if (a.charAt(k) == b.charAt(k)) {
                        sb.append(a.charAt(k));
                    }
                }
                result.add(sb.toString());
            }
        }
        result.stream().sorted(comparing(String::length).reversed())
                .findFirst().ifPresent(System.out::println);
    }
}
