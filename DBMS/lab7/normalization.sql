create database Lab7second;
use  lab7second;

CREATE TABLE STUDENT2 (
    StudentID VARCHAR(10) PRIMARY KEY,
    StudentName VARCHAR(100) NOT NULL,
    Program VARCHAR(50) NOT NULL
);
describe student2;


CREATE TABLE INSTRUCTOR (
    InstructorID VARCHAR(10) PRIMARY KEY,
    InstructorName VARCHAR(100) NOT NULL,
    InstructorOffice VARCHAR(20) NOT NULL
);
describe instructor;


CREATE TABLE TEXTBOOK (
    TextbookISBN VARCHAR(20) PRIMARY KEY,
    TextbookTitle VARCHAR(200) NOT NULL,
    Publisher VARCHAR(100) NOT NULL
);
describe textbook;

CREATE TABLE COURSE (
    CourseID VARCHAR(10) PRIMARY KEY,
    CourseName VARCHAR(100) NOT NULL,
    TextbookISBN VARCHAR(20),
    FOREIGN KEY (TextbookISBN) REFERENCES TEXTBOOK(TextbookISBN)
);
describe course;


CREATE TABLE ENROLLMENT (
    StudentID VARCHAR(10),
    CourseID VARCHAR(10),
    Semester VARCHAR(20),
    InstructorID VARCHAR(10) NOT NULL,
    Grade VARCHAR(5),
    PRIMARY KEY (StudentID, CourseID, Semester),
    FOREIGN KEY (StudentID) REFERENCES STUDENT(StudentID),
    FOREIGN KEY (CourseID) REFERENCES COURSE(CourseID),
    FOREIGN KEY (InstructorID) REFERENCES INSTRUCTOR(InstructorID)
);
describe enrollment;



