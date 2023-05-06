package ArraysAndHashing;

import java.util.Arrays;
import java.util.HashMap;

public class ValidAnagram {
    public static void main(String[] args) {
        String s = "anagram";
        String t = "nagaram";
        System.out.println(isAnagramHash(s, t));
    }

    // This is O(n2) time
    // The issue is when repeated characters are counted again and again, we need a way to mark the ones already checked.
    public static boolean isAnagramBrute(String s, String t){
        int lengthOne = s.length();
        int lengthTwo = t.length();

        // Boundary condition
        if (lengthOne != lengthTwo){
            return false;
        }

        boolean []checkedIndex = new boolean[s.length()];
        for(int i=0; i<lengthOne; i++){
            char character = s.charAt(i);
            boolean found = false;
            for(int j=0; j<lengthTwo ; j++){
                if (character == t.charAt(j)){
                    if(!checkedIndex[j]){
                        found = true;
                        checkedIndex[j] = true; // mark the index that is checked.
                        break;
                    }
                }
            }
            if (!found){
                return false;
            }
        }
        return true;
    }

    // Insertion, merge, quick, bucket, bubble
    public static boolean isAnagramSort(String s, String t){
        if(s.length() != t.length()){
            return false;
        }

        char [] sortedS = sort(s);
        char [] sortedT = sort(t);

        int length = sortedS.length;
        for (int i = 0; i < length; i++) {
            if(sortedS[i] != sortedT[i]){
                return false;
            }
        }
        return true;
    }

    public static  char [] sort(String s){
         char [] charS = s.toCharArray();
         sortChar(charS);
         return charS;
    }

    public static void sortChar(char [] chars){
        Arrays.parallelSort(chars);
    }

    public static boolean isAnagramHash(String s, String t){
        if (s.length() != t.length()){
            return false;
        }
        HashMap<Character, Integer> mapOne = new HashMap<>();
        HashMap<Character, Integer> mapTwo = new HashMap<>();

        char [] strOne = s.toCharArray();
        char [] strTwo = t.toCharArray();

        for (int i = 0; i < s.length(); i++) {
            if(mapOne.containsKey(strOne[i])){
                mapOne.put(strOne[i], mapOne.get(strOne[i]) + 1);
            }else{
                mapOne.put(strOne[i], 1);
            }

            // similarly for second string.
            if(mapTwo.containsKey(strTwo[i])){
                mapTwo.put(strTwo[i], mapTwo.get(strTwo[i])+1);
            }else{
                mapTwo.put(strTwo[i], 1);
            }
        }

        return mapOne.equals(mapTwo);
    }

    // Considering it is only
}
