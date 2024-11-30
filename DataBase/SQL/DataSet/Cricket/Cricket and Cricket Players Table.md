
Cricket Table


```sql
CREATE TABLE Cricket (
    Year INT,
    Player_Name VARCHAR(50),
    Runs INT,
    Balls INT
);


INSERT INTO Cricket (Year, Player_Name, Runs, Balls) VALUES
(2022, 'Hardik Pandya', 425, 345),
(2023, 'Virat Kohli', 480, 455),
(2023, 'KL Rahul', 450, 370),
(2022, 'Virat Kohli', 356, 346),
(2021, 'Shubman Gill', 620, 615),
(2023, 'Hardik Pandya', 350, 280),
(2022, 'KL Rahul', 325, 280),
(2023, 'Shubman Gill', 450, 400),
(2023, 'Rohit Sharma', 500, 348),
(2023, 'Rohit Sharma', 450, 440);


-- SELECT * 
-- FROM Cricket

-- Output:
-- +------+---------------+------+-------+
-- | Year | Player_Name   | Runs | Balls |
-- +------+---------------+------+-------+
-- | 2022 | Hardik Pandya |  425 |   345 |
-- | 2023 | Virat Kohli   |  480 |   455 |
-- | 2023 | KL Rahul      |  450 |   370 |
-- | 2022 | Virat Kohli   |  356 |   346 |
-- | 2021 | Shubman Gill  |  620 |   615 |
-- | 2023 | Hardik Pandya |  350 |   280 |
-- | 2022 | KL Rahul      |  325 |   280 |
-- | 2023 | Shubman Gill  |  450 |   400 |
-- | 2023 | Rohit Sharma  |  500 |   348 |
-- | 2023 | Rohit Sharma  |  450 |   440 |
-- +------+---------------+------+-------+
```




Cricket Players Table

```sql

CREATE TABLE Cricket_Players (
    Player_ID INT AUTO_INCREMENT PRIMARY KEY,
    Player_Name VARCHAR(50) UNIQUE
);

INSERT INTO Cricket_Players (Player_Name) VALUES
('Virat Kohli'),
('Shubman Gill'),
('Rohit Sharma');


SELECT *
FROM Cricket_Players

-- Output:

-- +-----------+--------------+
-- | Player_ID | Player_Name  |
-- +-----------+--------------+
-- |         3 | Rohit Sharma |
-- |         2 | Shubman Gill |
-- |         1 | Virat Kohli  |
-- +-----------+--------------+


```
