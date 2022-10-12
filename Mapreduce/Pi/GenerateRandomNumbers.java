import java.util.Scanner;

public class GenerateRandomNumbers {
        public static void main(String[] args) {
                System.out.println("How many random numbers to generate:");
                Scanner input =new Scanner(System.in);
                int RandomNumCount = input.nextInt();

                System.out.println("What's the radius number?");
                int radius = input.nextInt();
                int diameter = radius * 2;

                int num[]= new int[RandomNumCount];
    for(int i=0; i<RandomNumCount; i++){

      num[i]= (int) (Math.random()* diameter);
      System.out.print(num[i]+" ");
                }
        }}
                 
