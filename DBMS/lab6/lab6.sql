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


