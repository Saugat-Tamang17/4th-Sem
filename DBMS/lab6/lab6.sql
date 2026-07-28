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


