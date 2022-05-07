//lentgth of the string 
class Demo8{
  public static void main(String[] args) {
    String s="KaviyaSaravanan";
   char[] c=s.toCharArray();
   int count=0;
   for (char ch: c ) {
     count++;
   }System.out.println(count);
  }
}