//minimum of the array
class Demo6{
  public static void main(String[] args) {
    int arr[]={23,43,3,21,74};
    int min=arr[0];
    for (int i=0;i<arr.length ;i++ ) {
      if (min>arr[i]) {
        min=arr[i];
      }
    }System.out.println(min);
  }
}