-- Active: 1780405368569@@127.0.0.1@3306@sxc2
create DATABASE sxc2;
use sxc2;
CREATE TABLE Department (
    DeptNo INT PRIMARY KEY,
    DeptName VARCHAR(50) NOT NULL,
    DeptEmail VARCHAR(50) not null,
    DeptHOD varchar(50)
);
CREATE TABLE Employee (
    EmpNo INT PRIMARY KEY,
    EmpName VARCHAR(100) NOT NULL,
    Job VARCHAR(50),
    DeptNo INT,
    Phone_no VARCHAR(20),
    YearOfEnrollment INT,
    EmailAddress VARCHAR(100) UNIQUE, 
    PostalAddress VARCHAR(255),
    
   
    CONSTRAINT FK_Employee_Department FOREIGN KEY (DeptNo) 
        REFERENCES Department(DeptNo)
);
describe Department;
describe employee;

 INSERT INTO Department (DeptNo, DeptName, DeptEmail, DeptHOD) VALUES 
(2, 'Computer Science', 'cs@sxc.edu.np', 'Mr. Ganesh Yogi'),
(3, 'MicroBiology', 'microbio@sxc.edu.np', 'Mrs. Pramila Parajuli'),
(4, 'Physics', 'physics@sxc.edu.np', 'Mr. Binod Bhandari'),
(5, 'Business Studies', 'bs@sxc.edu.np', 'Mr. Maha Prasad Shrestha');

select *from department

insert into employee(EmpNo,EmpName,Job,DeptNo,Phone_no,YearofEnrollment,EmailAddress,PostalAddress) VALUES 
(1, 'Abhiyan Sainju', 'Teaching Assistant', 2, '5544332', 2016, 'abhiyansainju@gmail.com', '4066'),
(2, 'Babis Shrestha', 'Software Developer', 2, '7744533', 2018, 'babis@gmail.com', '3056'),
(3, 'Chetana Panta', 'Coordinator', 4, '3322551', 2015, 'chetana@gmail.com', '4066'),
(4, 'Diwas Sapkota', 'Researcher', 4, '776644', 2014, 'diwas@gmail.com', '9088'),
(5, 'Elina Malla', 'DBA', 3, '4433532', 2019, 'elina@gmail.com', '3056'),
(6, 'Indu Adhikari', 'Counsellor', 5, '352625', 2020, 'indu@gmail.com', '5504');

select *from employee

INSERT INTO Employee (
    EmpNo, EmpName, Job, DeptNo, Phone_no, YearOfEnrollment, EmailAddress, PostalAddress
) VALUES 
(7, 'Samir Thapa', 'Lecturer', 1, '984123456', 2021, 'samir@sxc.edu.np', '44600');

SELECT * FROM Employee WHERE DeptNo = 3;

SELECT * FROM Employee WHERE YearOfEnrollment >= 2016;

UPDATE Employee SET Phone_no = '3344225' WHERE EmpNo = 3;
SELECT * FROM Employee WHERE EmpNo=3;

delete from employee where DeptNo=3;
select *from employee ;

DELETE FROM Department WHERE DeptNo = 4;