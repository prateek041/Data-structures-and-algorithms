package ArraysAndHashing;

import java.sql.Array;
import java.util.*;

public class GroupAnagram{
    public static void main(String[] args) {
        String [] str = {"eat","tea","tan","ate","nat","bat"};
        System.out.println(groupAnagram(str));
    }

    public static void groupAnagramBrute(String [] original){
        String [] input = new String[original.length];
        System.arraycopy(original, 0, input, 0, original.length);
        sort(input);
        List<List<String>> result = new ArrayList<>();
        result = checkAnagrams(original, input);
        System.out.println(result);
    }

    public static List<List<String>> checkAnagrams(String [] original, String [] input){
        List<List<String>> list = new ArrayList<>();
        boolean [] checked = new boolean[input.length];
        for (int i = 0; i < input.length; i++) {
            List<String> wordList = new ArrayList<>();
            String word = input[i];
            for (int j = i; j < input.length; j++) {
                if(word.equals(input[j])){
                    if(!checked[j]) {
                        wordList.add(original[j]);
                        checked[j] = true;
                    }
                }
            }
            if(!wordList.isEmpty()) {
                list.add(wordList);
            }
        }
        return list;
    }

    public static void sort(String [] input){
        for (int i = 0; i<input.length; i++){
            // creating a character array
            char [] charArr = input[i].toCharArray();
            // sorting the array
            Arrays.sort(charArr);
            // Converting it back to string
            String newWord = new String(charArr);
            input[i] = newWord;
        }
    }

    public static List<List<String>> groupAnagram(String [] str){
        HashMap<String, List<String>> map = new HashMap<>(); // creating a hashmap.
        for(String word : str){
            char [] arr = word.toCharArray();
            // sort
            Arrays.sort(arr);
            String key = new String(arr); // Now this sorted string is the key for the hashmap
            if(map.containsKey(key)){
                List<String> list = map.get(key);
                list.add(word);
                map.replace(key, list);
            }else{
                List<String> newList = new ArrayList<>();
                newList.add(word);
                map.put(key, newList);
            }

        }
        return new ArrayList<>(map.values());
    }
}
