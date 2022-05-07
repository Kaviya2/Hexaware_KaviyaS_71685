// Bubble sort
public class Demo3{
  public static void main(String[] args) {
    int a[]={7,8,3,2,4,1};
    int n=a.length;
    for (int i=0;i<=n ;i++ ) {
      for(int j=0;j<n-1-i;j++){
        if (a[j+1]<a[j]) {
          int temp=a[j+1];
          a[j+1]=a[j];
          a[j]=temp;
        }
      }
    }
    for (int i=0;i<n ;i++ ) {
     System.out.print(a[i]);
    }
  }
}