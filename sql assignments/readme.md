1.we first created a database with name test_db:
CREATE DATABASE test_db;

2.we first created a table with name salespeople:

CREATE TABLE SalesPeople (
    Snum INT PRIMARY KEY,
    Sname VARCHAR(255) UNIQUE,
    City VARCHAR(255),
    Comm DECIMAL(4, 2)
);


3.Insert values in table salespeople:
INSERT INTO SalesPeople (Snum, Sname, City, Comm) VALUES
(1001, 'Peel', 'London', 0.12),
(1002, 'Serres', 'Sanjose', 0.13),
(1004, 'Motika', 'London', 0.11),
(1007, 'Rifkin', 'Barcelona', 0.15),
(1003, 'Axelrod', 'Newyork', 0.10);

4.create table customers:
CREATE TABLE Customers (
    Cnum INT PRIMARY KEY,
    Cname VARCHAR(255),
    City VARCHAR(255) NOT NULL,
    Snum INT,
    FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum)
);

5.Insert values in table customers;
INSERT INTO Customers (Cnum, Cname, City, Snum) VALUES
(2001, 'Hoffman', 'London', 1001),
(2002, 'Giovanni', 'Rome', 1003),
(2003, 'Liu', 'Sanjose', 1002),
(2004, 'Grass', 'Berlin', 1002),
(2006, 'Clemens', 'London', 1001),
(2008, 'Cisneros', 'Sanjose', 1007),
(2007, 'Pereira', 'Rome', 1004);

6.Create table orders:

CREATE TABLE Orders (
    Onum INT PRIMARY KEY,
    Amt DECIMAL(10, 2),
    Odate DATE,
    Cnum INT,
    Snum INT,
    FOREIGN KEY (Cnum) REFERENCES Customers(Cnum),
    FOREIGN KEY (Snum) REFERENCES SalesPeople(Snum)
);



7.Insert values in table orders:
INSERT INTO Orders (Onum, Amt, Odate, Cnum, Snum) VALUES
(3001, 18.69, '1990-03-10', 2008, 1007),
(3003, 767.19, '1990-03-10', 2001, 1001),
(3002, 1900.10, '1990-03-10', 2007, 1004),
(3005, 5160.45, '1990-03-10', 2003, 1002),
(3006, 1098.16, '1990-03-10', 2008, 1007),
(3009, 1713.23, '1990-04-10', 2002, 1003),
(3007, 75.75, '1990-04-10', 2004, 1002),
(3008, 4273.00, '1990-05-10', 2006, 1001),
(3010, 1309.95, '1990-06-10', 2004, 1002),
(3011, 9891.88, '1990-06-10', 2006, 1001);

8.Count the number of Salesperson whose name begin with ‘a’/’A’.

SELECT COUNT(*) 
FROM SalesPeople
WHERE Sname LIKE 'A%';

9.Display all the Salesperson whose all orders worth is more than Rs. 2000.

SELECT SP.Sname, SUM(O.Amt) AS TotalOrderWorth
FROM SalesPeople SP
INNER JOIN Orders O ON SP.Snum = O.Snum
GROUP BY SP.Snum
HAVING SUM(O.Amt) > 2000;

10.Count the number of Salesperson belonging to Newyork.


SELECT COUNT(*) 
FROM SalesPeople
WHERE City = 'Newyork';

11.Display the number of Salespeople belonging to London and belonging to Paris.

SELECT City, COUNT(*) AS NumSalespeople
FROM SalesPeople
WHERE City IN ('London', 'Paris')
GROUP BY City;

12.Display the number of orders taken by each Salesperson and their date of orders.

SELECT SP.Sname, O.Odate, COUNT(*) AS NumOrders
FROM SalesPeople SP
INNER JOIN Orders O ON SP.Snum = O.Snum
GROUP BY SP.Snum, O.Odate;





