//maximum in the array
class Demo5{
  public static void main(String[] args) {
    int arr[]={2,3,7,4,8};
    int max=0;
    for (int i=0;i<5 ;i++ ) {
      if (max<arr[i]) {
        max=arr[i];
      }

    }System.out.println(max);
  }
}