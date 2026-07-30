# Pivot (Rows ↔ Columns)

Two directions of the same idea: reshaping data between a "long" (row-based) and "wide" (column-based) layout.

---

## 1. Rows → Columns (Pivot)

**Use Case**

Transform rows into columns.

Input:

| id | event | time |
|----|-------|------|
| 1 | start | 10:00 |
| 1 | end | 10:30 |
| 2 | start | 11:00 |
| 2 | end | 11:20 |

Output:

| id | start_time | end_time |
|----|------------|----------|
| 1 | 10:00 | 10:30 |
| 2 | 11:00 | 11:20 |

```sql
SELECT
    id,
    MAX(CASE WHEN event = 'start' THEN time END) AS start_time,
    MAX(CASE WHEN event = 'end' THEN time END) AS end_time
FROM EventLog
GROUP BY id;
```

How it works:

For `start_time`:

```
start -> 10:00
end   -> NULL
```

After grouping:

```
MAX(10:00, NULL) = 10:00
```

Likewise for `end_time`.

Common interview questions:

- Start / End event logs
- Order status
- Gender statistics
- Monthly pivot tables

---

## 2. Columns → Rows (Unpivot)

**Use Case**

Transform columns into rows — the reverse of the above. Given one row per entity with several attribute columns, produce one row per (entity, attribute) pair.

Input:

| id | start_time | end_time |
|----|------------|----------|
| 1 | 10:00 | 10:30 |
| 2 | 11:00 | 11:20 |

Output:

| id | event | time |
|----|-------|------|
| 1 | start | 10:00 |
| 1 | end | 10:30 |
| 2 | start | 11:00 |
| 2 | end | 11:20 |

```sql
SELECT id, 'start' AS event, start_time AS time
FROM EventLog
UNION ALL
SELECT id, 'end' AS event, end_time AS time
FROM EventLog;
```

How it works:

Each `SELECT` peels off one column and relabels it as an `event`/`time` pair. `UNION ALL` stacks those results into a single long table (use `UNION ALL`, not `UNION`, so genuine duplicate rows aren't silently dropped).

Common interview questions:

- Reconstructing an event log from a wide status table
- Turning monthly columns (`jan`, `feb`, ...) into `(month, value)` rows
- Normalizing a denormalized "wide" table before aggregating it

---

## Cheat Sheet

| Direction | SQL |
|-----------|-----|
| Row → Column | `MAX(CASE WHEN ... THEN ... END)` |
| Column → Row | `SELECT ... UNION ALL SELECT ...` |
