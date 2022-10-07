import java.io.*;
import java.util.*;

public class Plane
{
    public static void main (String[] args) throws IOException
    {   
        // scanner to read the text file
        Scanner sf = new Scanner(new File("C:\\Users\\jcrav\\Desktop\\Java Programs\\planes.txt"));
        int maxIndx = -1;
        Airplane text[] = new Airplane[29];
        sf.nextLine();
        // divides the text file into parts and converts string numbers to int
        while(sf.hasNext())
        {
            maxIndx++;
            String s = sf.nextLine();
            String[] splitList = s.split(", ");
            int p = Integer.parseInt(splitList[0]);
            String d = splitList[1];
            int day = Integer.parseInt(splitList[2]);
            String m = splitList[3];
            int r = Integer.parseInt(splitList[4]);
            int seats = Integer.parseInt(splitList[5]);
            
            text[maxIndx] = new Airplane(p, d, day, m, r, seats);
        }
        sf.close();
        
        // text menu that accepts user input
        System.out.println("\nMAIN MENU:\n");
        System.out.println("Enter 1 to Add Passenger");
        System.out.println("Enter 2 to List Planes");
        System.out.println("Enter 3 to List Passengers");
        System.out.println("Enter 4 to Display Food Count");
        System.out.println("Enter 5 to Find Passenger");
        System.out.println("Enter 6 to Quit");
        Scanner input = new Scanner(System.in);
        int number = input.nextInt();
        
        // insertion sort to organize planes numerically by ID
        int n = text.length-1; 
        for (int i = 1; i < n; i++) 
        { 
            int key = text[i].getPlaneNum();
            Airplane pl = text[i];
            int j = i - 1; 
  
            while (j >= 0 && text[j].getPlaneNum() > key) { 
                text[j + 1] = text[j]; 
                j = j - 1; 
            } 
            text[j + 1] = pl; 
        }  
        
        Scanner sf2 = new Scanner(new File("C:\\Users\\jcrav\\Desktop\\Java Programs\\bookings.txt"));
        maxIndx = -1;
        sf2.nextLine();
        while(sf2.hasNextLine())
        {
            maxIndx++;
            String s = sf2.nextLine();
            String[] splitList = s.split(",");
            int p = Integer.parseInt(splitList[0]);
            String name = splitList[1];
            String food = splitList[2];
            int row = Integer.parseInt(splitList[3]);
            int seat = Integer.parseInt(splitList[4]);
            int result = 0;
            int x = p;
            int l = 0;
            int r = text.length - 1; 
            int m = 0;
            while (l <= r) 
            { 
                try
                {
                    m = (l + r) / 2; 
                    int w = text[m].getPlaneNum();
                    // check if x is present at mid 
                    if (text[m].getPlaneNum() == x) 
                    {
                         result = m; 
                    }
          
                    // if x greater, ignore left half 
                    if (text[m].getPlaneNum() < x) 
                    {
                        l = m + 1;
                    }
          
                    // if x is smaller, ignore right half 
                    else
                    {
                        r = m - 1;
                    }
                }
                catch(Exception e)
                {
                    break;
                }
            }
            text[result].setBookings(name, food, row, seat);
        }
        sf.close();
        
        // lets the user enter the plane number for certain menu options
        int plnum = 0;
        if (number == 1 || number == 3 || number == 4 || number == 5) 
        {
            // got binary search code from: https://www.geeksforgeeks.org/java-program-for-binary-search-recursive-and-iterative/
            System.out.println("What is the plane ID?");
            Scanner input2 = new Scanner(System.in);
            int result = 0;
            int x = input2.nextInt();
            int l = 0;
            int r = text.length - 1; 
            while (l <= r) 
            { 
                try
                {
                    int m = l + (r - l) / 2; 
          
                    // check if x is present at mid 
                    if (text[m].getPlaneNum() == x) 
                    {
                         result = m; 
                    }
          
                    // if x greater, ignore left half 
                    if (text[m].getPlaneNum() < x) 
                    {
                        l = m + 1;
                    }
          
                    // if x is smaller, ignore right half 
                    else
                    {
                        r = m - 1;
                    }
                }
                catch(Exception e)
                {
                    break;
                }
            }
            // notifies the user if the plane is not found
            if (x != text[result].getPlaneNum())
            {
                System.out.println("\n");
                System.out.println("Plane not found");
            }
            else
            {
               plnum = result;
            }
        }
        
        // press 1 to add a new passenger to a plane
        if(number == 1)
        {
            // lets the user know if the plane they chose is full and tries to find a new plane with the same destination
            if(text[plnum].isFull() == true)
            {
                System.out.println("Plane is full. Finding new plane...");
                boolean full = false;
                for (int i = 0; i < n; i++) 
                {   full = text[i].isFull();
                    if(text[i].getDestination().equals(text[plnum].getDestination()) && full == false) plnum = i;
                    else System.out.println("No planes available");
                }
                System.out.println("New plane available is "+text[plnum].getPlaneNum());
                System.out.println("Available seats:");
                text[plnum].isAvailable();
            }
            System.out.println("Please enter the passenger information:");
            
            System.out.println("What is your name?");
            Scanner input3 = new Scanner(System.in);
            String name = input3.next();
            
            System.out.println("Would you like chicken, pasta, or the special? ");
            Scanner input4 = new Scanner(System.in);
            String food = input4.next();
            
            System.out.println("What row would you like to sit on?");
            Scanner input5 = new Scanner(System.in);
            int row = input5.nextInt();
            
            System.out.println("What seat would you like to sit in?");
            Scanner input6 = new Scanner(System.in);
            int seat = input6.nextInt();
            
            text[plnum].setBookings(name, food, row, seat);
            
            // lets the user pick another spot if the spot they chose is booked
            int b = text[plnum].isBooked(row, seat);
            if(b == 1)
            {
                System.out.println("That spot is already taken. Please choose another row and seat.");
                System.out.println("Available seats:");
                text[plnum].isAvailable();
                System.out.println("What row would you like to sit on?");
                Scanner input7 = new Scanner(System.in);
                row = input7.nextInt();
                
                System.out.println("What seat would you like to sit in?");
                Scanner input8 = new Scanner(System.in);
                seat = input8.nextInt();
                text[plnum].setBookings(name, food, row, seat);
                System.out.println("Passenger information added");
            }
            else System.out.println("Passenger information added");
        }
        
        // press 2 to print the sorted plane list
        if (number == 2) 
        {   
            int avbl = 0;
            for (int i = 0; i < n; i++) 
            {   
                boolean full = false;
                avbl = text[i].countPassengers();
                full = text[i].isFull();
                System.out.print(text[i]);
                System.out.print("\t"+avbl);
                if(full == true) System.out.println("\tFull");
                else System.out.println("");
            }
        }
        
        // press 3 to list passengers in a plane
        if(number == 3)
        {
            text[plnum].listPassengers();
        }
            
        // press 4 to list all food requests in a plane
        if(number == 4)
        {
            System.out.println(text[plnum].foodCount());
        }
        
        // press 5 to find a passsenger in a plane
        if(number == 5)
        {
            System.out.println(text[plnum].findPassenger());
        }
        
        // press 6 to exit the program
        if (number == 6) 
        {
            System.out.println("\nShutting Down");
            System.exit(0);
        }
        
        // closes the scanner object
        input.close();
    }   
}   