// palindrome
class Demo1{
  public static void main(String[] args) {
    int k=12345;
    int sum=0;
    int res;
    int n=5;
    for (int i=0;i<n ;i++ ) {
      res=k%10;
      sum = (sum*10)+res;
      k=k/10;
    }
    System.out.println(sum);
  }
}