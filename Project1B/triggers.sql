/*Trigger #1 - A trigger that defaults a restaurants location in Biloxi every time a new restaurant is 
				inserted into the database.*/
DELIMITER $$
CREATE TRIGGER default_loc
AFTER INSERT ON restaurant
FOR EACH ROW
BEGIN
	INSERT INTO rest_locations
    	VALUES('Biloxi', NEW.restid);
END$$
DELIMITER ;

INSERT INTO restaurant(restid,rname,operating_hours)
VALUES (1111222233,'Burgers N Fries','12:00PM-8:00PM');