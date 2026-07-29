# Bash Quotes

Quotes control how the shell interprets text.

## Summary

| Syntax | Variable Expansion | Word Splitting | Wildcard Expansion | Command Substitution |
|---------|--------------------|----------------|---------------------|----------------------|
| `$var` | ✅ | ✅ | ✅ | ✅ |
| `"$var"` | ✅ | ❌ | ❌ | ✅ |
| `'$var'` | ❌ | ❌ | ❌ | ❌ |

---

## No Quotes

Shell performs:

- Variable expansion
- Word splitting
- Wildcard (glob) expansion
- Command substitution

```bash
name="Jake Wang"

echo $name
```

Expands to:

```bash
echo Jake Wang
```

Result:

```text
Argument 1: Jake
Argument 2: Wang
```

---

## Double Quotes `"..."`

Preserves spaces while still allowing expansion.

```bash
name="Jake Wang"

echo "$name"
```

Output:

```text
Jake Wang
```

### Variable Expansion

```bash
name="Jake"

echo "Hello $name"
```

Output:

```text
Hello Jake
```

### Command Substitution

```bash
echo "Today is $(date)"
```

Example output:

```text
Today is Tue Jul 29 ...
```

### Wildcards Are NOT Expanded

```bash
echo "$HOME/*.txt"
```

Output:

```text
/home/jake/*.txt
```

---

## Single Quotes `'...'`

Everything is treated literally.

```bash
name="Jake"

echo '$name'
```

Output:

```text
$name
```

No variable expansion.

### No Command Substitution

```bash
echo 'Today is $(date)'
```

Output:

```text
Today is $(date)
```

---

## Why Quote Variables?

Without quotes:

```bash
file="My Folder/test.txt"

rm $file
```

Shell sees:

```bash
rm My Folder/test.txt
```

Two arguments.

Correct:

```bash
rm "$file"
```

---

## Common Rule

Always quote variables unless you intentionally want shell expansion.

Good:

```bash
"$file"
"$HOME"
"$1"
"$@"
```

Don't quote patterns when using pattern matching:

```bash
[[ $file == *.log ]]
```

Not:

```bash
[[ $file == "*.log" ]]
```

The quoted version compares the literal string `*.log`.

---

## Examples

```bash
name="Jake Wang"

echo $name
# Jake Wang (split into two arguments)

echo "$name"
# Jake Wang (one argument)

echo '$name'
# $name
```

```bash
echo *.txt
# Expands to matching files

echo "*.txt"
# Prints *.txt
```

```bash
echo $(date)
# Executes date

echo "$(date)"
# Executes date and preserves spaces

echo '$(date)'
# Prints $(date)
```

---

## Best Practice

> **Default to using double quotes around variables.**

```bash
cp "$src" "$dst"

rm "$file"

grep "$pattern" "$log"

mkdir "$dir"
```

This avoids bugs caused by spaces, tabs, and special characters in filenames.