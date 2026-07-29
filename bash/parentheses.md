# Bash Parentheses

## Summary

| Syntax | Purpose |
|---------|---------|
| `( )` | Run commands in a **subshell** |
| `{ }` | Group commands in the **current shell** |
| `(( ))` | Arithmetic evaluation |
| `[[ ]]` | Conditional expression (Bash keyword) |
| `$( )` | Command substitution |
| `${ }` | Variable expansion |

---

# `( )` — Subshell

Commands inside run in a child shell.

```bash
pwd

(
    cd /tmp
    pwd
)

pwd
```

Output:

```text
/home/jake

/tmp

/home/jake
```

The `cd` only affects the subshell.

Useful for temporary environment changes.

---

# `{ }` — Command Group

Runs in the current shell.

```bash
pwd

{
    cd /tmp
    pwd
}

pwd
```

Output:

```text
/home/jake

/tmp

/tmp
```

Changes persist.

**Notice:**

```bash
{
    echo hello
}
```

Requires spaces and a semicolon (or newline):

```bash
{ echo hello; }
```

---

# `(( ))` — Arithmetic

Used for integer arithmetic.

```bash
(( a = 5 ))

(( a++ ))

(( a += 10 ))
```

Condition:

```bash
if (( a > 10 )); then
    echo "Large"
fi
```

Preferred over:

```bash
[[ $a -gt 10 ]]
```

for numeric comparisons.

---

# `[[ ]]` — Conditional Test

Modern Bash conditional syntax.

```bash
[[ -f file ]]

[[ $name == Jake ]]

[[ $file == *.txt ]]

[[ $input =~ ^[0-9]+$ ]]
```

Supports:

- pattern matching
- regex
- `&&`
- `||`

---

# `$( )` — Command Substitution

Execute a command and substitute its output.

```bash
today=$(date)

echo "$today"
```

Equivalent to the old syntax:

```bash
`date`
```

but much easier to read.

Nested commands work naturally:

```bash
echo "$(dirname "$(pwd)")"
```

---

# `${ }` — Variable Expansion

Expands variables and supports many operations.

Basic:

```bash
echo "${HOME}"
```

Default value:

```bash
echo "${name:-Guest}"
```

Length:

```bash
echo "${#name}"
```

Substring:

```bash
echo "${name:0:4}"
```

Remove suffix:

```bash
echo "${file%.txt}"
```

Replace:

```bash
echo "${path//old/new}"
```

---

# Example

```bash
name="Jake"

echo "${name}"
```

Output:

```text
Jake
```

---

# Best Practice

```bash
( )     Temporary subshell

{ }     Group commands

(( ))   Arithmetic

[[ ]]   Conditions

$( )    Command substitution

${ }    Variable expansion
```