-- 1.Create a view which contains information about employee’s fullname, email and office city location.
CREATE VIEW Employee_View AS
SELECT
    CONCAT(e.firstName, ' ', e.lastName) AS FullName,
    e.email,
    o.city AS OfficeCity
FROM employees e
JOIN offices o
ON e.officeCode = o.officeCode;
SELECT * FROM Employee_View;


-- 2.Create a view that contains information about customerNumber, customerName, Full contact name, orderNumber, order status and total amount of each order.
CREATE VIEW Customer_Order_View AS
SELECT
    c.customerNumber,
    c.customerName,
    CONCAT(c.contactFirstName, ' ', c.contactLastName) AS ContactName,
    o.orderNumber,
    o.status,
    SUM(od.quantityOrdered * od.priceEach) AS TotalAmount
FROM customers c
JOIN orders o
ON c.customerNumber = o.customerNumber
JOIN orderdetails od
ON o.orderNumber = od.orderNumber
GROUP BY
    c.customerNumber,
    c.customerName,
    ContactName,
    o.orderNumber,
    o.status;
SELECT * FROM Customer_Order_View;
show tables;

-- 3. Create a view that contains information about customer name, customer city, product name and quantity of given product ordered by all customers.
CREATE VIEW Customer_Product_View AS
SELECT
    c.customerName,
    c.city,
    p.productName,
    od.quantityOrdered
FROM customers c
JOIN orders o
ON c.customerNumber = o.customerNumber
JOIN orderdetails od
ON o.orderNumber = od.orderNumber
JOIN products p
ON od.productCode = p.productCode;
SELECT * FROM Customer_Product_View;

-- 4. Create a view that contains information about customer number, customer name, total amount paid by each customer.
CREATE VIEW Customer_Payment_View AS
SELECT
    c.customerNumber,
    c.customerName,
    SUM(p.amount) AS TotalAmountPaid
FROM customers c
JOIN payments p
ON c.customerNumber = p.customerNumber
GROUP BY
    c.customerNumber,
    c.customerName;
Select * from Customer_Payment_View;


-- 4. Create a view that contains information about customer number, customer name, total amount paid by each customer.
CREATE VIEW Customer_Payment_View AS
SELECT
    c.customerNumber,
    c.customerName,
    SUM(p.amount) AS TotalAmountPaid
FROM customers c
JOIN payments p
ON c.customerNumber = p.customerNumber
GROUP BY
    c.customerNumber,
    c.customerName;
Select * from Customer_Payment_View;


-- 5. Create a view that contains information about product details for products ordered by customer residing in city 'NYC'.
CREATE VIEW NYC_Product_View AS
SELECT DISTINCT
    p.*
FROM customers c
JOIN orders o
ON c.customerNumber = o.customerNumber
JOIN orderdetails od
ON o.orderNumber = od.orderNumber
JOIN products p
ON od.productCode = p.productCode
WHERE c.city = 'NYC';
Select * from NYC_Product_View;


-- 6. Update view in question number 1 to add information about the employee's job title.
CREATE OR REPLACE VIEW Employee_View AS
SELECT
    CONCAT(e.firstName, ' ', e.lastName) AS FullName,
    e.email,
    o.city AS OfficeCity,
    e.jobTitle
FROM employees e
JOIN offices o
ON e.officeCode = o.officeCode;
select * from Employee_View;

-- 7. Update view in question number 5 to information about product details for products ordered by customer residing in city 'Las Vegas' and 'San Francisco'.
CREATE OR REPLACE VIEW NYC_Product_View AS
SELECT DISTINCT
    p.*
FROM customers c
JOIN orders o
ON c.customerNumber = o.customerNumber
JOIN orderdetails od
ON o.orderNumber = od.orderNumber
JOIN products p
ON od.productCode = p.productCode
WHERE c.city IN ('Las Vegas', 'San Francisco');
select * from NYC_Product_View;
