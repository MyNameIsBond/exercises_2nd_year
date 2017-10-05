

-----------------------  Wards Table -------------------------- |
Create Table Wards(
ward_id 		NUMBER(5) PRIMARY KEY,
Ward_name 		VARCHAR(15) NOT NULL,
Ward_Manager_id NUMBER(4) NOT NULL
);
INSERT INTO Wards (ward_id, Ward_name, Ward_Manager_id)
VALUES ( RH1,	Robin Hood Ward,		A01);
VALUES ( DHL1,	DH Lawrence Ward,		B19);
VALUES ( LB1,	Lord Byron Ward,		A05);
VALUES ( RLH1,	Richard Lionheart Ward,	B99);

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

INSERT INTO stuff (First_name, surname, salary,Bonus_pct)
VALUES (Cornelius,Murray, 	60000, 	RH1);
VALUES (Suky 	 ,Smith, 	19000, 	DHL1);
VALUES (Elvis 	 ,Malone,  	25000, 	LB1);
VALUES (Peter 	 ,Oville,  	30000, 	LB1);
VALUES (John 	 ,Garfield, 25000, 	LB1);
VALUES (Mike 	 ,Best,  	26500, 	LB1);
VALUES (Shila 	 ,Jones,  	50000, 	LB1);
VALUES (Paul 	 ,Hamzepur, 20000, 	LB1);



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

