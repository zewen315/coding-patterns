# Date Operators

Common date/time functions that show up in SQL interview questions. Syntax varies by dialect — examples below use MySQL, with Postgres/SQL Server noted where they differ.

---

## 1. Current Date / Time

```sql
SELECT NOW();          -- current date + time
SELECT CURDATE();       -- current date only
SELECT CURRENT_DATE;    -- ANSI standard, works almost everywhere
```

Useful for:

- "active in the last N days" filters
- Default values / audit columns

---

## 2. DATEDIFF (difference between two dates)

**Use Case**

How many days/months/years apart are two dates?

```sql
SELECT DATEDIFF(end_date, start_date) AS days_between
FROM Bookings;
```

Order matters: `DATEDIFF(later, earlier)` gives a positive number.

Dialect differences:

```
MySQL:      DATEDIFF(date1, date2)               -- always whole days
Postgres:   date1 - date2                          -- integer days (no DATEDIFF function)
SQL Server: DATEDIFF(day, date1, date2)            -- unit is an explicit first arg
```

Common interview questions:

- Days between signup and first purchase
- Subscription length
- Time-to-resolution for tickets

---

## 3. Date Arithmetic (DATE_ADD / DATE_SUB / INTERVAL)

**Use Case**

Shift a date forward or backward by some amount.

```sql
SELECT DATE_ADD(order_date, INTERVAL 7 DAY) AS due_date
FROM Orders;

SELECT DATE_SUB(NOW(), INTERVAL 30 DAY) AS thirty_days_ago;
```

Postgres uses plain arithmetic with `INTERVAL`:

```sql
SELECT order_date + INTERVAL '7 days' AS due_date
FROM Orders;
```

Useful for:

- "orders placed in the last 30 days" (`WHERE order_date >= CURDATE() - INTERVAL 30 DAY`)
- Computing due dates / expiry dates
- Rolling windows

---

## 4. Extracting Parts (YEAR / MONTH / DAY / EXTRACT)

**Use Case**

Pull out a component of a date to group or filter by it.

```sql
SELECT
    YEAR(order_date)  AS yr,
    MONTH(order_date) AS mo,
    DAY(order_date)   AS d
FROM Orders;
```

ANSI standard (works in Postgres, and MySQL supports it too):

```sql
SELECT EXTRACT(YEAR FROM order_date) AS yr
FROM Orders;
```

Common interview questions:

- Revenue by month/year
- Signups by day of week (`DAYOFWEEK()` / `EXTRACT(DOW FROM ...)`)
- Cohort analysis (group users by signup month)

---

## 5. Truncating to a Period (DATE_TRUNC / DATE_FORMAT)

**Use Case**

Collapse a timestamp down to the start of its containing day/week/month, so rows in the same period group together.

Postgres/SQL Server style:

```sql
SELECT DATE_TRUNC('month', order_date) AS month_start
FROM Orders;
```

MySQL has no `DATE_TRUNC`; simulate it with `DATE_FORMAT`:

```sql
SELECT DATE_FORMAT(order_date, '%Y-%m-01') AS month_start
FROM Orders;
```

Useful for:

- Monthly / weekly rollups
- `GROUP BY` on a truncated date instead of the raw timestamp

---

## 6. Formatting Dates (DATE_FORMAT / TO_CHAR)

**Use Case**

Render a date as a string in a specific shape (for display, not for comparison).

```sql
-- MySQL
SELECT DATE_FORMAT(order_date, '%Y-%m-%d') AS formatted;

-- Postgres
SELECT TO_CHAR(order_date, 'YYYY-MM-DD') AS formatted;

-- SQL Server
SELECT FORMAT(order_date, 'yyyy-MM-dd') AS formatted;
```

Note: format strings are dialect-specific (`%Y` vs `YYYY`), so this is the one function you should always double-check against docs.

---

## Cheat Sheet

| Need | MySQL | Postgres | SQL Server |
|------|-------|----------|------------|
| Now | `NOW()` | `NOW()` | `GETDATE()` |
| Today | `CURDATE()` | `CURRENT_DATE` | `CAST(GETDATE() AS DATE)` |
| Diff in days | `DATEDIFF(a, b)` | `a - b` | `DATEDIFF(day, b, a)` |
| Add interval | `DATE_ADD(d, INTERVAL n UNIT)` | `d + INTERVAL 'n unit'` | `DATEADD(unit, n, d)` |
| Subtract interval | `DATE_SUB(d, INTERVAL n UNIT)` | `d - INTERVAL 'n unit'` | `DATEADD(unit, -n, d)` |
| Extract part | `YEAR(d)` / `MONTH(d)` | `EXTRACT(YEAR FROM d)` | `DATEPART(year, d)` |
| Truncate to period | `DATE_FORMAT(d, '%Y-%m-01')` | `DATE_TRUNC('month', d)` | `DATETRUNC(month, d)` |
| Format as string | `DATE_FORMAT(d, fmt)` | `TO_CHAR(d, fmt)` | `FORMAT(d, fmt)` |
