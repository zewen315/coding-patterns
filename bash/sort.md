# `sort` Command Cheat Sheet

`sort` sorts lines of text alphabetically, numerically, or by specified fields.

## Syntax

```bash
sort [OPTION]... [FILE]
```

Or with a pipe:

```bash
command | sort
```

---

# 1. Default Sort (Lexicographic)

Input:

```text
banana
apple
orange
```

```bash
sort file.txt
```

Output:

```text
apple
banana
orange
```

---

# 2. Reverse Order (`-r`)

```bash
sort -r file.txt
```

Output:

```text
orange
banana
apple
```

---

# 3. Numeric Sort (`-n`)

Input:

```text
100
20
3
```

```bash
sort -n file.txt
```

Output:

```text
3
20
100
```

Without `-n`:

```text
100
20
3
```

because the default comparison is lexicographic.

---

# 4. Unique Lines (`-u`)

Input:

```text
apple
banana
apple
orange
banana
```

```bash
sort -u file.txt
```

Output:

```text
apple
banana
orange
```

Equivalent to:

```bash
sort file.txt | uniq
```

---

# 5. Ignore Case (`-f`)

Input:

```text
Apple
banana
apple
Orange
```

```bash
sort -f file.txt
```

Treats uppercase and lowercase letters as equal during comparison.

---

# 6. Sort by a Field (`-k`)

Input (space-separated):

```text
Alice 90
Bob 85
Charlie 95
```

Sort by the second field:

```bash
sort -k2,2
```

Output:

```text
Bob 85
Alice 90
Charlie 95
```

---

# 7. Specify Field Delimiter (`-t`)

Input (CSV):

```text
Alice,90
Bob,85
Charlie,95
```

```bash
sort -t',' -k2,2
```

---

Tab-separated example:

```bash
sort -t $'\t' -k2,2
```

`$'\t'` represents a real **Tab** character.

---

# 8. Numeric Sort by a Field

Input:

```text
Alice 90
Bob 85
Charlie 95
```

```bash
sort -k2,2 -n
```

Output:

```text
Bob 85
Alice 90
Charlie 95
```

---

# 9. Descending Numeric Sort

```bash
sort -k2,2 -nr
```

Output:

```text
Charlie 95
Alice 90
Bob 85
```

---

# 10. Month Sort (`-M`)

Input:

```text
Jan
Mar
Feb
Dec
```

```bash
sort -M
```

Output:

```text
Jan
Feb
Mar
Dec
```

---

# 11. Human-Readable Numbers (`-h`)

Input:

```text
2K
500M
10G
100K
```

```bash
sort -h
```

Sorts values like:

- K
- M
- G
- T

according to their numeric size.

---

# 12. Version Sort (`-V`)

Input:

```text
v1
v10
v2
```

```bash
sort -V
```

Output:

```text
v1
v2
v10
```

---

# Common Examples

## Sort `/etc/passwd` by username

```bash
sort /etc/passwd
```

---

## Sort CSV by the second column

```bash
sort -t',' -k2,2 file.csv
```

---

## Sort TSV by the third column (descending)

```bash
sort -t $'\t' -k3,3 -nr file.tsv
```

---

## Sort and remove duplicates

```bash
sort -u file.txt
```

---

## Sort IP addresses numerically by the last octet

```bash
sort -t'.' -k4,4 -n
```

---

# Important Options

| Option | Description |
|---------|-------------|
| `-r` | Reverse (descending) |
| `-n` | Numeric sort |
| `-u` | Remove duplicate lines |
| `-f` | Ignore case |
| `-k N,M` | Sort by field(s) |
| `-t X` | Field delimiter |
| `-M` | Month name sort |
| `-h` | Human-readable number sort (`K`, `M`, `G`) |
| `-V` | Version number sort |

---

# `-k` Explained

```bash
sort -k2
```

Sort key starts at **field 2** and continues to the end of the line.

```bash
sort -k2,2
```

Sort **only** by field 2.

For precise field-based sorting, prefer:

```bash
sort -k2,2
```

---

# Quick Reference

| Task | Command |
|------|---------|
| Alphabetical sort | `sort file.txt` |
| Reverse sort | `sort -r file.txt` |
| Numeric sort | `sort -n file.txt` |
| Remove duplicates | `sort -u file.txt` |
| Ignore case | `sort -f file.txt` |
| Sort by second field | `sort -k2,2` |
| Sort CSV by second field | `sort -t',' -k2,2` |
| Numeric descending by second field | `sort -k2,2 -nr` |
| Sort versions | `sort -V` |
| Sort human-readable sizes | `sort -h` |

---

# Most Common Patterns

```bash
# Alphabetical
sort file.txt

# Reverse alphabetical
sort -r file.txt

# Numeric
sort -n file.txt

# Remove duplicates
sort -u file.txt

# Sort by second column
sort -k2,2

# Numeric descending by second column
sort -k2,2 -nr

# CSV (comma-delimited)
sort -t',' -k2,2

# TSV (tab-delimited)
sort -t $'\t' -k2,2
```