public class Main {
    public static void main(String[] args) {
        int[] testArray = {9,8,7,6,5,4,3,2,1,0};
        mergesort(testArray);
        for (int i : testArray) {
        System.out.print(i + " ");
    }
}
    public static void mergesort(int[] array){
        if(array.length < 2)
        return;
        int lenArray = array.length;
        int mid = lenArray / 2;
        int[] left = new int[mid];
        int[] right = new int[lenArray - mid];
        for (int i = 0; i < mid; i++) {
            left[i] = array[i];
        }
        for (int i = mid; i < lenArray; i++) {
            right[i - mid] = array[i];
        }
        mergesort(left);
        mergesort(right);
        int leftI = 0, rightI = 0, arrayI = 0;
        while(leftI < left.length && rightI < right.length){
            if(left[leftI] < right[rightI]){
                array[arrayI] = left[leftI];
                leftI++;
                arrayI++;
            }else{
                array[arrayI] = right[rightI];
                rightI++;
                arrayI++;
            }
        }
        for (; leftI < left.length;leftI++) {
            array[arrayI] = left[leftI];
            arrayI++;
        }
        for (; rightI < right.length; rightI++) {
            array[arrayI] = right[rightI];
        }
    }
}