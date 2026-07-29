# `cut` Command Cheat Sheet

`cut` extracts sections from each line of input.

## Syntax

```bash
cut [OPTION]... [FILE]
```

Commonly used with pipes:

```bash
command | cut ...
```

---

# 1. Cut by Characters (`-c`)

### First character

```bash
echo "abcdefg" | cut -c1
```

Output:

```text
a
```

### First 3 characters

```bash
echo "abcdefg" | cut -c1-3
```

Output:

```text
abc
```

### Characters 3–5

```bash
echo "abcdefg" | cut -c3-5
```

Output:

```text
cde
```

### From character 5 to the end

```bash
echo "abcdefg" | cut -c5-
```

Output:

```text
efg
```

### Multiple positions

```bash
echo "abcdefg" | cut -c1,3,5
```

Output:

```text
ace
```

---

# 2. Cut by Bytes (`-b`)

Useful for byte-oriented data.

```bash
echo "abcdef" | cut -b1-3
```

Output:

```text
abc
```

> **Note:** For ASCII text, `-b` and `-c` behave the same. For UTF-8 (e.g., Chinese), `-b` may split a character in the middle.

---

# 3. Cut by Fields (`-f`)

Given:

```text
Tom:20:NY
Alice:18:CA
Bob:30:TX
```

### First field

```bash
cut -d':' -f1 file.txt
```

Output:

```text
Tom
Alice
Bob
```

### Second field

```bash
cut -d':' -f2 file.txt
```

Output:

```text
20
18
30
```

### First and third fields

```bash
cut -d':' -f1,3 file.txt
```

Output:

```text
Tom:NY
Alice:CA
Bob:TX
```

### From the second field to the end

```bash
cut -d':' -f2- file.txt
```

Output:

```text
20:NY
18:CA
30:TX
```

---

# 4. Specify Delimiter (`-d`)

CSV example:

```bash
echo "Tom,20,NY" | cut -d',' -f2
```

Output:

```text
20
```

Space-delimited example:

```bash
echo "Tom 20 NY" | cut -d' ' -f2
```

---

# 5. Common Examples

## Get usernames from `/etc/passwd`

```bash
cut -d':' -f1 /etc/passwd
```

## Get the first octet of an IP address

```bash
echo "192.168.1.10" | cut -d'.' -f1
```

Output:

```text
192
```

## Get a file extension

```bash
echo "photo.jpg" | cut -d'.' -f2
```

Output:

```text
jpg
```

---

# `cut` vs `awk`

`cut` uses a fixed delimiter.

```bash
cut -d':' -f2 file.txt
```

`awk` handles arbitrary whitespace automatically.

```bash
awk '{print $2}'
```

Use:

- `cut` → Fixed delimiter (CSV, TSV, logs)
- `awk` → Variable whitespace or more complex processing

---

# Quick Reference

| Option | Description | Example |
|---------|-------------|---------|
| `-c N` | Character N | `cut -c1` |
| `-c M-N` | Characters M to N | `cut -c2-5` |
| `-c N-` | Character N to end | `cut -c5-` |
| `-b N` | Byte N | `cut -b1` |
| `-b M-N` | Bytes M to N | `cut -b1-5` |
| `-d X` | Delimiter | `cut -d':'` |
| `-f N` | Field N | `cut -d':' -f2` |
| `-f M,N` | Multiple fields | `cut -d',' -f1,3` |
| `-f M-` | Field M to end | `cut -d':' -f2-` |

---

# Most Common Patterns

```bash
# Characters
cut -c1-5 file.txt

# Bytes
cut -b1-8 file.txt

# First field (colon-separated)
cut -d':' -f1 file.txt

# Second field (comma-separated)
cut -d',' -f2 file.csv

# Fields 2 through end
cut -d':' -f2- file.txt
```