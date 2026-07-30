# SQL Patterns

A collection of common SQL interview patterns.

---

# 1. Conditional Aggregation (Pivot)

See [pivot.md](pivot.md) for rows → columns and the reverse (columns → rows).

---

# 2. Self Join

**Use Case**

Join different rows of the same table.

Example:

```sql
SELECT
    s.id,
    s.time AS start_time,
    e.time AS end_time
FROM EventLog s
JOIN EventLog e
ON s.id = e.id
WHERE s.event = 'start'
  AND e.event = 'end';
```

Think of one table as two different tables.

```
EventLog (start)
        JOIN
EventLog (end)
```

Common interview questions:

- Employee / Manager
- Previous day / Current day
- Start / End events

---

# 3. Conditional Count

Count rows satisfying a condition.

```sql
SELECT
    department,
    SUM(CASE WHEN gender = 'M' THEN 1 ELSE 0 END) AS male_count,
    SUM(CASE WHEN gender = 'F' THEN 1 ELSE 0 END) AS female_count
FROM Employee
GROUP BY department;
```

Equivalent logic:

```
if gender == 'M':
    +1
else:
    +0
```

---

# 4. Conditional Sum

Sum values satisfying a condition.

```sql
SELECT
    customer_id,
    SUM(CASE WHEN type = 'deposit' THEN amount ELSE 0 END) AS deposits,
    SUM(CASE WHEN type = 'withdraw' THEN amount ELSE 0 END) AS withdrawals
FROM Transactions
GROUP BY customer_id;
```

Useful for:

- Revenue by category
- Expenses
- Financial reports

---

# 5. MIN / MAX as First / Last

When records are naturally ordered.

Example:

```sql
SELECT
    id,
    MIN(timestamp) AS first_seen,
    MAX(timestamp) AS last_seen
FROM Log
GROUP BY id;
```

Useful for:

- Session start/end
- First login
- Last activity

---

# 6. LEFT JOIN + IFNULL

Return all rows from the left table.

```sql
SELECT
    u.name,
    IFNULL(SUM(r.distance), 0) AS travelled_distance
FROM Users u
LEFT JOIN Rides r
ON u.id = r.user_id
GROUP BY u.id, u.name;
```

Pattern:

```
LEFT JOIN
↓

Keep every row on the left.

Missing matches become NULL.

↓

IFNULL(..., 0)
```

Common interview questions:

- Users with no orders
- Customers with zero purchases
- Employees without managers

---

# 7. NOT EXISTS

Find rows with **no matching records**.

```sql
SELECT s.name
FROM SalesPerson s
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    JOIN Company c
      ON o.com_id = c.com_id
    WHERE o.sales_id = s.sales_id
      AND c.name = 'RED'
);
```

Useful for:

- Never ordered
- Never logged in
- Never purchased

---

# 8. GROUP BY + HAVING

Filter groups instead of rows.

```sql
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
```

Execution order:

```
FROM

↓

WHERE

↓

GROUP BY

↓

HAVING

↓

SELECT

↓

ORDER BY
```

Remember:

- WHERE filters rows.
- HAVING filters groups.

---

# 9. Scalar Subquery

A subquery used as a single value.

```sql
SELECT (
    SELECT salary
    FROM Employee
    WHERE id = 100
);
```

Rules:

- 1 row → value
- 0 rows → NULL
- >1 rows → error

Useful in:

- Biggest single number
- Lookup queries

---

# 10. Window Functions

Keep every row while computing statistics.

Examples:

```sql
ROW_NUMBER()
RANK()
DENSE_RANK()
LAG()
LEAD()
```

Example:

```sql
SELECT
    *,
    ROW_NUMBER() OVER (
        PARTITION BY department
        ORDER BY salary DESC
    ) AS rn
FROM Employee;
```

Useful for:

- Top K per group
- Consecutive events
- Ranking
- Pairing start/end events

---

# Cheat Sheet

| Pattern | SQL |
|----------|-----|
| Row → Column | `MAX(CASE WHEN ... THEN ... END)` |
| Conditional Count | `SUM(CASE WHEN ... THEN 1 ELSE 0 END)` |
| Conditional Sum | `SUM(CASE WHEN ... THEN amount ELSE 0 END)` |
| Self Join | `JOIN` same table |
| Missing Records | `LEFT JOIN ... IS NULL` / `NOT EXISTS` |
| First / Last | `MIN()` / `MAX()` |
| Duplicate Detection | `GROUP BY ... HAVING COUNT(*) > 1` |
| Keep All Left Rows | `LEFT JOIN` |
| Replace NULL | `IFNULL()` / `COALESCE()` |
| Ranking | `ROW_NUMBER()` |
| Previous Row | `LAG()` |
| Next Row | `LEAD()` |
| Top K Per Group | `ROW_NUMBER() + WHERE rn <= K` |