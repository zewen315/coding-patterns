# xargs Cheat Sheet

## What is xargs?

`xargs` converts **stdin** into **command-line arguments (argv)**.

Think of it as:

```text
stdin
   │
   ▼
xargs
   │
   ▼
argv
```

Without `xargs`

```bash
echo "file1 file2 file3"
```

The output is just text.

With `xargs`

```bash
echo "file1 file2 file3" | xargs rm
```

becomes

```bash
rm file1 file2 file3
```

---

# Why xargs?

Many commands produce output through **stdin**.

Many commands expect **argv**.

Example:

```bash
find . -name "*.log"
```

Output

```text
a.log
b.log
c.log
```

But `rm` does **not** read stdin.

Instead it expects

```bash
rm a.log b.log c.log
```

`xargs` bridges the gap.

---

# Mental Model

Without xargs

```text
Producer
    │
    ▼
stdin

rm
```

Nothing happens.

With xargs

```text
Producer
    │
    ▼
stdin
    │
    ▼
xargs
    │
    ▼
argv
    │
    ▼
rm
```

---

# Basic Usage

```bash
command | xargs another_command
```

Example

```bash
find . -name "*.log" | xargs rm
```

Equivalent to

```bash
rm file1.log file2.log file3.log
```

---

# grep Example

Search every Python file for TODO.

```bash
find . -name "*.py" | xargs grep TODO
```

Equivalent to

```bash
grep TODO file1.py file2.py file3.py
```

---

# cat Example

```bash
echo "a.txt b.txt" | xargs cat
```

Equivalent

```bash
cat a.txt b.txt
```

---

# chmod Example

```bash
find . -name "*.sh" | xargs chmod +x
```

Equivalent

```bash
chmod +x file1.sh file2.sh
```

---

# mkdir Example

```bash
echo "dir1 dir2 dir3" | xargs mkdir
```

Equivalent

```bash
mkdir dir1 dir2 dir3
```

---

# -n

Limit how many arguments are passed each time.

```bash
echo "1 2 3 4 5" | xargs -n2 echo
```

Output

```text
1 2
3 4
5
```

Equivalent execution

```bash
echo 1 2
echo 3 4
echo 5
```

Useful when a command should not receive too many arguments.

---

# -I

Replace placeholder.

```bash
echo "app.log" | xargs -I{} cp {} backup/{}
```

Equivalent

```bash
cp app.log backup/app.log
```

Placeholder can be any name.

```bash
xargs -IFILE
```

---

# -0

Safely handle filenames containing spaces or special characters.

Producer

```bash
find . -print0
```

Consumer

```bash
xargs -0
```

Example

```bash
find . -name "*.txt" -print0 | xargs -0 rm
```

Always pair

```text
-print0
```

with

```text
-0
```

---

# Common Pipeline

Delete log files

```bash
find . -name "*.log" | xargs rm
```

Search TODO

```bash
find . -name "*.py" | xargs grep TODO
```

Count lines of all Python files

```bash
find . -name "*.py" | xargs wc -l
```

Archive files

```bash
find logs -mtime +30 | xargs tar -rvf archive.tar
```

---

# xargs vs -exec

find supports built-in execution.

```bash
find . -name "*.log" -exec rm {} \;
```

Runs

```bash
rm file1
rm file2
rm file3
```

One process per file.

---

Efficient version

```bash
find . -name "*.log" -exec rm {} +
```

Runs

```bash
rm file1 file2 file3
```

Almost identical to

```bash
find . -name "*.log" | xargs rm
```

---

# stdin vs argv

Commands that mainly read **stdin**

* grep
* sort
* uniq
* head
* tail
* wc
* cut
* tr
* sed
* awk

Commands that mainly expect **argv**

* rm
* cp
* mv
* chmod
* chown
* mkdir
* gzip
* tar

`xargs` is most useful when sending data from the first group to the second.

---

# Common Mistakes

❌ Wrong

```bash
find . -name "*.log" | rm
```

`rm` ignores stdin.

---

✅ Correct

```bash
find . -name "*.log" | xargs rm
```

---

❌ Wrong

```bash
find . -name "*.py" | grep TODO
```

`grep` searches the filenames coming from stdin, not the contents of those files.

---

✅ Correct

```bash
find . -name "*.py" | xargs grep TODO
```

---

# Python Analogy

Think of

```bash
find . -name "*.py" | xargs grep TODO
```

as

```python
files = find("*.py")

grep("TODO", *files)
```

`xargs` is effectively unpacking a list into function arguments.

---

# When Should I Use xargs?

Use `xargs` whenever:

* Input comes from **stdin**
* The next command expects **argv**

Rule of thumb:

```text
Need stdin → argv ?

Use xargs.
```

---

# Interview Tips

Know these patterns by heart:

```bash
find . -name "*.log" | xargs rm
```

```bash
find . -name "*.py" | xargs grep TODO
```

```bash
find . -print0 | xargs -0 rm
```

```bash
echo "a b c" | xargs mkdir
```

```bash
echo "1 2 3 4" | xargs -n2 echo
```

Understanding **why** `xargs` exists is more important than memorizing its options:

> It converts **stdin** into **command-line arguments (argv)**.
