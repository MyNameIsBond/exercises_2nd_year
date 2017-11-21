---------------------- Normalisation No1 ----------------------
Create Table Client(
Cust_ID			VARCHAR(5)  PRIMARY KEY,
Cust_Name		VARCHAR(25) NOT NULL,
Cust_address	VARCHAR(25) NOT NULL,
date_ord 		Date(15) 	NOT NULL,	
Total_price		VARCHAR(5) 	NOT NULL,
Order_ID		NUMBER(5)  	NOT NULL,

);



Create Table Order(
QTy				VARCHAR(5) 	NOT NULL, 
Unit_Price		NUMBER(5)  	NOT NULL, 
Equipment		VARCHAR(5) 	NOT NULL,
);



ALTER TABLE Project
ADD CONSTRAINT 	Employee_No FOREIGN KEY (Employee_No)
REFERENCES 		Employee(Employee_No);

ALTER TABLE Employee
ADD CONSTRAINT 	Departure_No FOREIGN KEY (Departure_No)
REFERENCES 		Deparment(Departure_No);



---------------------- Normalisation No2 ----------------------


Create Table Client(
Cust_ID			VARCHAR(5)  PRIMARY KEY,
Cust_Name		VARCHAR(25) NOT NULL,
Cust_address	VARCHAR(25) NOT NULL,
);



Create Table Items(
QTy				VARCHAR(5) 	NOT NULL, 
Unit_Price		NUMBER(5)  	NOT NULL, 
Equipment		VARCHAR(5) 	NOT NULL,
);

Create Table Order(
Order_ID		NUMBER(5)  	PRIMARY KEY,
date_ord		Date(15) 	NOT NULL,	
Total_price		VARCHAR(5) 	NOT NULL,
);

---------------------- Normalisation No2 2nd Idea----------------------Create Table Client(

Create Table Customer(
Cust_ID			VARCHAR(5)  PRIMARY KEY,
Cust_Name		VARCHAR(25) NOT NULL,
Cust_address	VARCHAR(25) NOT NULL,
);


Create Table Order(
Order_ID		NUMBER(5)  	NOT NULL,
QTy				VARCHAR(5) 	NOT NULL, 
date_ord 		Date(15) 	NOT NULL,	
Unit_Price		NUMBER(5)  	NOT NULL, 
Equipment		VARCHAR(5) 	NOT NULL,
Total_price		VARCHAR(5) 	NOT NULL,
);



---------------------- Normalisation No3 ----------------------
Create Table Customer(
Cust_ID			VARCHAR(5)  PRIMARY KEY,
Cust_Name		VARCHAR(25) NOT NULL,
Cust_address	VARCHAR(25) NOT NULL,
);


Create Table Order(
Order_ID		NUMBER(5)  	PRIMARY KEY,
QTy				VARCHAR(5) 	NOT NULL, 
date_ord 		Date(15) 	NOT NULL,	
Unit_Price		NUMBER(5)  	NOT NULL, 
Equipment		VARCHAR(5) 	NOT NULL,
Total_price		VARCHAR(5) 	NOT NULL,
);





