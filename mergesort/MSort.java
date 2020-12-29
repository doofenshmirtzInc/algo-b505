
// Author: Jack McShane
// CSCI-B505 Applied Algorithms
// Lab 4: merge Sort
//
//
//
//this iteration of merge sort is working properly
//have to add in the functionality to read in from the command line args
//
import java.util.Scanner;

public class MSort{
    public static int[] mergeSort(int[] unsorted){
        if(unsorted.length == 1)
            return unsorted;

        int mid = unsorted.length / 2;
        int [] leftHalf = new int[mid];
        int [] rightHalf = new int[(unsorted.length - mid)];
        System.arraycopy(unsorted, 0, leftHalf, 0, mid + 1);
        System.arraycopy(unsorted, mid + 1, rightHalf, 0, unsorted.length - (mid + 1));
        int[] sortedLeft = mergeSort(leftHalf);
        int[] sortedRight = mergeSort(rightHalf);
        int[] sortedWhole = merge(sortedLeft, sortedRight);
        return sortedWhole;
    }


    public static int[] merge(int[] leftHalf, int[] rightHalf){
        int[] sorted = new int[leftHalf.length + rightHalf.length];
        int indexlh = 0;
        int indexrh = 0;
        int index_sortd = 0;

        while((indexlh < leftHalf.length) && (indexrh < rightHalf.length)){
            int elemlh = leftHalf[indexlh];
            int elemrh = rightHalf[indexrh];
            if(elemlh <= elemrh){
                sorted[index_sortd] = leftHalf[indexlh];
                indexlh++;
            }else{
                sorted[index_sortd] = rightHalf[indexrh];
                indexrh++;
            }

            index_sortd++;
        }

        System.arraycopy(leftHalf, indexlh, sorted, index_sortd, leftHalf.length - indexlh);
        System.arraycopy(rightHalf, indexrh, sorted, index_sortd, rightHalf.length - indexrh);

        return sorted;
    }


    public static void main(String[] args){
        //driver code
        Scanner in = new Scanner(System.in);
        int length = in.nextInt();
        int index = 0;
        int[] unsorted = new int[length];
        
        while(in.hasNextInt()){
            unsorted[index] = in.nextInt();
            index++;
        }


        System.out.println("unsorted array:");
        for(int i = 0; i < unsorted.length; i++)
            System.out.print(unsorted[i] + " ");

        int[] sorted = mergeSort(unsorted);
        System.out.println("\nsorted array:");
        for(int j = 0; j < sorted.length; j++)
            System.out.print(sorted[j] + " ");
    }
}
