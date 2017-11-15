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
Project_code	VARCHAR(5)  PRIMARY KEY, -- same as customer ID
Proj_Title 		CHAR(25)    NOT NULL,
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
Project_code	VARCHAR(5)  PRIMARY KEY, -- same as customer ID
Proj_Title 		CHAR(25)    NOT NULL,
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
Project_code	VARCHAR(5)  PRIMARY KEY, -- same as customer ID
Proj_Title 		CHAR(25)    NOT NULL, 
Project_Badget	VARCHAR(25) NOT NULL,
Project_Manager VARCHAR(25) NOT NULL,
Hourly_Rate		VARCHAR(25) NOT NULL
);



Create Table Employee(
Employee_No		NUMBER(5)  PRIMARY KEY, -- same as customer ID
Employee_Name	VARCHAR(5) NOT NULL, -- same as customer ID

);

Create Table Deparment(
Departure_No	NUMBER(5)  PRIMARY KEY, -- same as customer ID
Departure_Name	VARCHAR(5) NOT NULL, -- same as customer ID
);




ALTER TABLE Project
ADD CONSTRAINT 	Employee_No FOREIGN KEY (Employee_No)
REFERENCES 		Employee(Employee_No);

ALTER TABLE Employee
ADD CONSTRAINT 	Departure_No FOREIGN KEY (Departure_No)
REFERENCES 		Deparment(Departure_No);



--------------------------------2| week 3 Mapping!------------------------------

-- mapping:

-- input:name
-- input = user_input
-- for input in every_input:
-- 	if input related with the person
-- 	group_by_input()


-- sort:

-- list_of_input []
-- for elements in group_by_input:
-- 	count the elements

-- 	if they are dublicated:
-- 		add them in a list

-- reduce:

-- counted_elements = []
-- for elements in group_by_input:
-- 	count the elements and return a list
-- 	while elements have been counted.



-- reduce: connect the name -> tweet, username -> retweet.


----------------------------------------- ---------------------------------------


-------------------------------------- 4 | Week 3---------------------------------
-- My solution is to take 10 ads in two months and make a chain of products
-- which actually, the previous ad is going to be related with the last one. 
-- and so on.


--------------------------------------   ----------------------------------------
SPLITING 	MAPPING  SHUFFLING 		REDUCING 		FINAL RESULT
---------------------------------------------------------------------------------	
R G G G -> 	R,1  => G, (1,1,1) 		-> G,3
			G,1
			G,1
			G,1

R B O P ->	R,1  => R, (1,1,1,1) 	-> R,4		->		G,3  
			B,1										 	R,4
			O,1										 	B,3 
			P,1											O,3
												->		P,3
P B O R ->	P,1	 => B (1,1,1) 		-> B,3		
			B,1
			O,1
			R,1

B P R O ->	B,1	 => O (1,1,1)		-> O,3
			P,1
			R,1
			O,1	 => P (1,1,1)		-> P,3



-------------------------------------- 1| Week 3 Task 2b  ------------------------------------


My solution on this is to create an algorithm 
to count the mutual friends and now many post theyve shared.



-------------------------------------- 2| Week 3 Task 2b  ------------------------------------









a) information about US cities as well as location of the city which includes lat and log. 
-- b) vary of things, for examplbe we can count the cities, or sum up the population.




-- { "_id" : "01036", "city" : "HAMPDEN", "loc" : [ -72.43182299999999, 42.064756 ], "pop" : 4709,
-- "state" : "MA" }



-- a) SELECT MA FROM CITIES
-- b) SELECT Fisher Island FROM CITIES


-- c. db.zipcodes.aggregate( [
-- { $group: { _id: "$state", totalPop: { $sum: "$pop" } } },
-- { $match: { totalPop: { $gte: 10*1000*1000 } } }] )
-- SELECT state, SUM(pop) AS totalPop
-- FROM Cities
-- GROUP BY state
-- HAVING totalPop >= (10*1000*1000)


-- D. db.zipcodes.aggregate({$group: {_id: "$state", avg:{$avg:"$pop"}}}


-- SELECT state, AVG (pop)
-- FROM [Cities]


-- E. group({
-- key : {state:1},
-- initial : {pop:-1,city:"none"},
-- reduce : function Reduce(doc, out) {
-- if(doc.pop < out.pop || out.pop==-1)
-- {
-- out.pop=doc.pop;
-- out.city=doc.city;
-- }
-- }})

-- SELECT COUNT (key,)

---------------------------------------------------- Week 6. ----------------------------------------

What type of queries will need to be done?
-- 1) we have to divide the pages.
-- we need a log in / registation / profile page. (user pages.)

-- 1.1) which is the product storage. price,quantity. suggestions on what other people usually bought.
-- when they purchased the same item which is loaded.


-- 2) we need pages to show the productes weither seperated by categories or brands. (or maybe both.)

-- 3) we need to decide on if we want to use baskets. lattest research have show that 90% of the baskets
-- they end up for ever filled and people won't carry on their 'shopping'

-- 4)   



-- since we need the results quick. The best option should be MongoDB



-- What type of queries will need to be done?

-- - How fast do you need the results back? 
-- pretty fast, cause nowdays if the algorithms are slow the costumer is not going to come back.


-- - How will you link the customer to the products bought?
-- eatch costomer will have a list which indicates to the products bought.


-- - Which fields should you use for comparison for recommendations?
-- probably eatch items would have a certain category.
-- further more you can store details for eatch items like inches or resolution for screens or laptops etc.

-- - What objects would be required? What documents?
-- in eatch item would have their own details.
-- the documents would be seperated by category.

-- - Are the documents atomic or are there embedded documents?

-- since we need to 

-- - Is this all a separate collection or do you want your whole database available for real time querying?

-- The durability is when a nodes dies what steps do I have to make to save my data. 
-- Well, one of the options is to split the data to multiple nodes (servers)


-- Availability is how quick the data will be launched and be available to the user.
-- One solution for this is to store data every time the transaction is completed

--  Reduced Latency is how the quick the data will be travel to be launched. So the best thing is to split the data into many nodes and keep it close to the main node.

-- Scalability can be achieved by simply adding more nodes so we can jump to the previous node and forth again.





