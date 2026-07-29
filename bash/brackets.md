# Bash Scripting

## Test Expressions

### `[ ]` vs `[[ ]]`

Both are used for conditional testing, but `[[ ]]` is the modern Bash syntax and is generally preferred.

| Feature | `[ ]` | `[[ ]]` |
|---------|------|---------|
| POSIX compatible | ✅ | ❌ (Bash/Ksh/Zsh only) |
| Implemented as | `test` command | Bash keyword |
| Variable quoting required | Usually | Usually not |
| Pattern matching (`*.txt`) | ❌ | ✅ |
| Regex (`=~`) | ❌ | ✅ |
| Complex logic (`&&`, `||`) | Awkward | ✅ |

### Basic Examples

```bash
if [ "$name" = "Jake" ]; then
    echo "Hello"
fi
```

```bash
if [[ $name == "Jake" ]]; then
    echo "Hello"
fi
```

---

## File Tests

```bash
[[ -f file ]]    # regular file exists
[[ -d dir ]]     # directory exists
[[ -e path ]]    # file or directory exists
[[ -r file ]]    # readable
[[ -w file ]]    # writable
[[ -x file ]]    # executable
[[ -s file ]]    # file is not empty
```

---

## String Tests

```bash
[[ -z $str ]]        # empty string
[[ -n $str ]]        # non-empty string

[[ $a == $b ]]       # equal
[[ $a != $b ]]       # not equal
[[ $a < $b ]]        # lexicographically smaller
[[ $a > $b ]]        # lexicographically greater
```

### Pattern Matching

```bash
[[ $file == *.log ]]
[[ $name == user_* ]]
```

### Regular Expressions

```bash
[[ $input =~ ^[0-9]+$ ]]
```

---

## Numeric Tests

```bash
[[ $a -eq $b ]]      # ==
[[ $a -ne $b ]]      # !=
[[ $a -lt $b ]]      # <
[[ $a -le $b ]]      # <=
[[ $a -gt $b ]]      # >
[[ $a -ge $b ]]      # >=
```

### Arithmetic Syntax

Preferred for arithmetic:

```bash
(( a > b ))
(( a <= b ))
(( a += 1 ))
```

Example:

```bash
if (( age >= 18 )); then
    echo "Adult"
fi
```

---

## Logical Operators

```bash
[[ $age -gt 18 && $country == "US" ]]

[[ $age -gt 18 || $admin == true ]]

[[ ! -f file ]]
```

---

## Exit Status

Every command returns an exit code.

```bash
0     success
non-0 failure
```

Example:

```bash
mkdir test

echo $?
```

```bash
grep ERROR app.log

if [[ $? -eq 0 ]]; then
    echo "Found"
fi
```

More idiomatic:

```bash
if grep ERROR app.log; then
    echo "Found"
fi
```

---

## Variables

```bash
name="Jake"

echo "$name"
```

Command substitution:

```bash
today=$(date)

files=$(ls)
```

---

## Arrays

```bash
arr=(apple banana orange)

echo "${arr[0]}"

echo "${arr[@]}"

echo "${#arr[@]}"
```

Loop:

```bash
for item in "${arr[@]}"; do
    echo "$item"
done
```

---

## Conditionals

```bash
if [[ condition ]]; then
    ...
elif [[ condition ]]; then
    ...
else
    ...
fi
```

---

## Loops

### for

```bash
for file in *.txt; do
    echo "$file"
done
```

### while

```bash
while read line; do
    echo "$line"
done < input.txt
```

### C-style

```bash
for ((i=0; i<10; i++)); do
    echo "$i"
done
```

---

## Functions

```bash
hello() {
    echo "Hello"
}

hello
```

Arguments:

```bash
sum() {
    echo $(($1 + $2))
}

sum 3 5
```

---

## Common Special Variables

```bash
$0      script name
$1      first argument
$2      second argument

$#      number of arguments
$@      all arguments
$*      all arguments (single string)

$?      last exit code
$$      current process ID
```

---

## Pipes

```bash
cat log.txt | grep ERROR | sort | uniq -c | sort -nr
```

---

## Redirection

```bash
>       overwrite

>>      append

<       input

2>      stderr

2>&1    redirect stderr to stdout
```

Example:

```bash
command > output.txt

command >> output.txt

command > output.txt 2>&1
```

---

## Common Commands

### Text Processing

```bash
grep
sed
awk
cut
sort
uniq
tr
xargs
head
tail
wc
```

### Files

```bash
ls
cp
mv
rm
find
chmod
chown
ln
```

### Process

```bash
ps
top
kill
pkill
pgrep
```

### Network

```bash
ss
netstat
curl
wget
dig
ping
```

### Disk

```bash
df
du
mount
```

### System

```bash
systemctl
journalctl
dmesg
```

---

## Best Practices

Always quote variables unless you intentionally want word splitting.

```bash
"$file"
"$name"
"$@"
```

Prefer:

```bash
[[ ... ]]
```

instead of

```bash
[ ... ]
```

Use arithmetic syntax for numbers:

```bash
(( count++ ))
```

instead of

```bash
count=$((count + 1))
```

Use command substitution:

```bash
$(...)
```

instead of legacy backticks:

```bash
`...`
```

---

## Shell Script Template

```bash
#!/usr/bin/env bash

set -euo pipefail

main() {

}

main "$@"
```

### `set -euo pipefail`

```text
-e   Exit immediately if a command fails.

-u   Treat undefined variables as errors.

-o pipefail
     Return the first failed command in a pipeline.
```