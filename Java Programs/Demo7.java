//total of all the array
class Demo7{
  public static void main(String[] args) {
    int arr[]={6,2,3,1,4,7};
    int res=0;
    int n=arr.length;
    for (int i=0;i<n ;i++ ) {
    res+= arr[i];
     }
    System.out.println(res);
    }
}