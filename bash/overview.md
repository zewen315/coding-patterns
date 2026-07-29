# Shell Script

## Commonly Used

Easy:
- sort
- grep
- uniq
- cut
- tr
- wc

Hard:
- find
- sed
- awk
- xargs

---

## Script Arguments

```bash
echo "$0"   # script name
echo "$1"   # first argument
echo "$#"   # number of arguments
echo "$@"   # all arguments
```

Exit Status

```bash
exit 0      # success
exit 1      # failure

echo $?     # previous command's exit code
```

---

## Basics

Variables

```bash
name="Jake"
echo "$name"
```

Conditionals

```bash
if [ "$age" -gt 18 ]; then
    echo "Adult"
else
    echo "Child"
fi
```

for

```bash
for file in *.cpp; do
    echo "$file"
done
```

while

```bash
while [ $count -lt 5 ]; do
    ((count++))
done
```

Functions

```bash
hello() {
    echo "Hello"
}

hello
```

Case Statement

```bash
case "$1" in
    start) echo "Start" ;;
    stop)  echo "Stop" ;;
    *)     echo "Unknown" ;;
esac
```

Arrays

```bash
files=("a.txt" "b.txt")

echo "${files[0]}"
```

Command Substitution


```bash
today=$(date)
```

Arithmetic

```bash
echo $((3 + 5))
```

Redirection

```bash
ls > output.txt
ls >> output.txt
command 2> error.log
command > all.log 2>&1
```

Pipes

```bash
cat log.txt | grep ERROR | sort
```

Environment Variables

```bash
export PATH=$PATH:/my/bin
```

Alias

```bash
alias ll="ls -al"
```

Source

```bash
source ~/.bashrc
```

or

```bash
. ~/.bashrc
```

Boolean Operators

```bash
mkdir test && cd test

make || echo "Build failed"
```

Comments

```bash
# This is a comment
```
---