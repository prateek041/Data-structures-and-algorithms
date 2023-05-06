package learnings.algorithms.sorting;

import java.util.Arrays;

// Pattern: When given numbers range from 1->N, use cyclic sort
public class cycle {
    public static void main(String[] args) {
        int [] numbers = {2,1,3};
        int length = numbers.length;
        int index = 0;
        if (length > 1){
            while(index < length){
                if(numbers[index] != index+1){ // check if the value is at correct index.
                    swap(numbers, index);
                }else{
                    index++;
                }
            }
        }
        System.out.println(Arrays.toString(numbers));
    }

    public static void swap(int[] numbers, int index){
        int correctIndex = numbers[index] -1;
        int temp = numbers[correctIndex];
        numbers[correctIndex] = numbers[index];
        numbers[index] = temp;
    }
}
