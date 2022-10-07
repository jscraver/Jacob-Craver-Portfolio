/*View #1 - A view that displays the fname, lname, and ssn of all chefs.*/
CREATE VIEW rest_chefs
AS SELECT fname, lname, ssn
   FROM employee e, chef c
   WHERE e.Ssn = c.Essn;

SELECT *
FROM rest_chefs;

/*View #2 - A view that displays the item(item ID and item name) offered at a restaurant(menu ID and restaurant name).*/
CREATE VIEW menu_info(itemid, iname, menuid, rname)
AS SELECT itemid, iname, menuid, rname
   FROM item i, menu m, restaurant r, offers o
   WHERE o.item_id = i.itemid AND o.menu_id = m.menuid AND m.restID = r.RestID
   GROUP BY itemid, iname, menuid;

SELECT *
FROM menu_info;

/*View #3 - A view that displays restaurant ID, restaurant name, total number of employees, total salary paid.*/
CREATE VIEW restaurant_info(restid, rname, total_no_emp, total_sal)
AS SELECT restid, rname, COUNT(*), SUM(salary)
   FROM restaurant r, employee e
   WHERE r.restid = e.restaurantid
   GROUP BY restid, rname;
   
SELECT *
FROM restaurant_info;
