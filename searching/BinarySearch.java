import java.util.Scanner;

public class BinarySearch {
    public static void main(String[] args) {
        
        // Asks the user for the key
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the key");
        int key = scan.nextInt();
        scan.close();

        //output stuff
        int arr[] = {1,2,3,4,5,6,7,8,9};
        // int result = searchRecursive(arr,0,arr.length-1,key);
        int result2 = searchIterrative(arr, key);
        if(result2 != -1){
            System.out.println("Key at index: "+ result2);
        }else{
            System.out.println("nothing found!");
        }
        
    }


    public static int searchIterrative(int arr[], int key){
        
        int low = 0;
        int high = arr.length - 1;
        while(low <= high){
            int mid = low + (high -1) /2;
            if(arr[mid] == key){
                return mid;
            }
            if(arr[mid] < key){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }

        }
        return -1;
    }

    public static int searchRecursive(int arr[], int low, int high, int key){
        
        if(low<=high){

            int mid = low + (high-1)/2;
            if(arr[mid] == key)
                return mid;
            if(arr[mid] > key){
                return searchRecursive(arr, low, mid - 1, key);
            }
            return searchRecursive(arr, mid + 1, high, key);
            

        }

        return -1;
    }
}
