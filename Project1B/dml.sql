/*Inserts Turkey into item table.*/
INSERT INTO item
VALUES(2226,2,'Meat','Turkey',10);

/*Deletes Houston from table rest_locations*/
DELETE FROM rest_locations
WHERE rlocation = 'Houston';

/*Updates Fried Pickles quantity in item table to 5.*/
UPDATE item
SET quantity = 5
WHERE itemid = 1567;

/*Query #1 - Retrieve the first name, last name, and their restaurant id of all the employees who have a salary greater than 50,000.*/
SELECT e.fname, e.lname, e.restaurantid 
FROM employee AS e
WHERE salary > 50000;

/*Query #2 -Retrieve the first name, last name, and their salary of the employees who have a hourly pay greater than 35.*/
SELECT e.fname, e.lname, e.salary
FROM employee AS e, server AS s
WHERE s.hourly_pay > 35 AND e.ssn = s.essn;

/*Query #3 - Retrieve all the items' type and name of the items whose price is less than 7.*/
SELECT i.itype, i.iname
FROM item AS i
WHERE i.price < 7;

/*Query #4 - Retrieve the restaurant's id for the restaurants that have more than 2 employees and return the 
			average salary of the employees working at those restaurants. */
SELECT r.restid, COUNT(*), AVG(e.salary)
FROM restaurant r, employee e
WHERE r.restid = e.restaurantid
GROUP BY r.restid
HAVING COUNT(*) > 2;

/* Query #5 - Retrieve all servers with an hourly pay of greater than 20 */
SELECT e.lname, e.fname
FROM employee e
WHERE (SELECT s.hourly_pay
	   FROM server s
	   WHERE e.Ssn = s.Essn) > 20;