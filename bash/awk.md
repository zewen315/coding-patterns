# AWK Cheat Sheet

## What is awk?

`awk` is a **data processing language** designed to process structured text.

Unlike `grep` or `sed`, which mainly manipulate strings, `awk` treats each line as **records** and **fields**.

Think of it as:

```text
awk = Python
    + automatic file reading
    + automatic line splitting
    + built-in variables
    + associative arrays (dict)
```

---

# Processing Model

For every input line:

```text
Read one line
        ↓
Split into fields
        ↓
Execute awk code
        ↓
Read next line
```

Equivalent Python:

```python
for line in file:
    fields = line.split()
    ...
```

---

# General Syntax

```bash
awk 'pattern { action }' file
```

Think of it as:

```text
if pattern:
    action
```

Example:

```bash
awk '$2 > 90 {print $1}'
```

Equivalent Python:

```python
for line in file:
    fields = line.split()

    if int(fields[1]) > 90:
        print(fields[0])
```

---

# Built-in Variables

## $0

Entire line.

```bash
awk '{print $0}'
```

Input

```text
alice 90
```

Output

```text
alice 90
```

---

## $1

First field.

```bash
awk '{print $1}'
```

Output

```text
alice
```

---

## $2

Second field.

```bash
awk '{print $2}'
```

Output

```text
90
```

---

## $NF

Last field.

```bash
awk '{print $NF}'
```

Example

```text
alice 90 engineer
```

Output

```text
engineer
```

Equivalent Python:

```python
fields[-1]
```

---

## NF

Number of fields.

```bash
awk '{print NF}'
```

Equivalent Python:

```python
len(fields)
```

---

## NR

Record number (line number).

```bash
awk '{print NR, $0}'
```

Output

```text
1 alice 90
2 bob 85
```

Equivalent Python:

```python
for i, line in enumerate(file, start=1):
```

---

# print

Print fields.

```bash
awk '{print $1}'
```

Print multiple values.

```bash
awk '{print $1, $2}'
```

Output

```text
alice 90
```

---

## String Concatenation

Unlike most languages, awk concatenates strings simply by placing them together.

```bash
awk '{print $1 ":" $2}'
```

Output

```text
alice:90
```

Equivalent Python:

```python
print(fields[0] + ":" + fields[1])
```

---

# Pattern

Only execute on matching lines.

Example:

```bash
awk '$2 > 90'
```

Default action is:

```awk
{print}
```

Equivalent to:

```bash
awk '$2 > 90 {print $0}'
```

---

Regex pattern:

```bash
awk '/ERROR/'
```

Equivalent Python:

```python
if "ERROR" in line:
    print(line)
```

---

# Variables

Variables are created automatically.

```bash
awk '{sum += $2}'
```

Equivalent Python:

```python
sum += int(fields[1])
```

No declaration required.

Variables default to zero or empty string.

---

# BEGIN

Runs once before reading any input.

```bash
awk 'BEGIN {print "Start"}'
```

Equivalent Python:

```python
print("Start")

for line in file:
    ...
```

---

# END

Runs once after reading the entire file.

```bash
awk 'END {print NR}'
```

Equivalent Python:

```python
for line in file:
    ...

print(total_lines)
```

---

# BEGIN + Main + END

Typical structure:

```awk
BEGIN {

}

{

}

END {

}
```

Equivalent Python:

```python
# BEGIN

for line in file:
    # Main

# END
```

---

# Sum Example

Input

```text
alice 90
bob 85
charlie 95
```

awk

```bash
awk '{sum += $2} END {print "Total:", sum}'
```

Output

```text
Total: 270
```

Equivalent Python:

```python
sum = 0

for line in file:
    fields = line.split()
    sum += int(fields[1])

print(sum)
```

---

# Associative Arrays (Dictionary)

This is the most powerful feature of awk.

Count IP addresses.

Input

```text
10.0.0.1
10.0.0.2
10.0.0.1
10.0.0.3
10.0.0.2
10.0.0.1
```

awk

```bash
awk '{count[$1]++} END {for (ip in count) print ip, count[ip]}'
```

Output

```text
10.0.0.1 3
10.0.0.2 2
10.0.0.3 1
```

Equivalent Python:

```python
count = {}

for line in file:
    ip = line.strip()
    count[ip] = count.get(ip, 0) + 1

for ip in count:
    print(ip, count[ip])
```

---

# Numeric Operations

```bash
awk '{print $2+10}'
```

```bash
awk '{print $2*2}'
```

```bash
awk '{print $2/1024}'
```

awk automatically converts strings to numbers when needed.

Equivalent Python:

```python
int(fields[1]) + 10
```

---

# Common Examples

First column

```bash
awk '{print $1}'
```

Last column

```bash
awk '{print $NF}'
```

Filter rows

```bash
awk '$2 > 90'
```

Filter and print first column

```bash
awk '$2 > 90 {print $1}'
```

Add 10 to score

```bash
awk '{print $1, $2+10}'
```

Count lines

```bash
awk 'END {print NR}'
```

Sum second column

```bash
awk '{sum += $2} END {print sum}'
```

Count occurrences

```bash
awk '{count[$1]++} END {for (k in count) print k, count[k]}'
```

---

# awk vs Other Tools

| Tool    | Best At                       |
| ------- | ----------------------------- |
| grep    | Filter lines                  |
| cut     | Extract fixed columns         |
| tr      | Character translation         |
| sort    | Sorting                       |
| uniq    | Deduplication                 |
| sed     | Text editing                  |
| **awk** | Data processing & aggregation |

---

# Mental Model

Think of every awk program as this Python template:

```python
# BEGIN

for line in file:
    fields = line.split()

    # pattern

    # action

# END
```

Most real-world awk scripts only use these concepts:

* `$0`, `$1`, `$NF`
* `NR`, `NF`
* `print`
* Variables (`sum += ...`)
* Associative arrays (`count[key]++`)
* `BEGIN`
* `END`

Once you understand this model, awk becomes a concise way to write small Python-like data processing scripts directly in the shell.
