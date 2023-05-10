package learnings.algorithms.sorting;

import java.util.Arrays;

// sinking, exchange sort
public class bubble {

    public static void main(String[] args) {
        int [] number = {1,2,3,4,5};
        int length = number.length;
        for(int i=0; i<length ; i++){
            boolean swap = false;
            for (int j = 0; j < length-i-1 ; j++) {
                if(number[j] > number[j+1]){
                    swap(number, j , j+1);
                    swap = true;
                    System.out.println(Arrays.toString(number));
                }
            }
            if (!swap){
                break;
            }
        }
    }

    // when we pass a non-primitive variable to a function as argumnet, we are actually passing the refrence and therefore all the
    // changes are persisted. premitive ones are passed by value.
    public static void swap(int [] number, int x , int y){
        int temp;
        temp = number[x];
        number[x] = number[y];
        number[y] = temp;
    }
}
