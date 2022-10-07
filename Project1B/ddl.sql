CREATE DATABASE restaurants;
USE restaurants;

/************************************************
* Creation of Tables							*
************************************************/

DROP TABLE IF EXISTS employee;
CREATE TABLE employee (
	fname VARCHAR(15) NOT NULL,
	minit CHAR,
	lname VARCHAR(15) NOT NULL,
	ssn INT(9) NOT NULL,
	address VARCHAR(45) NOT NULL,
	salary INT(7) NOT NULL,
	phone_number VARCHAR(10) NOT NULL,
	sex CHAR(1) NOT NULL,
	restaurantid BIGINT(15) NOT NULL,
	CONSTRAINT empl_pk
		PRIMARY KEY (ssn)
);

DROP TABLE IF EXISTS chef;
CREATE TABLE chef (
	essn INT(9) NOT NULL,
	CONSTRAINT chef_pk
		PRIMARY KEY (essn)
);

DROP TABLE IF EXISTS cooking_certifications;
CREATE TABLE cooking_certifications (
	essn INT(9) NOT NULL,
	ccertificate VARCHAR(20),
	CONSTRAINT cookcert_pk
		PRIMARY KEY (essn)
);

DROP TABLE IF EXISTS server;
CREATE TABLE server (
	essn INT(9) NOT NULL,
	hourly_pay VARCHAR(10) NOT NULL,
	CONSTRAINT serv_pk
		PRIMARY KEY (essn)
);

DROP TABLE IF EXISTS hostess; 
CREATE TABLE hostess (
	essn INT(9) NOT NULL,
	work_experience VARCHAR(15) NOT NULL,
	CONSTRAINT host_pk
		PRIMARY KEY (essn)
);

DROP TABLE IF EXISTS busboy;
CREATE TABLE busboy (
	essn INT(9) NOT NULL,
	work_experience VARCHAR(15) NOT NULL,
	CONSTRAINT busb_pk
		PRIMARY KEY (essn)
);

DROP TABLE IF EXISTS bartender;
CREATE TABLE bartender (
	essn INT(9) NOT NULL,
	liquor_license VARCHAR(20) NOT NULL,
	CONSTRAINT bart_pk
		PRIMARY KEY (essn)
);

DROP TABLE IF EXISTS waiter; 
CREATE TABLE waiter (
	essn INT(9) NOT NULL,
	tips INT(4) NOT NULL,
	CONSTRAINT wait_pk
		PRIMARY KEY (essn)
);

DROP TABLE IF EXISTS restaurant;
CREATE TABLE restaurant (
	restid BIGINT(45) NOT NULL,
	rname VARCHAR(15) NOT NULL,
	operating_hours VARCHAR(15) NOT NULL,
	CONSTRAINT rest_pk
		PRIMARY KEY (restid)
);

DROP TABLE IF EXISTS rest_locations;
CREATE TABLE rest_locations (
	rlocation VARCHAR(15) NOT NULL,
	rid BIGINT(15) NOT NULL, 
	CONSTRAINT restloca_pk
		PRIMARY KEY (rlocation,rid)
);

DROP TABLE IF EXISTS customer;
CREATE TABLE customer (
	custid BIGINT(15) NOT NULL,
	fname VARCHAR(15) NOT NULL,
	lname VARCHAR(15) NOT NULL,
	CONSTRAINT cust_pk
		PRIMARY KEY (custid)
);

DROP TABLE IF EXISTS atable; 
CREATE TABLE atable (
	table_number TINYINT(2) NOT NULL,
	min_size TINYINT(2) NOT NULL,
	max_size TINYINT(2) NOT NULL,
	essn INT(9) NOT NULL,
	CONSTRAINT atab_pk
		PRIMARY KEY (table_number,essn)
);

DROP TABLE IF EXISTS reserve;
CREATE TABLE reserve (
	status VARCHAR(15) NOT NULL,
	rdate DATE NOT NULL,
	party_size TINYINT(2) NOT NULL,
	rtime TIME NOT NULL,
	restid BIGINT(15) NOT NULL,
	custid BIGINT(15) NOT NULL,
	tblnum TINYINT(2) NOT NUll,
	CONSTRAINT rese_pk
		PRIMARY KEY (restid,custid,tblnum)
);

DROP TABLE IF EXISTS menu;
CREATE TABLE menu (
	menuid BIGINT(15) NOT NULL,
	drink VARCHAR(15) NOT NULL,
	appetizer VARCHAR(15) NOT NULL,
	entree VARCHAR(15) NOT NULL,
	dessert VARCHAR(15) NOT NULL,
	restid BIGINT(15) NOT NULL,
	CONSTRAINT menu_pk
		PRIMARY KEY (menuid,restid)
);

DROP TABLE IF EXISTS offers;
CREATE TABLE offers (
	item_id BIGINT(15) NOT NULL,
	menu_id BIGINT(15) NOT NULL,
	CONSTRAINT offe_pk
		PRIMARY KEY (item_id,menu_id)
);

DROP TABLE IF EXISTS item;
CREATE TABLE item (
	itemid BIGINT(15) NOT NULL,
	price TINYINT(2) NOT NULL,
	itype VARCHAR(15) NOT NULL, 
	iname VARCHAR(20) NOT NULL,
	quantity INT(4) NOT NULL,
	CONSTRAINT item_pk
		PRIMARY KEY (itemid)
);

/************************************************
* Creation of Foreign Keys						*
************************************************/

ALTER TABLE employee
ADD CONSTRAINT empl_rest_fk
	FOREIGN KEY (restaurantid) REFERENCES restaurant(restid)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;
		
ALTER TABLE chef
ADD CONSTRAINT chef_essn_fk
	FOREIGN KEY (essn) REFERENCES employee(ssn)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;
		
ALTER TABLE server
ADD CONSTRAINT serv_essn_fk
	FOREIGN KEY (essn) REFERENCES employee(ssn)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;
		
ALTER TABLE hostess
ADD CONSTRAINT host_essn_fk
	FOREIGN KEY (essn) REFERENCES employee(ssn)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;
		
ALTER TABLE cooking_certifications
ADD CONSTRAINT cook_cert_essn_fk
	FOREIGN KEY (essn) REFERENCES chef(essn)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;
		
ALTER TABLE busboy
ADD CONSTRAINT busb_essn_fk
	FOREIGN KEY (essn) REFERENCES server(essn)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;

ALTER TABLE bartender
ADD CONSTRAINT bart_essn_fk
	FOREIGN KEY (essn) REFERENCES server(essn)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;
		
ALTER TABLE waiter
ADD CONSTRAINT wait_essn_fk
	FOREIGN KEY (essn) REFERENCES server(essn)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;

ALTER TABLE rest_locations
ADD CONSTRAINT rest_loca_rid_fk
	FOREIGN KEY (rid) REFERENCES restaurant(restid)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;
		
ALTER TABLE atable
ADD CONSTRAINT atab_essn_fk
	FOREIGN KEY (essn) REFERENCES server(essn)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;
		
ALTER TABLE reserve
ADD CONSTRAINT rese_rest_fk
	FOREIGN KEY (restid) REFERENCES restaurant(restid)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
ADD CONSTRAINT rese_cust_fk
	FOREIGN KEY (custid) REFERENCES customer(custid)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
ADD CONSTRAINT rese_tbln_fk
	FOREIGN KEY (tblnum) REFERENCES atable(table_number)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;

ALTER TABLE menu
ADD CONSTRAINT menu_rest_fk
	FOREIGN KEY (restid) REFERENCES restaurant(restid)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;
		
ALTER TABLE offers
ADD CONSTRAINT offe_item_fk
	FOREIGN KEY (item_id) REFERENCES item(itemid)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
ADD CONSTRAINT offe_menu_fk
	FOREIGN KEY (menu_id) REFERENCES menu(menuid)
		ON DELETE RESTRICT
		ON UPDATE CASCADE;

