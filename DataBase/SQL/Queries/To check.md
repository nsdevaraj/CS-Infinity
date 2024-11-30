


to jot {

https://youtu.be/UlXtfq-kuF4?si=lJoXBg2nCfqNcMlR

https://youtu.be/HQUUBOS4S9Q?si=NIFwG0A5P0ZnhQ6z


}



https://tacnique.com/interviews/9d7c9f67-a372-41cf-8cf0-530a91295472/questions/9d7a45e5-2882-457b-9aec-1937928dde41



https://onecompiler.com/mysql/42yjn9tux


```sql


CREATE TABLE IF NOT EXISTS maintable_885DX (
    ID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    ReportsTo VARCHAR(50),
    Position VARCHAR(50),
    Age INT
);

-- Step 2: Insert data into the table
INSERT INTO maintable_885DX (ID, FirstName, LastName, ReportsTo, Position, Age) VALUES
(1, 'Daniel', 'Smith', 'Bob Boss', 'Engineer', 25),
(2, 'Mike', 'White', 'Bob Boss', 'Contractor', 22),
(3, 'Jenny', 'Richards', NULL, 'CEO', 45),
(4, 'Robert', 'Black', 'Daniel Smith', 'Sales', 22),
(5, 'Noah', 'Fritz', 'Jenny Richards', 'Assistant', 30),
(6, 'David', 'S', 'Jenny Richards', 'Director', 32),
(7, 'Ashley', 'Wells', 'David S', 'Assistant', 25),
(8, 'Ashley', 'Johnson', NULL, 'Intern', 25);


-- Bob Boss         2 (25+22)/2
-- Daniel Smith     1 22
-- Jenny Richards   2 (30+32)/2
-- soon

-- reportTo, no of people who report, average age (neareast interger), sorted alphabetically

Select * from maintable_885DX;



select ReportsTo, count(*) as no_of_reportees, ROUND(SUM(Age)/count(*))
from maintable_885DX
where ReportsTo is not NULL
group by ReportsTo
order by ReportsTo

```


https://tacnique.com/interviews/9d7c9f67-a372-41cf-8cf0-530a91295472/questions/9c5c7e31-06db-41f7-99bf-a89d1bec76b7


https://onecompiler.com/mysql/42yjmc2kp


```sql

-- Create Client Table
CREATE TABLE Client (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    client_email VARCHAR(255) NOT NULL
);
-- Create ID Table
CREATE TABLE ID (
    person_id INT PRIMARY KEY,
    client_id INT,
    FOREIGN KEY (client_id) REFERENCES Client(client_id)
);

-- Create Deals Table
CREATE TABLE Deals (
    deal_id INT PRIMARY KEY,
    client_id INT,
    deal_status VARCHAR(50) NOT NULL,
    deal_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Client(client_id)
);
-- Insert data into Client Table
INSERT INTO Client (client_id, client_name, client_email)
VALUES
    (1, 'Alice Johnson', 'alice.johnson@example.com'),
    (2, 'Bob Smith', 'bob.smith@example.com'),
    (3, 'Charlie Brown', 'charlie.brown@example.com');

-- Insert data into ID Table
INSERT INTO ID (person_id, client_id)
VALUES
    (1001, 1),
    (1002, 2),
    (1003, 3);

-- Insert data into Deals Table
INSERT INTO Deals (deal_id, client_id, deal_status, deal_amount)
VALUES
    (2001, 1, 'closed', 10000.00),
    (2002, 1, 'open', 15000.00),
    (2003, 2, 'closed', 20000.00),
    (2004, 3, 'open', 25000.00),
    (2005, 3, 'closed', 30000.00);
    
select * from ID;
select * from Client;
select * from Deals;

-- no of closed Deals
-- person id



select i.person_id, COUNT(*) as closed_deals
from ID  i
join Deals d 
  on i.client_id = d.client_id
where d.deal_status = 'closed'
group by d.client_id, i.person_id




```



https://tacnique.com/interviews/9d7c9f67-a372-41cf-8cf0-530a91295472/questions/9d4e8fb0-0b5f-4fc7-a861-1ca6ea6cba6e


https://onecompiler.com/mysql/42yjmtmgt


```sql


CREATE TABLE Client (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(255) NOT NULL,
    client_email VARCHAR(255) 
);

CREATE TABLE ID (
    person_id INT PRIMARY KEY,
    client_id INT NULL, 
    FOREIGN KEY (client_id) REFERENCES Client(client_id)
);


CREATE TABLE Deals (
    deal_id INT PRIMARY KEY,
    client_id INT NULL,
    deal_status VARCHAR(50) NULL, 
    deal_amount DECIMAL(10, 2) NULL,
    FOREIGN KEY (client_id) REFERENCES Client(client_id)
);


INSERT INTO Client (client_id, client_name, client_email)
VALUES
    (1, 'Alice Johnson', 'alice.johnson@example.com'),
    (2, 'Bob Smith', NULL), 
    (3, 'Charlie Brown', 'charlie.brown@example.com');


INSERT INTO ID (person_id, client_id)
VALUES
    (1001, 1),
    (1002, NULL),  
    (1003, 3);


INSERT INTO Deals (deal_id, client_id, deal_status, deal_amount)
VALUES
    (2001, 1, 'closed', 10000.00),
    (2002, 1, NULL, 15000.00),
    (2003, 2, 'closed', NULL),
    (2004, 3, 'open', NULL),
    (2005, 3, 'closed', 30000.00);

-- Queries to check data in each table
SELECT * FROM ID;
SELECT * FROM Client;
SELECT * FROM Deals;

-- each client, client_id, clientname, client email, total deal amount if avail if not default 0,
-- only client with normal email included.. 

select c.client_id, c.client_name, client_email, SUM(d.deal_amount)
from Client c
join Deals d
  on c.client_id = d.client_id
where c.client_email IS NOT NULL AND d.deal_amount IS NOT NULL
group by c.client_id, c.client_name, client_email



```



to jot {

[06:38, 13/11/2024] JS_JeevaSaravanan: https://youtu.be/UlXtfq-kuF4?si=lJoXBg2nCfqNcMlR
[07:00, 13/11/2024] JS_JeevaSaravanan: https://youtu.be/HQUUBOS4S9Q?si=NIFwG0A5P0ZnhQ6z


}