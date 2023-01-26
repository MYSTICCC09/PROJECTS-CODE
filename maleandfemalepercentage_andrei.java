package javafundamentals;

import java.util.Scanner;

public class maleandfemalepercentage_andrei {

	    public static void main(String args[]){
	    
	        Scanner input = new Scanner(System.in);
	        float maleAmount;
	        float femaleAmount;
	        float total;
	        float malePercent;
	        float femalePercent;
	        String malePercentString;
	        String femalePercentString;

	        System.out.println();
	        System.out.print("Enter How Many Male Students are in the class: ");
	        maleAmount = input.nextInt();

	        System.out.print("Enter How Many Female Students are in the class: "); 
	        femaleAmount = input.nextInt();
	        input.close();

	        total = maleAmount + femaleAmount;
	        malePercent = (maleAmount/total)*100;
	        femalePercent = (femaleAmount/total)*100;
	        malePercentString = String.format("%.02f", malePercent);
	        femalePercentString = String.format("%.02f", femalePercent);

	        System.out.println();
	        System.out.println("Total Number of Students: " + (int)total);
	        System.out.println("Male Students: " + (int)maleAmount + " / " + (int)total);
	        System.out.println("Female Students: " + (int)femaleAmount + " / " + (int)total);
	        System.out.println("Percentage of Male Students: " + malePercentString + " %");
	        System.out.println("Percentage of Female Students: " + femalePercentString + " %");
	        System.out.println();
	        
	        /* Submitted By: Andrei N. Capili (BSCPE 1-1) */ 
	    }
	}
