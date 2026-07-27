## Permutation vs Combination

| Permutation | Combination |
|-------------|-------------|
| Order matters | Order does not matter |
| `[1,2]` and `[2,1]` are different | `[1,2]` and `[2,1]` are the same |
| Uses `used[]` | Uses `start` index |
| Choose the next **position** | Choose the next **element** |

### Permutation

**Question:** Who should go in the next position?

```python
for i in range(n):
    if used[i]:
        continue
    used[i] = True
    path.append(nums[i])
    dfs()
    path.pop()
    used[i] = False
```

Example:

```
Input: [1,2,3]

123
132
213
231
312
321
```

---

### Combination

**Question:** Which remaining elements should I pick?

```python
for i in range(start, n):
    path.append(nums[i])
    dfs(i + 1)
    path.pop()
```

Example (`k = 2`):

```
Input: [1,2,3]

[1,2]
[1,3]
[2,3]
```

---

### Rule of Thumb

- **Permutation:** Arrange elements in different orders.
- **Combination:** Choose a subset of elements; order does not matter.