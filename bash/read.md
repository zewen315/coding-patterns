# Bash `read`

`read` reads one line from standard input (or a file) and stores it into variables.

## Syntax

```bash
read [options] variable
```

---

## Basic Usage

```bash
read name

echo "$name"
```

Input:

```text
Jake
```

Output:

```text
Jake
```

---

## Read Multiple Variables

```bash
read first last
```

Input:

```text
Jake Wang
```

Result:

```text
first="Jake"
last="Wang"
```

Extra fields are assigned to the last variable.

```bash
read a b
```

Input:

```text
1 2 3 4
```

Result:

```text
a="1"
b="2 3 4"
```

---

## Read Into an Array

```bash
read -a arr
```

Input:

```text
apple banana orange
```

Result:

```text
arr[0]="apple"
arr[1]="banana"
arr[2]="orange"
```

---

## Read a File Line by Line

```bash
while IFS= read -r line; do
    echo "$line"
done < file.txt
```

Recommended form (handles files without a trailing newline):

```bash
while IFS= read -r line || [[ -n "$line" ]]; do
    echo "$line"
done < file.txt
```

---

## Options

### `-r`

Do not treat backslashes (`\`) as escape characters.

```bash
read -r line
```

Recommended for almost all scripts.

---

### `-a`

Read words into an array.

```bash
read -a arr
```

---

### `-p`

Display a prompt.

```bash
read -p "Enter your name: " name
```

---

### `-s`

Silent mode (hide user input).

Useful for passwords.

```bash
read -s password
```

---

### `-n`

Read a fixed number of characters.

```bash
read -n 1 answer
```

Reads exactly one character.

---

### `-t`

Timeout after a number of seconds.

```bash
read -t 5 input
```

---

## `IFS=`

`IFS` (Internal Field Separator) controls how input is split.

Default separators:

- Space
- Tab
- Newline

Recommended when reading files:

```bash
IFS= read -r line
```

This preserves:

- Leading spaces
- Trailing spaces
- Tabs

---

## Exit Status

`read` returns:

| Exit Code | Meaning |
|-----------|---------|
| `0` | Successfully read a line |
| non-zero | EOF or read error |

Example:

```bash
if read line; then
    echo "Read successfully"
else
    echo "Reached EOF"
fi
```

---

## EOF

EOF = **End Of File**

When there is no more input:

```text
apple
banana
orange
```

After reading `orange`, the next `read` reaches EOF and returns a non-zero exit status.

---

## Best Practice

```bash
while IFS= read -r line || [[ -n "$line" ]]; do
    echo "$line"
done < file.txt
```

This:

- Preserves whitespace
- Preserves backslashes
- Correctly handles the last line even if it does not end with a newline
```