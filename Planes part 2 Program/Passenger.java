import java.io.*;
import java.util.*;

// class to store passenger inforamtion
public class Passenger extends Plane
{
    private String Name;
    private String FoodPreference;
    
    public Passenger()
    {
        Name = "empty";
        FoodPreference = "none";
    }
    public Passenger(String n, String f)
    {
        Name = n;
        FoodPreference = f;
    }
    
    public String getName()
	{
		return this.Name;
	}
    public void setPlaneNum(String n)
    {
    	this.Name = Name;
    }
    
    public String getFoodPreference()
	{
		return this.FoodPreference;
	}
    public void setFoodPreference(String f)
    {
    	this.FoodPreference = FoodPreference;
    }
    
    // prints the passenger information in the correct format
    public String toString()
    {
        return(Name+"\t"+FoodPreference);
    }
}
