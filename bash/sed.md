# sed Cheat Sheet

## What is `sed`?

`sed` (Stream EDitor) is a **stream editor** for processing text line by line.

Processing model:

```text
Read one line
      ↓
Execute sed commands
      ↓
Print the result
      ↓
Read next line
```

By default, `sed` **does not modify the original file**.

---

# General Syntax

```bash
sed '[address] command' file
```

Think of it as:

```text
[address] command
```

* **address** → Which line(s) should this command apply to?
* **command** → What should be done?

Examples:

```bash
sed '3d' file
```

```text
address = line 3
command = delete
```

---

```bash
sed '/ERROR/d' file
```

```text
address = lines matching /ERROR/
command = delete
```

---

## Addresses

### Every line (default)

```bash
sed 's/foo/bar/'
```

Applies to every line.

---

### Line number

```bash
sed '5d'
```

Delete line 5.

---

### Line range

```bash
sed '3,8d'
```

Delete lines 3–8.

---

### Regex

```bash
sed '/ERROR/d'
```

Delete lines containing `ERROR`.

---

### Start and end regex

```bash
sed '/BEGIN/,/END/d'
```

Delete everything between BEGIN and END (inclusive).

---

# The Most Important Command: `s`

Substitute.

Syntax:

```bash
s/regex/replacement/flags
```

Think of it as:

```text
Substitute(
    regex,
    replacement,
    flags
)
```

Example:

```bash
sed 's/apple/APPLE/'
```

Only replaces the **first** match on each line.

---

## Global replacement

```bash
sed 's/apple/APPLE/g'
```

`g`

means:

```text
Replace ALL matches on EACH line.
```

Not the whole file.

---

## Regex

Replace any password:

```bash
sed 's/^password=.*$/password=******/'
```

---

## Common flags

### g

Replace every match.

```bash
sed 's/foo/bar/g'
```

---

### I (GNU sed)

Ignore case.

```bash
sed 's/error/ERROR/I'
```

---

# Delete Command

Syntax:

```bash
/address/d
```

Examples:

Delete lines containing apple:

```bash
sed '/apple/d'
```

---

Delete line 3:

```bash
sed '3d'
```

---

Delete lines 3-5:

```bash
sed '3,5d'
```

---

Delete blank lines:

```bash
sed '/^$/d'
```

---

Delete whitespace-only lines:

```bash
sed '/^[[:space:]]*$/d'
```

---

# Print Command

Normally, `sed` prints every line.

To print selectively:

```bash
sed -n '/ERROR/p'
```

Meaning:

* Don't print everything (`-n`)
* Print matching lines (`p`)

---

# Insert

Insert **before** a line.

```bash
sed '/ERROR/i\
### Error Found
'
```

Output:

```text
### Error Found
ERROR database timeout
```

---

# Append

Insert **after** a line.

```bash
sed '/ERROR/a\
Please investigate.
'
```

---

# Change

Replace the entire line.

```bash
sed '/ERROR/c\
System failed.
'
```

---

# Capture Groups

Enable extended regex:

```bash
sed -E 's/^name=(.*)$/Hello \1/'
```

Input:

```text
name=alice
```

Output:

```text
Hello alice
```

Explanation:

```text
(.*)
```

captures

```text
alice
```

Later:

```text
\1
```

references the first captured group.

---

Multiple groups:

```bash
sed -E 's/(.*),(.*)/\2,\1/'
```

Input:

```text
John,Doe
```

Output:

```text
Doe,John
```

---

# Common Regex

| Regex         | Meaning                  |
| ------------- | ------------------------ |
| `^`           | Beginning of line        |
| `$`           | End of line              |
| `.`           | Any character            |
| `.*`          | Any number of characters |
| `[0-9]`       | Digit                    |
| `[a-z]`       | Lowercase letter         |
| `[A-Z]`       | Uppercase letter         |
| `[[:space:]]` | Whitespace               |
| `( )`         | Capture group (`-E`)     |

---

# In-place Editing

Modify the original file.

Linux:

```bash
sed -i 's/foo/bar/g' file
```

macOS:

```bash
sed -i '' 's/foo/bar/g' file
```

---

# Single Quotes vs Double Quotes

Almost always use **single quotes**.

```bash
sed 's/$HOME/test/'
```

Shell does **not** expand variables.

Double quotes:

```bash
sed "s/$HOME/test/"
```

Shell expands `$HOME` **before** running `sed`.

---

# How to Read a sed Command

Instead of reading:

```bash
sed 's/^server=.*$/server=localhost/'
```

as a string...

Read it as:

```text
Command:
    Substitute

Regex:
    ^server=.*$

Replacement:
    server=localhost
```

Equivalent pseudocode:

```python
for line in file:
    if regex_match("^server=.*$", line):
        line = "server=localhost"
```

---

Another example:

```bash
sed '/ERROR/d'
```

Read it as:

```text
Address:
    /ERROR/

Command:
    delete
```

Equivalent pseudocode:

```python
for line in file:
    if "ERROR" in line:
        continue
    print(line)
```

---

# Mental Model

Every `sed` command follows the same pattern:

```text
[address] command
```

Most common commands:

| Command | Meaning       |
| ------- | ------------- |
| `s`     | Substitute    |
| `d`     | Delete line   |
| `p`     | Print line    |
| `i`     | Insert before |
| `a`     | Append after  |
| `c`     | Change line   |

Think of `sed` as a tiny programming language:

```text
for each line:
    if address matches:
        execute command
```

Once you understand this model, most `sed` commands become easy to read and write.
