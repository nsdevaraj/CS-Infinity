

### **Interview-Level SQL Questions**

1. **Find the highest GPA student in each major. Display their name, major, and GPA.**


```sql
SELECT s1.name, s1.major, s1.gpa
FROM Students s1
WHERE s1.gpa = (
	SELECT MAX(s2.gpa)
  	FROM Students s2
  	WHERE s1.major = s2.major 
)
```


To be continued:


2. **List the students who are enrolled in all the courses offered by their major’s department.**

note: not sure about its correctness
```sql

SELECT s.name
FROM Students s
JOIN Courses c On s.major = c.department
JOIN Enrollments e on e.StudentID = s.id AND e.CourseID = c.id
GROUP BY s.id, s.name, s.major
HAVING COUNT(DISTINCT c.id) = (
  SELECT COUNT(*)
  FROM Courses c2
  WHERE c2.department = s.major
  )

```



1. **Identify the courses in which more than one student achieved an 'A' grade in the same semester.**

```sql

SELECT C.CourseName, E.Semester
FROM Enrollments E
JOIN Courses C 
	ON E.CourseID = C.CourseID
WHERE E.Grade = 'A'
GROUP BY C.CourseName, E.Semester
HAVING COUNT(DISTINCT E.StudentID) > 1;

```


4. **Find the students who have never taken any course outside their major’s department.**


   ```sql
   SELECT S.Name
   FROM Students S
   WHERE NOT EXISTS (
       SELECT 1
       FROM Enrollments E
       JOIN Courses C ON E.CourseID = C.CourseID
       WHERE E.StudentID = S.StudentID AND C.Department != S.Major
   );
   ```


5. **Find the average GPA of students who have taken at least one course in the "Mathematics" department.**

   ```sql
   SELECT AVG(S.GPA)
   FROM Students S
   WHERE S.StudentID IN (
       SELECT DISTINCT E.StudentID
       FROM Enrollments E
       JOIN Courses C ON E.CourseID = C.CourseID
       WHERE C.Department = 'Mathematics'
   );
   ```



 to be continued...
 
1. **For each course, find the percentage of students who scored above 'B' in a specific semester.**

   ```sql
   SELECT C.CourseName, E.Semester,
          (COUNT(CASE WHEN E.Grade IN ('A', 'A-', 'B+') THEN 1 END) * 100.0 / COUNT(*)) AS PercentageAboveB
   FROM Enrollments E
   JOIN Courses C ON E.CourseID = C.CourseID
   GROUP BY C.CourseName, E.Semester;
   ```

7. **Identify the students who have taken the highest number of credits in a single semester.**
   ```sql
   SELECT S.Name, E.Semester, SUM(C.Credits) AS TotalCredits
   FROM Students S
   JOIN Enrollments E ON S.StudentID = E.StudentID
   JOIN Courses C ON E.CourseID = C.CourseID
   GROUP BY S.Name, E.Semester
   HAVING SUM(C.Credits) = (
       SELECT MAX(TotalCredits)
       FROM (
           SELECT SUM(C1.Credits) AS TotalCredits
           FROM Enrollments E1
           JOIN Courses C1 ON E1.CourseID = C1.CourseID
           GROUP BY E1.StudentID, E1.Semester
       ) AS SubQuery
   );
   ```

8. **Retrieve the name and GPA of students whose GPA rank is in the top 50% in their major.**
   ```sql
   WITH RankedStudents AS (
       SELECT Major, StudentID, Name, GPA,
              RANK() OVER (PARTITION BY Major ORDER BY GPA DESC) AS RankInMajor,
              COUNT(*) OVER (PARTITION BY Major) AS TotalStudents
       FROM Students
   )
   SELECT Name, GPA
   FROM RankedStudents
   WHERE RankInMajor <= TotalStudents / 2;
   ```




