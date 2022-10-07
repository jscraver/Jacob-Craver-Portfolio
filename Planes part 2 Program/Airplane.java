import java.io.*;
import java.util.*;

// class to store plane inforamtion
public class Airplane
{
    private int PlaneNum;
    private String Destination;
    private int DayOfTravel;
    
    private boolean HasMeal;
    private int NumOnPlane;
    private int MaxSeats;
    
    private Passenger[][] Bookings;
    
    public Airplane()
    {
        PlaneNum = 0;
        Destination = "";
        DayOfTravel = 0;
    }
    public Airplane(int n, String d, int day, String m, int r, int s)
    {
        PlaneNum = n;
        Destination = d;
        DayOfTravel = day;
        if(m.equals("yes"))
            HasMeal = true;
        else
            HasMeal = false;
        NumOnPlane = 0;
        MaxSeats = r*s;
       
        Bookings = new Passenger[r][s];
    }
    
    // method to set bookings
    public void setBookings(String name, String food, int r, int s) 
    {
        if((r<=Bookings.length) && (s<=Bookings[0].length) && isEmpty(r, s))
        Bookings[r-1][s-1] = new Passenger(name, food);
    }
       
    // method to see if a spot on a plane is empty
    public boolean isEmpty(int r, int s)
    {
        if(Bookings[r-1][s-1]==null) return true;
        else return false;
    }
    
    // method to count food requests on a plane
    public String foodCount()
    {
        int chik = 0;
        int pasta = 0;
        int special = 0;
        String fp = "";
        for(int i = 0; i < Bookings.length; i++)
        {
           for (int j = 0; j < Bookings[0].length; j++)
           {
               if (!isEmpty(i+1, j+1))
               {
                   fp = Bookings[i][j].getFoodPreference();
                   if (fp.equals("chicken")) chik++;
                   if (fp.equals("pasta")) pasta++;
                   if (fp.equals("special")) special++;
               }   
            }
        }
        if (HasMeal)
            return("Chicken = "+chik+" Pasta = "+pasta+" Special = "+special);
        else
            return("Snacks = "+(chik+pasta+special));
    }
    
    // method to list the passengers on a plane
    public String listPassengers()
    {
        String name = "";
        int row = 0;
        int seat = 0;
        for(int i = 0; i < Bookings.length; i++)
        {
           for (int j = 0; j < Bookings[0].length; j++)
           {
               if (!isEmpty(i+1, j+1)) 
               {
                   name = Bookings[i][j].getName();
                   row = i+1;
                   seat = j+1;
                   System.out.println("Name = "+name+" Row = "+row+" Seat = "+seat);
               }
           }
        }
        return "Error";
    }
    
    // method to find a passenger on a plane
    public String findPassenger()
    {
        System.out.println("What is the passenger's name?");
        Scanner input = new Scanner(System.in);
        String x = input.next();
        String name = "";
        int row = 0;
        int seat = 0;
        for(int i = 0; i < Bookings.length; i++)
        {
           for (int j = 0; j < Bookings[0].length; j++)
           {
                if (!isEmpty(i+1, j+1)) {
                name = Bookings[i][j].getName();
                if (name.equals(x))
                {
                    row = i+1;
                    seat = j+1;
                    return("Row = "+row+" Seat = "+seat);
                }
                }
           }
        }
        return("Passenger not found");
    }
    
    // method to count the passengers on a plane
    public int countPassengers()
    {
        int counter = 0;
        for(int i = 0; i < Bookings.length; i++)
        {
           for (int j = 0; j < Bookings[0].length; j++)
           {
               if (!isEmpty(i+1, j+1)) 
               {
                   counter += 1;
               }
           }
        }
        return counter;
    }
    
    // method to see if a plane is full
    public boolean isFull()
    {
        int counter = 0;
        for(int i = 0; i < Bookings.length; i++)
        {
           for (int j = 0; j < Bookings[0].length; j++)
           {
               if (!isEmpty(i+1, j+1)) 
               {
                   counter += 1;
               }
           }
        }
        if(counter == MaxSeats) return true;
        else return false;
    }
    
    // method to see if a spot on a plane is already booked
    public int isBooked(int i, int j)
    {
        if (!isEmpty(i+1, j+1)) return 1;
        else return 0;
    }
        
    // method to see what spots on a plane are available to be booked
    public int isAvailable()
    {
        int row = 0;
        int seat = 0;
        for(int i = 0; i < Bookings.length; i++)
        {
           for (int j = 0; j < Bookings[0].length; j++)
           {
               if (isEmpty(i+1, j+1)) 
               {
                   row = i+1;
                   seat = j+1;
                   System.out.println("Available: Row = "+row+" Seat = "+seat);
               }
           }
        }
        return 0;
    }
    
    public int getPlaneNum()
    {
        return this.PlaneNum;
    }
    public void setPlaneNum()
    {
        this.PlaneNum = PlaneNum;
    }
    
    public String getDestination()
    {
        return this.Destination;
    }
    public void setDestination()
    {
        this.Destination = Destination;
    }
    
    public int getDayOfTravel()
    {
        return this.DayOfTravel;
    }
    public void setDayOfTravel()
    {
        this.DayOfTravel = DayOfTravel;
    }
    
    public boolean getHasMeal()
    {
        return this.HasMeal;
    }
    public void setHasMeal()
    {
        this.HasMeal = HasMeal;
    }
    
    public int getMaxSeats()
    {
        return this.MaxSeats;
    }
    public void setMaxSeats()
    {
        this.MaxSeats = MaxSeats;
    }
    
    public int getNumOnPlane()
    {
        return this.NumOnPlane;
    }
    
    // prints the plane information in the correct format
    public String toString()
    {
        return(PlaneNum+"\t"+Destination+"\t"+DayOfTravel);
    }
}
