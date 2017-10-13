-----------------------  Wards Table -------------------------- |
Create Table Wards(
ward_id 		NUMBER(5) PRIMARY KEY,
Ward_name 		VARCHAR(15) NOT NULL,
Ward_Manager_id NUMBER(4) NOT NULL
);

INSERT INTO Wards(ward_id, Ward_name, Ward_Manager_id)
VALUES ( RH1,Robin_Hood_Ward,B19);
VALUES ( DHL1,DH _Lawrence_Ward,B19);
VALUES ( LB1,Lord_Byron_Ward,A05);
VALUES ( RLH1,Richard_Lionheart_Ward,B99);


-----------------------  Stuff Table -------------------------- |

Create Table Stuff(
stuff_id 	NUMBER(5) 	PRIMARY KEY,
First_name 	VARCHAR(15) NOT NULL,
surname 	VARCHAR(4) 	NOT NULL,
Ward_id 	NUMBER(4) 	NOT NULL,
salary 		NUMBER(4) 	NOT NULL,
Bonus_pct 	NUMBER(4) 	NOT NULL
);

ALTER TABLE Stuff
ADD CONSTRAINT 	ward_id_fk FOREIGN KEY (Ward_id)
REFERENCES 		Wards(ward_id);

INSERT INTO Stuff (First_name, surname, salary,Bonus_pct)
VALUES(Cornelius,Murray, 	60000, 	RH1);
VALUES(Suky 	 ,Smith, 	19000, 	DHL1);
VALUES(Elvis 	 ,Malone,  	25000, 	LB1);
VALUES(Peter 	 ,Oville,  	30000, 	LB1);
VALUES(John 	 ,Garfield, 25000, 	LB1);
VALUES(Mike 	 ,Best,  	26500, 	LB1);
VALUES(Shila 	 ,Jones,  	50000, 	LB1);
VALUES(Paul 	 ,Hamzepur, 20000, 	LB1);



-----------------------  StaffGrades Table --------------------- |


Create Table StaffGrades (
Grade_Level 	NUMBER(2)	 NOT NULL,
Min_sal 		VARCHAR(7,2) NOT NULL,
Max_sal 		VARCHAR(9,2) NOT NULL
);

INSERT INTO stuff (Grade_Level, Min_sal, Max_sal)
VALUES (1,10000.00, 60000, 	29000.00);
VALUES (2,30000.00, 60000, 	39000.00);
VALUES (3,40000.00, 60000, 	49000.00);
VALUES (4,50000.00, 60000, 	59000.00);
VALUES (5,60000.00, 60000, 	99000.00);

------------------------------- lab Tasks 2 -------------------------------

-- Produce a list of staff showing for each member of staff his/her id, surname and Monthly Salary.
-- The list should be headed Staff ID, Surname and Monthly Salary.

SELECT stuff_id,surname,salary FROM stuff;
ORDER BY stuff_id,surname,salary;


-- Produce a list of the wards. The list should be headed: Ward NAME Ward Code
-- Ward Manager

SELECT Ward_name,Ward_Manager_id,ward_id FROM Wards;
ORDER BY Ward_name,Ward_Manager_id,ward_id;

-- Ward_name,Ward_Manager_id,ward_id

SELECT MAX(salary) and MIN(salary) FROM	Stuff


-- Produce a list of staff showing for each staff in the hospital his/her first name, 
-- his her surname (all in capital letters) and his/her id. 
-- The list should be headed as follows: “First Name” “Surname” “Staff ID”. 
-- The list should be sorted by surname

SELECT First_name,surname FROM stuff
ORDER BY First_name,surname;
Where hospital = TRUE;

-- Produce a list of staff that earn annual salaries more than 23000. 
-- The list should show for each member of staff, 
-- the “Staff ID” and the “Annual Salary”. 
-- The list should be sorted in descending order of salary

SELECT Salary,stuff_id FROM stuff
Where salary < 23000;

-- Produce a list of staff that earn between 20000 and 70000 and work on the :DH Lawrence ward.




SELECT * FROM stuff
where salary BETWEEN 20000 and 70000;



-- It has now been decided that the date employed by each staff should be included in the staff table. 
-- Modify the staff table to include this attribute. 
-- Its data type is date.

ALTER TABLE stuff
ADD Date_employed date();


-- Produce a list of all the staff in ward LB1. 
-- The list should include for each staff, his/her staff id, surname, first name and the annual salary. 
-- The list should be sorted in ascending order of salary and then surname. 

-- YYYY-MM-DD

INSERT INTO Stuff (Date_employed)
VALUES(2001-8-26);
VALUES(1997-9-1);
VALUES(1998-1-1);
VALUES(2004-6-6);
VALUES(2009-4-17);
VALUES(2011-8-17);
VALUES(2008-7-17);
VALUES(2010-10-10);



-- ------------------------------------------- WEEK 2 norm 1. -------------------------------------------




Create Table Item(
item_id 			NUMBER(5) PRIMARY KEY,
item_name 			VARCHAR(15) NOT NULL,
item_Price 			FLOAT(4) NOT NULL,
);

INSERT INTO Item(item_id, item_name, item_Price,qty)
VALUES 		(1,Bakewell Tart,0.15,		20);
VALUES 		(2,Danish Pastry,0.20,		13);
VALUES 		(3,Apple Pie,	 0.15,	  	45);


Create Table Customer(
acc_number 			NUMBER(5) PRIMARY KEY, -- same as customer ID
Address 			VARCHAR(25) NOT NULL,
Customer 			VARCHAR(25) NOT NULL
);

INSERT INTO Customer(acc_number, Address, Customer)
VALUES 		(1,	27 Bay Drive Cove,Robin_Hood_Ward,	Daisy s Café );
VALUES 		(2,	12 Dee View	Aberdeen,Smiths	);
VALUES 		(3,3 High Street Banchory, Sally s Snacks);
VALUES 		(3,3 High Street Banchory, Sally s Snacks);



Create Table Order(
order_No 		NUMBER(5) 	PRIMARY KEY,
date_ord 		Date(15) 	NOT NULL,
item_Price 		FLOAT(4) 	NOT NULL
);

INSERT INTO Order (order_No,date_ord,item_Price)
VALUES (1,7823, 16-7)
VALUES (1,7823, 16-7)










-- ------------------------------------------- WEEK 2 norm 2. -------------------------------------------
-------------------------------------------------->1Nf<--------------------------------------------------
Create Table Project(
Project_code	VARCHAR(5) PRIMARY KEY, -- same as customer ID
Proj_Title 		CHAR(25) NOT NULL,
Project_Badget	VARCHAR(25) NOT NULL,
Project_Manager VARCHAR(25) NOT NULL,
Hourly_Rate		VARCHAR(25) NOT NULL
);

Create Table Employee(
Employee_No		NUMBER(5) PRIMARY KEY, -- same as customer ID
Employee_Name	NUMBER(5) PRIMARY KEY, -- same as customer ID
Departure_No	NUMBER(5) PRIMARY KEY, -- same as customer ID
Departure_Name	NUMBER(5) PRIMARY KEY, -- same as customer ID
);
-------------------------------------------------->2Nf<--------------------------------------------------
Create Table Project(
Project_code	VARCHAR(5) PRIMARY KEY, -- same as customer ID
Proj_Title 		CHAR(25) NOT NULL,
Project_Badget	VARCHAR(25) NOT NULL,
Project_Manager VARCHAR(25) NOT NULL,
Hourly_Rate		VARCHAR(25) NOT NULL
);

Create Table Employee(
Employee_No		NUMBER(5) PRIMARY KEY, -- same as customer ID
Employee_Name	NUMBER(5) PRIMARY KEY, -- same as customer ID

);

Create Table Deparment(
Departure_No	NUMBER(5) PRIMARY KEY, -- same as customer ID
Departure_Name	NUMBER(5) PRIMARY KEY, -- same as customer ID
);

-------------------------------------------------->3Nf<--------------------------------------------------

-- 
--
--
--
--
--
Create Table Project(
Project_code	VARCHAR(5) PRIMARY KEY, -- same as customer ID
Proj_Title 		CHAR(25) NOT NULL, 
Project_Badget	VARCHAR(25) NOT NULL,
Project_Manager VARCHAR(25) NOT NULL,
Hourly_Rate		VARCHAR(25) NOT NULL
);



Create Table Employee(
Employee_No		NUMBER(5) PRIMARY KEY, -- same as customer ID
Employee_Name	NUMBER(5) PRIMARY KEY, -- same as customer ID

);



Create Table Deparment(
Departure_No	NUMBER(5) PRIMARY KEY, -- same as customer ID
Departure_Name	NUMBER(5) PRIMARY KEY, -- same as customer ID
);




ALTER TABLE Project
ADD CONSTRAINT 	Employee_No FOREIGN KEY (Employee_No)
REFERENCES 		Employee(Employee_No);

ALTER TABLE Employee
ADD CONSTRAINT 	Departure_No FOREIGN KEY (Departure_No)
REFERENCES 		Deparment(Departure_No);
