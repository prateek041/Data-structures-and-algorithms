package learnings.algorithms.sorting;

import java.util.Arrays;

// find max and swap it with any value in the subarray you are checking in.
// This is O(n2) type algorithm
public class selection {
    public static void main(String[] args) {
        int [] numbers = {4,3,1,2,5};
        int length = numbers.length;
        for (int i = 0; i < length; i++) {
            int maxIndex = 0;
            for (int j = 0; j < length-i; j++) {
                if (numbers[maxIndex] < numbers[j]){
                    maxIndex = j;
                }
            }
            swap(numbers, maxIndex, length-i-1);
            System.out.println(Arrays.toString(numbers));
        }
    }

    public static void swap(int [] numbers, int maxIndex, int lastIndex){
        int temp = numbers[maxIndex];
        numbers[maxIndex] = numbers[lastIndex];
        numbers[lastIndex] = temp;
    }
}
