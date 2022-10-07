/************************************************
* Database Data									*
************************************************/

INSERT INTO restaurant
VALUES (1923568771,'Burgers N Fries','10:00AM-10:00PM'),
	(1234567890,'Burgers N Fries','8:00AM-10:00PM'),
        (9876543210,'Burgers N Fries','10:00AM-12:00AM');

INSERT INTO employee
VALUES('Jan','M','Vincent',123456789,'123 Thornton Ave',30000,'9034567931','M',1923568771),
		('Obi','W','Kenobi',123123123,'456 Tatooine Dr',40000,'7362364836','M',1234567890),
		('Jonathan','S','Wellmeyer',321321321,'876 Louis Str',50000,'8493759375','M',9876543210),
		('Commander','T','Zavala',456456456,'098 Destiny Ave',60000,'0284758384','M',1234567890),
		('Anakin','P','Skywalker',654654654,'836 Mustafar Dr',70000,'8375938475','M',1234567890),
		('Bilbo','B','Baggins',789789789,'898 Shire Str',80000,'9375389575','M',9876543210),
		('Leia','S','Organa',987987987,'936 Alderan Ave',90000,'7395739274','F',1923568771),
		('Luke','M','Skywalker',000011111,'465 Tatooine Dr',20000,'9359284768','M',1923568771),
		('John','M','Wick',111110000,'648 Trenton Str',66000,'1238047594','M',1234567890),
		('Ikora','W','Rey',234234234,'975 Tower Rd',75000,'6543381374','F',1234567890);

INSERT INTO chef
VALUES(123123123),
(654654654);

INSERT INTO cooking_certifications
VALUES(123123123,'A+ Certificate'),
(654654654,'A+ Certificate');

INSERT INTO server
VALUES(456456456,'10'),
(123456789,'20'),
(789789789,'30'),
(321321321,'40'),
(000011111,'50'),
(111110000,'60');

INSERT INTO hostess
VALUES(234234234,'3'),
(987987987,'2');

INSERT INTO busboy
VALUES(456456456,'1'),
(123456789,'1');

INSERT INTO bartender
VALUES(789789789,'1'),
(321321321,'1');

INSERT INTO waiter
VALUES(000011111,25),
(111110000,70);

INSERT INTO rest_locations
VALUES ('Houston',1923568771),
('Ruston',1234567890),
('Farmerville',9876543210);

INSERT INTO customer
VALUES (345678,'John','Martin'),
(123456,'Martha','Stewart'),
(908777,'Andrew','Young');

INSERT INTO atable
VALUES (3,1,4,123456789),
(7,1,5,321321321),
(9,1,2,123456789);

INSERT INTO reserve
VALUES ('Upcoming','2020-01-21',4,'08:00:00',1923568771,345678,3),
		('Done','2020-11-03',2,'02:30:00',1234567890,123456,9),
        ('Done','2020-12-28',5,'05:30:00',9876543210,908777,7);

INSERT INTO menu
VALUES(123456, 'Dr. Pepper', 'Fried Pickles', 'Chicken', 'Ice Cream', 1234567890),
		(246801, 'Coke', 'Cheese Fries', 'Hamburger', 'Brownie', 1923568771);

INSERT INTO item
VALUES(2345, 2, 'Drink', 'Dr. Pepper', 100),
(1567, 6, 'Vegetable', 'Fried Pickles', 50),
(9854, 10, 'Meat', 'Chicken', 30),
(3490, 4, 'Dessert', 'Ice Cream', 23),
(6732, 2, 'Drink', 'Coke', 103),
(1763, 7, 'Vegetable', 'Cheese Fries', 36),
(1302, 8, 'Meat', 'Hamburger', 70),
(4207, 5, 'Dessert', 'Brownie', 42);

INSERT INTO offers
VALUES(2345,123456),
(1567, 123456),
(9854, 123456),
(3490, 123456),
(6732, 123456),
(1763, 123456),
(1302, 123456),
(4207, 123456),
(1567, 246801),
(9854, 246801),
(3490, 246801),
(6732, 246801),
(1763, 246801),
(1302, 246801),
(4207, 246801);