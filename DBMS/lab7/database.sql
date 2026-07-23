-- Active: 1780924718547@@127.0.0.1@3306

create database lab7;
use lab7;

create table Faculty(
  FacultyID int primary key,
  Name varchar(50) not null,
  Designation varchar(50),
  Department varchar(50) not null,
  OfficePhone varchar(50) not null,
  Email varchar(50) not null unique
);

create table Student(
  StudentID int primary key not null unique,
  Name varchar(50) not null,
  Program varchar(100) not null,
  Year int not null,
  Email varchar(50) not null unique
);

create table ResearchArea(
  AreaID int primary key unique,
  AreaName varchar(50) not null,
  Description varchar(50)
);

create table ResearchProject(
  ProjectID int primary key,
  Title varchar(50) not null,
  StartDate DATE not null,
  EndDate DATE,
  Budget Decimal(12,2),
  Status Varchar(20) not null,
  FacultyID int not null, -- foreignK from the Faculty --
  AreaID int not null , -- foreignK from the ReasearchArea--

  Foreign Key (FacultyID) REFERENCES Faculty(FacultyID),
  Foreign Key (AreaID) REFERENCES ResearchArea(AreaID)
);

create Table FundingAgency(
  AgencyID int primary key,
  AgencyName varchar(50) not null,
  Country varchar(50),
  ContactPerson varchar (20),
  Email varchar (20) not null unique
);

CREATE TABLE LABORATORY (
    LabID         INT PRIMARY KEY,
    Name          VARCHAR(100) NOT NULL,
    Building      VARCHAR(100),
    Capacity      INT
);

CREATE TABLE PUBLICATION (
    PublicationID     INT PRIMARY KEY,
    Title             VARCHAR(200) NOT NULL,
    Journal           VARCHAR(150),
    PublicationYear   year,
    DOI               VARCHAR(50) UNIQUE
)

create table Participation(
  ProjectID int not null,
  StudentID int not null,  -- student can work on M projects --

  JoiningDate DATE not null,
  Role varchar(50) not null,
  MonthlyStipend decimal(10,2),
  Foreign Key (ProjectID) REFERENCES ResearchProject(ProjectID),
  Foreign Key (StudentID) REFERENCES Student(StudentID)
)

create table Funding(
  AgencyID int not null ,
  ProjectID int not null , -- 1project can get funded from multiple agencies --
  Amount decimal(12,2) not null,
  FundingDate DATE not null,
  FOREIGN KEY (ProjectID) REFERENCES ResearchProject(ProjectID),
    FOREIGN KEY (AgencyID) REFERENCES FundingAgency(AgencyID)
)



