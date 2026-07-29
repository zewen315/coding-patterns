# `tr` Command Cheat Sheet

`tr` (translate) translates, deletes, or squeezes characters from standard input.

> **Note:** `tr` only reads from **stdin**, not directly from files.

## Syntax

```bash
tr [OPTION] SET1 [SET2]
```

---

# 1. Character Translation

Replace characters in `SET1` with corresponding characters in `SET2`.

## Lowercase → Uppercase

```bash
echo "hello" | tr 'a-z' 'A-Z'
```

Output:

```text
HELLO
```

---

## Uppercase → Lowercase

```bash
echo "HELLO" | tr 'A-Z' 'a-z'
```

Output:

```text
hello
```

---

## Replace Parentheses with Brackets

```bash
echo "(a+b)*(c-d)" | tr "()" "[]"
```

Output:

```text
[a+b]*[c-d]
```

---

# 2. Delete Characters (`-d`)

Delete all characters in `SET1`.

## Delete lowercase letters

```bash
echo "HelloWorld123" | tr -d 'a-z'
```

Output:

```text
HW123
```

---

## Delete digits

```bash
echo "abc123xyz" | tr -d '0-9'
```

Output:

```text
abcxyz
```

---

## Delete spaces

```bash
echo "Hello World" | tr -d ' '
```

Output:

```text
HelloWorld
```

---

## Delete whitespace

```bash
tr -d '[:space:]'
```

Deletes spaces, tabs, and newlines.

---

# 3. Squeeze Repeated Characters (`-s`)

Replace consecutive repeated characters with a single one.

## Squeeze spaces

```bash
echo "Hello     World" | tr -s ' '
```

Output:

```text
Hello World
```

---

## Squeeze repeated digits

```bash
echo "111223333" | tr -s '0-9'
```

Output:

```text
123
```

---

## Squeeze repeated newlines

```bash
tr -s '\n'
```

---

# 4. Character Classes

Instead of explicit ranges, use POSIX character classes.

| Class | Description |
|--------|-------------|
| `[:lower:]` | Lowercase letters |
| `[:upper:]` | Uppercase letters |
| `[:alpha:]` | Alphabetic characters |
| `[:digit:]` | Digits |
| `[:alnum:]` | Letters and digits |
| `[:space:]` | Whitespace |
| `[:punct:]` | Punctuation |

Example:

```bash
echo "hello123" | tr '[:lower:]' '[:upper:]'
```

Output:

```text
HELLO123
```

---

# 5. Common Examples

## Convert to uppercase

```bash
cat file.txt | tr 'a-z' 'A-Z'
```

---

## Convert to lowercase

```bash
cat file.txt | tr 'A-Z' 'a-z'
```

---

## Remove all digits

```bash
cat file.txt | tr -d '0-9'
```

---

## Remove blank lines

```bash
tr -s '\n'
```

---

## Normalize multiple spaces

```bash
cat file.txt | tr -s ' '
```

---

# Quick Reference

| Option | Description | Example |
|---------|-------------|---------|
| `tr 'a-z' 'A-Z'` | Translate characters | Convert to uppercase |
| `tr 'A-Z' 'a-z'` | Translate characters | Convert to lowercase |
| `tr -d 'a-z'` | Delete characters | Remove lowercase letters |
| `tr -d '0-9'` | Delete digits | Remove numbers |
| `tr -d '[:space:]'` | Delete whitespace | Remove spaces, tabs, newlines |
| `tr -s ' '` | Squeeze repeated spaces | Collapse multiple spaces |
| `tr -s '\n'` | Squeeze repeated newlines | Remove extra blank lines |

---

# Most Common Patterns

```bash
# Uppercase
tr 'a-z' 'A-Z'

# Lowercase
tr 'A-Z' 'a-z'

# Delete lowercase letters
tr -d 'a-z'

# Delete digits
tr -d '0-9'

# Collapse multiple spaces
tr -s ' '

# Replace parentheses with brackets
tr '()' '[]'
```