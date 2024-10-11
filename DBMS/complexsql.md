# Complex SQL Queries 🔥
---


# Write a SQL Query to fetch all the duplicate records in a table.

### Simplest SQL Query

**SQL Query:**
```sql
SELECT email, COUNT(*) as count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

**Explanation:**
- **`SELECT email, COUNT(*) as count`**: This part selects the `email` column and counts how many times each email appears in the `users` table.
- **`FROM users`**: Specifies the source table.
- **`GROUP BY email`**: Groups the results by the `email` column.
- **`HAVING COUNT(*) > 1`**: Filters the results to show only those emails that appear more than once, indicating duplicates.

### Complex SQL Query

**SQL Query:**
```sql
WITH DuplicateRecords AS (
    SELECT 
        id, 
        email, 
        first_name, 
        last_name, 
        ROW_NUMBER() OVER (PARTITION BY email, first_name ORDER BY id) AS row_num
    FROM users
)
SELECT *
FROM DuplicateRecords
WHERE row_num > 1;
```

**Explanation:**
- **Common Table Expression (CTE)**: 
  - The CTE named `DuplicateRecords` retrieves records from the `users` table.
  - **`ROW_NUMBER() OVER (PARTITION BY email, first_name ORDER BY id)`**: Assigns a unique row number to each record within each group of `email` and `first_name`, ordered by `id`. This helps identify duplicates.
- **Final Selection**:
  - The outer query selects all columns from `DuplicateRecords`.
  - **`WHERE row_num > 1`**: Filters the results to include only duplicate records (those with a row number greater than 1).
 
---

# Write a SQL query to fetch the second last record from the employee table.

## Simple Query
```sql
SELECT *
FROM EMPLOYEE
ORDER BY employee_id DESC
LIMIT 1 OFFSET 1;
```
### Explanation:
- This query orders the records in the `EMPLOYEE` table by `employee_id` in descending order.
- **`LIMIT 1 OFFSET 1`**: This combination retrieves the second record from the ordered result, effectively giving you the second last record.

## Complex Query
```sql
WITH RankedEmployees AS (
    SELECT *,
           ROW_NUMBER() OVER (ORDER BY employee_id DESC) AS rn
    FROM EMPLOYEE
)
SELECT *
FROM RankedEmployees
WHERE rn = 2;
```
### Explanation:
- The Common Table Expression (CTE) named `RankedEmployees` assigns a row number to each employee based on their `employee_id` in descending order.
- **`ROW_NUMBER() OVER (ORDER BY employee_id DESC)`**: This function generates a unique row number for each employee.
- The outer query selects all columns from the CTE where the row number (`rn`) equals 2, retrieving the second last record from the employee table.

Feel free to ask if you have more questions!

### Summary of Comparison
- The **simplest query** quickly identifies duplicate emails without providing full context for the duplicate entries.
- The **complex query** offers more detail by retrieving all relevant columns for duplicates, making it useful when you need to see additional information about the duplicate entries, such as user IDs and names.

---

# Write a SQL query to display only the details of employees who either earn the highest salary or the lowest salary in each department from the employee table.

## Simple Query
```sql
SELECT *
FROM EMPLOYEE
WHERE salary = (SELECT MAX(salary) FROM EMPLOYEE e WHERE e.department_id = EMPLOYEE.department_id)
   OR salary = (SELECT MIN(salary) FROM EMPLOYEE e WHERE e.department_id = EMPLOYEE.department_id);
```
### Explanation:
- This query selects all columns from the `EMPLOYEE` table where the salary is equal to the maximum salary or minimum salary within the same department.
- It uses subqueries to find the highest and lowest salaries for each department, effectively filtering the main query results.

## Complex Query
```sql
WITH RankedSalaries AS ( 
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC) AS max_rank,
           ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary ASC) AS min_rank
    FROM EMPLOYEE
)
SELECT *
FROM RankedSalaries
WHERE max_rank = 1 OR min_rank = 1;
```
### Explanation:
- The Common Table Expression (CTE) named `RankedSalaries` assigns two row numbers to each employee: one for the maximum salary (`max_rank`) and another for the minimum salary (`min_rank`) within each department.
- **`ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary DESC)`**: Assigns a rank to each employee based on their salary in descending order.
- **`ROW_NUMBER() OVER (PARTITION BY department_id ORDER BY salary ASC)`**: Assigns a rank based on their salary in ascending order.
- The outer query then selects all records where the rank is 1 for either the maximum or minimum salary, thus displaying employees who earn the highest or lowest salary in each department.


# Fetch all doctors who are working in the same hospital but have different specialties.

```sql
SELECT d1.*
FROM doctors d1
JOIN doctors d2 ON d1.id != d2.id 
WHERE d1.hospital = d2.hospital 
AND d1.specialty = d2.specialty;
```


---

# From the login_details table, fetch the users who logged in consecutively 3 or more times.

```sql
SELECT *, 
    CASE 
        WHEN user_name = LEAD(user_name) OVER (ORDER BY login_id) 
             AND user_name = LEAD(user_name, 2) OVER (ORDER BY login_id) 
        THEN user_name 
        ELSE NULL 
    END AS repeated_users 
FROM login_details 
WHERE repeated_users IS NOT NULL;
```

### Explanation:
1. **LEAD Function**:
   - The `LEAD` function is used to look ahead in the result set. Here, it checks if the `user_name` is the same as the next user name and the user name two positions ahead.
   - `LEAD(user_name) OVER (ORDER BY login_id)` checks the next row.
   - `LEAD(user_name, 2) OVER (ORDER BY login_id)` checks two rows ahead.

2. **CASE Statement**:
   - The `CASE` statement evaluates if the current `user_name` is the same as both the next and the next-to-next entries. If so, it returns the `user_name`; otherwise, it returns `NULL`.

3. **Filtering Repeated Users**:
   - The `WHERE repeated_users IS NOT NULL` clause filters the results to only show rows where the user has logged in consecutively at least three times.

### Assumptions:
- This query assumes that `login_id` is a column that uniquely identifies each login event and is in chronological order.
- The `user_name` column holds the names of users who logged in. 


