create database lab7third;
use lab7third;

create table artist( 
artistID int primary key, 
artistName varchar(40) not null 
); 
Describe artist; 

create table customer( 
customerID int primary key, 
customerName varchar(40) not null, 
address varchar(60) not null, 
phone varchar(15) not null 
); describe customers; 

create table sale( 
saleID int primary key, 
customerID int not null, 
paintingID int not null, 
purchaseDate date not null, 
salesPrice decimal(12, 2) not null, 
foreign key (customerID) references customer(customerID), 
foreign key (paintingID) references painting(paintingID) 
); describe sale ;
