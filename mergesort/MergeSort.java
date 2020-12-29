// Author: Jack McShane
// CSCI-B505 Applied Algorithms
// Lab 4: Merge Sort
//
//
//
//this iteration of merge sort is working properly
//have to add in the functionality to read in from the command line args
//
import java.util.Scanner;

public class MergeSort{
    public static void mergesort(int[] a, int[] temp, int leftStart, int rightEnd){
        if(leftStart >= rightEnd){
            return;
        }
        int middle = (leftStart + rightEnd) / 2;
        mergesort(a, temp, leftStart, middle);
        mergesort(a, temp, middle + 1, rightEnd);
        mergeHalves(a, temp, leftStart, rightEnd);
    }



    public static void mergeHalves(int[] a, int[] temp, int leftStart, int rightEnd){
        int leftEnd = (rightEnd + leftStart) / 2;
        int rightStart = leftEnd + 1;
        int size = rightEnd - leftStart + 1;

        int left = leftStart;
        int right = rightStart;
        int index = leftStart;

        while(left <= leftEnd && right <= rightEnd){
            if(a[left] <= a[right]){
                temp[index] = a[left];
                left++;
            }else{
                temp[index] = a[right];
                right++;
            }
            index++;
        }

        System.arraycopy(a, left, temp, index, leftEnd - left + 1);
        System.arraycopy(a, right, temp, index, rightEnd - right + 1);
        System.arraycopy(temp, leftStart, a, leftStart, size);
    }



    public static void main(String[] args){
        Scanner in = new Scanner(System.in);
        int[] a = new int[10];

        int array_length = in.nextInt();
        int[] array = new int[array_length];
        int index = 0;
        while(in.hasNextInt() && index < array_length){
            array[index] = in.nextInt();
            index++;
        }

        mergesort(array, new int[array.length], 0, array.length - 1);
        for(int i = 0; i < array.length; i++)
            System.out.println(array[i]);
    }
}
